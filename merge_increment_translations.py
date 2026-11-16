# -*- coding: utf-8 -*-
"""
无极国际版 - 增量人工翻译一键合并与回填工具
=====================================================
说明：
当人工翻译团队完成了《本次更新_待人工翻译_增量表.xlsx》后，
执行本脚本可一键：
  1. 将人工翻译的内容精准回填至《需要翻译的文本.xlsx》与《需要翻译的图片翻译.xlsx》对应单元格。
  2. 自动将新翻译的词条追加同步到三大翻译总表（国际服繁体.xlsx、国际服印尼.xlsx、国际服英文.xlsx），
     确保后续版本更新时历史翻译库越来越完整！
"""

import os
import sys
import time
import shutil
from datetime import datetime
import openpyxl

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_INCREMENT = os.path.join(BASE_DIR, "本次更新_待人工翻译_增量表.xlsx")
FILE_TARGET_TEXT = os.path.join(BASE_DIR, "需要翻译的文本.xlsx")
FILE_TARGET_IMAGE = os.path.join(BASE_DIR, "需要翻译的图片翻译.xlsx")

FILE_MASTER_TC = os.path.join(BASE_DIR, "国际服繁体.xlsx")
FILE_MASTER_ID = os.path.join(BASE_DIR, "国际服印尼.xlsx")
FILE_MASTER_EN = os.path.join(BASE_DIR, "国际服英文.xlsx")


def clean_str(val):
    if val is None:
        return ""
    return str(val).replace("\ufeff", "").strip()


def backup_before_merge():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(BASE_DIR, f"备份_合并前_{timestamp}")
    os.makedirs(backup_dir, exist_ok=True)
    for f in [FILE_TARGET_TEXT, FILE_TARGET_IMAGE, FILE_MASTER_TC, FILE_MASTER_ID, FILE_MASTER_EN]:
        if os.path.exists(f):
            shutil.copy2(f, os.path.join(backup_dir, os.path.basename(f)))
    print(f"[+] 已创建合并前备份目录: {os.path.basename(backup_dir)}/")
    return backup_dir


def main():
    print("=" * 65)
    print("      无极国际版 - 增量人工翻译一键合并与总表更新工具")
    print("=" * 65)

    if not os.path.exists(FILE_INCREMENT):
        print(f"[X] 未找到增量翻译表: {os.path.basename(FILE_INCREMENT)}")
        print("请在翻译团队填完该表格后再执行合并。")
        sys.exit(1)

    backup_before_merge()

    print(f"[*] 正在读取增量翻译表: {os.path.basename(FILE_INCREMENT)} ...")
    wb_inc = openpyxl.load_workbook(FILE_INCREMENT, data_only=True)

    # 1. 读取文本增量
    text_updates = {}  # row_num -> (en, tc, id, zh, mod)
    new_text_entries = [] # for master appending
    if "待翻译_文本增量" in wb_inc.sheetnames:
        ws_t = wb_inc["待翻译_文本增量"]
        for row in list(ws_t.iter_rows(values_only=True))[1:]:
            if not row or len(row) < 8:
                continue
            id_val, row_num, zh, mod, remark, en, tc, id_lang = row[:8]
            en_str = clean_str(en)
            tc_str = clean_str(tc)
            id_str = clean_str(id_lang)
            zh_str = clean_str(zh)
            mod_str = clean_str(mod)

            if en_str or tc_str or id_str:
                text_updates[int(row_num)] = {
                    "en": en_str,
                    "tc": tc_str,
                    "id": id_str,
                    "zh": zh_str,
                    "mod": mod_str
                }
                new_text_entries.append((zh_str, mod_str, en_str, tc_str, id_str))

    # 2. 读取图片增量
    img_updates = {}  # row_num -> (tc, en, id)
    new_img_entries = []
    if "待翻译_图片增量" in wb_inc.sheetnames:
        ws_i = wb_inc["待翻译_图片增量"]
        for row in list(ws_i.iter_rows(values_only=True))[1:]:
            if not row or len(row) < 6:
                continue
            id_val, row_num, zh, tc, en, id_lang = row[:6]
            tc_str = clean_str(tc)
            en_str = clean_str(en)
            id_str = clean_str(id_lang)
            zh_str = clean_str(zh)

            if tc_str or en_str or id_str:
                img_updates[int(row_num)] = {
                    "tc": tc_str,
                    "en": en_str,
                    "id": id_str,
                    "zh": zh_str
                }
                new_img_entries.append((zh_str, "", en_str, tc_str, id_str))

    wb_inc.close()

    print(f"[+] 成功读取有效增量翻译：文本 {len(text_updates)} 行，图片 {len(img_updates)} 行")

    if not text_updates and not img_updates:
        print("[!] 增量表中尚未填写任何翻译内容，取消合并。")
        return

    # 回填文本表
    if text_updates and os.path.exists(FILE_TARGET_TEXT):
        print(f"[*] 正在回填《{os.path.basename(FILE_TARGET_TEXT)}》...")
        wb_txt = openpyxl.load_workbook(FILE_TARGET_TEXT)
        sheet_lang_cols = {
            "英文": "en",
            "English": "en",
            "繁体": "tc",
            "Traditional": "tc",
            "印尼": "id",
            "Indonesian": "id",
        }
        for sname in wb_txt.sheetnames:
            target_lang = None
            for k, v in sheet_lang_cols.items():
                if k in sname:
                    target_lang = v
                    break
            if not target_lang:
                continue

            ws = wb_txt[sname]
            for r_num, data in text_updates.items():
                val = data[target_lang]
                if val:
                    ws.cell(row=r_num, column=3, value=val)
        wb_txt.save(FILE_TARGET_TEXT)
        wb_txt.close()
        print(f"[+] 《{os.path.basename(FILE_TARGET_TEXT)}》回填完成！")

    # 回填图片表
    if img_updates and os.path.exists(FILE_TARGET_IMAGE):
        print(f"[*] 正在回填《{os.path.basename(FILE_TARGET_IMAGE)}》...")
        wb_img = openpyxl.load_workbook(FILE_TARGET_IMAGE)
        ws = wb_img.active
        for r_num, data in img_updates.items():
            if data["tc"]: ws.cell(row=r_num, column=3, value=data["tc"])
            if data["en"]: ws.cell(row=r_num, column=4, value=data["en"])
            if data["id"]: ws.cell(row=r_num, column=5, value=data["id"])
        wb_img.save(FILE_TARGET_IMAGE)
        wb_img.close()
        print(f"[+] 《{os.path.basename(FILE_TARGET_IMAGE)}》回填完成！")

    # 同步追加更新到三大总表
    print("[*] 正在同步追加新词条至三大历史翻译总表...")
    all_new = new_text_entries + new_img_entries
    
    # 追加繁体
    wb_tc = openpyxl.load_workbook(FILE_MASTER_TC)
    ws_tc = wb_tc["语言表"] if "语言表" in wb_tc.sheetnames else wb_tc.active
    added_tc = 0
    for zh, mod, en, tc, id_lang in all_new:
        if tc:
            ws_tc.append([zh, tc, mod])
            added_tc += 1
    wb_tc.save(FILE_MASTER_TC)
    wb_tc.close()

    # 追加英文
    wb_en = openpyxl.load_workbook(FILE_MASTER_EN)
    ws_en = wb_en.active
    added_en = 0
    for zh, mod, en, tc, id_lang in all_new:
        if en:
            ws_en.append([zh, en, mod])
            added_en += 1
    wb_en.save(FILE_MASTER_EN)
    wb_en.close()

    # 追加印尼
    wb_id = openpyxl.load_workbook(FILE_MASTER_ID)
    ws_id = wb_id.active
    added_id = 0
    for zh, mod, en, tc, id_lang in all_new:
        if id_lang:
            ws_id.append([zh, id_lang, mod])
            added_id += 1
    wb_id.save(FILE_MASTER_ID)
    wb_id.close()

    print(f"[+] 总表同步完毕！(繁体新增 {added_tc} 条, 英文新增 {added_en} 条, 印尼新增 {added_id} 条)")
    print("\n[V] 全部合并与更新操作顺利完成！")
    print("=" * 65)


if __name__ == "__main__":
    main()
