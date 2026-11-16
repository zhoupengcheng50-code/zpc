# -*- coding: utf-8 -*-
"""
无极仙途国际化翻译工作台 - Web 核心服务
FastAPI 高性能异步后端（支持多项目绝对物理隔离与动态无缝切换）
"""

import os
import sys
import time
import shutil
import socket
from typing import List, Optional
from pydantic import BaseModel

from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# 确保能加载本地模块
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

from engine import MemoryStore, TranslationEngine, align_text_symbols, ProjectManager

# 基础目录
BASE_DIR = os.path.dirname(CURRENT_DIR)
TEMPLATES_DIR = os.path.join(CURRENT_DIR, "templates")
STATIC_DIR = os.path.join(CURRENT_DIR, "static")
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)

# 初始化多项目管理器（完全物理隔离：各项目独享 memory_db, uploads, outputs）
project_manager = ProjectManager(CURRENT_DIR)

app = FastAPI(
    title="无极仙途国际化翻译工作台",
    description="专为游戏出海打造的智能本地化翻译与质检平台（多项目绝对隔离）",
    version="2.0.0"
)

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# 允许跨域（方便外网或各种客户端访问）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_local_ip():
    """获取本机局域网 IP"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


# 数据模型
class CreateProjectRequest(BaseModel):
    name: str
    desc: Optional[str] = ""
    icon: Optional[str] = ""


class ManualFixItem(BaseModel):
    sheet: str
    row: int
    col: int
    zh: Optional[str] = ""
    lang: Optional[str] = ""
    value: str


class FixIssuesRequest(BaseModel):
    output_filename: str
    project_id: Optional[str] = "wuji"
    manual_fixes: Optional[List[ManualFixItem]] = []


@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_file = os.path.join(TEMPLATES_DIR, "index.html")
    if os.path.exists(index_file):
        with open(index_file, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>无极仙途国际化翻译工作台正在初始化，请稍候刷新...</h1>"


# 项目管理 API
@app.get("/api/projects")
async def list_projects():
    """获取所有项目列表及各项目词库统计"""
    return {
        "projects": project_manager.list_projects()
    }


@app.post("/api/projects")
async def create_project(req: CreateProjectRequest):
    """创建新项目（自动创建独立 memory_db, uploads, outputs 目录，完全物理隔离）"""
    try:
        pinfo = project_manager.create_project(req.name, req.desc, req.icon)
        return {
            "success": True,
            "message": f"项目【{pinfo['name']}】创建成功！",
            "project": pinfo,
            "projects": project_manager.list_projects()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/api/projects/{project_id}")
async def delete_project(project_id: str):
    """删除非核心项目"""
    try:
        project_manager.delete_project(project_id)
        return {
            "success": True,
            "message": "项目已成功删除",
            "projects": project_manager.list_projects()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/system/status")
async def get_system_status(project_id: str = "wuji"):
    """获取系统运行状态、网络地址及当前项目状态"""
    local_ip = get_local_ip()
    store, _ = project_manager.get_project(project_id)
    return {
        "status": "online",
        "app_name": "无极仙途国际化翻译",
        "version": "2.0.0",
        "local_url": "http://127.0.0.1:8000",
        "lan_url": f"http://{local_ip}:8000",
        "projects": project_manager.list_projects(),
        "active_project_id": project_id,
        "memory_stats": store.get_stats()
    }


@app.get("/api/memory/stats")
async def get_memory_stats(project_id: str = "wuji"):
    """获取指定项目的术语库记忆详情（完全隔离）"""
    store, _ = project_manager.get_project(project_id)
    return store.get_stats()


@app.post("/api/memory/upload")
async def upload_memory_file(
    file: UploadFile = File(...),
    project_id: str = Form("wuji")
):
    """
    上传术语库/翻译总表文件到指定项目
    自动识别语言并持久化保存为该项目的专属记忆点，杜绝项目间污染
    """
    if not file.filename.endswith((".xlsx", ".xlsm")):
        raise HTTPException(status_code=400, detail="请上传 .xlsx 格式的 Excel 文件！")

    dirs = project_manager.get_project_dirs(project_id)
    save_path = os.path.join(dirs["uploads"], f"master_{int(time.time())}_{file.filename}")
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        store, _ = project_manager.get_project(project_id)
        res = store.ingest_excel(save_path, original_filename=file.filename)
        return {
            "success": True,
            "message": f"成功录入【{res['label']}】术语记忆！共新增/更新 {res['total']} 条词汇。",
            "detail": res,
            "current_stats": store.get_stats()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"解析术语库文件失败: {str(e)}")


@app.post("/api/translate")
async def run_translation(
    file: UploadFile = File(...),
    project_id: str = Form("wuji")
):
    """
    在指定项目下上传待翻译文件并执行智能比对、格式严谨对齐与自动化质检
    """
    if not file.filename.endswith((".xlsx", ".xlsm")):
        raise HTTPException(status_code=400, detail="请上传 .xlsx 格式的待翻译 Excel 文件！")

    dirs = project_manager.get_project_dirs(project_id)
    target_save_path = os.path.join(dirs["uploads"], file.filename)
    with open(target_save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        _, engine = project_manager.get_project(project_id)
        result = engine.process_file(target_save_path, original_filename=file.filename)
        return {
            "success": True,
            "message": f"智能比对完成！已处理 {result['stats']['total_rows']} 行文本，发现 {result['stats']['issue_count']} 项需关注/修复项。",
            "stats": result["stats"],
            "issues": result["issues"][:300],  # 限制前端初次渲染数量
            "total_issues": len(result["issues"]),
            "output_filename": result["download_filename"],
            "project_id": project_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"翻译比对处理失败: {str(e)}")


@app.post("/api/fix_issues")
async def fix_issues(req: FixIssuesRequest):
    """
    针对指定项目的翻译成果执行一键智能修复与纠错
    """
    pid = req.project_id or "wuji"
    dirs = project_manager.get_project_dirs(pid)
    file_path = os.path.join(dirs["outputs"], req.output_filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="目标文件不存在，请先执行翻译！")

    try:
        manual_list = []
        if req.manual_fixes:
            for item in req.manual_fixes:
                if hasattr(item, "model_dump"):
                    manual_list.append(item.model_dump())
                else:
                    manual_list.append(item.dict())
        _, engine = project_manager.get_project(pid)
        res = engine.execute_auto_fix(file_path, manual_fixes=manual_list)

        # 修复后重新全量质检，生成全新问题清单
        re_audit = engine.process_file(file_path, original_filename=req.output_filename.replace("已完成翻译_", ""))

        return {
            "success": True,
            "message": res["message"],
            "fixes_applied": res["fixes_applied"],
            "remaining_issues_count": len(re_audit["issues"]),
            "remaining_issues": re_audit["issues"][:300],
            "stats": re_audit["stats"],
            "output_filename": req.output_filename,
            "project_id": pid
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"执行修复失败: {str(e)}")


@app.get("/api/download/{project_id}/{filename}")
async def download_file_by_project(project_id: str, filename: str):
    """从指定项目成果区下载 Excel 文件"""
    dirs = project_manager.get_project_dirs(project_id)
    file_path = os.path.join(dirs["outputs"], filename)
    if not os.path.exists(file_path):
        alt_path = os.path.join(dirs["uploads"], filename)
        if os.path.exists(alt_path):
            file_path = alt_path
        else:
            raise HTTPException(status_code=404, detail="文件不存在或已被移除！")

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


@app.get("/api/download/{filename}")
async def download_file_legacy(filename: str, project_id: Optional[str] = None):
    """兼容旧版下载请求路由"""
    pid = project_id or "wuji"
    dirs = project_manager.get_project_dirs(pid)
    file_path = os.path.join(dirs["outputs"], filename)
    if not os.path.exists(file_path):
        found = False
        for p in project_manager.list_projects():
            p_dirs = project_manager.get_project_dirs(p["id"])
            test_path = os.path.join(p_dirs["outputs"], filename)
            if os.path.exists(test_path):
                file_path = test_path
                found = True
                break
        if not found:
            raise HTTPException(status_code=404, detail="文件不存在或已被移除！")

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
