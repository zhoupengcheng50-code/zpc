# -*- coding: utf-8 -*-
"""
无极仙途国际化翻译 - 核心业务引擎与多项目隔离系统
包含：
1. 术语库与记忆库智能识别、加载与持久化存储
2. 多语言智能比对与翻译回填
3. 严格格式与特殊符号对齐机制（编号1、、括号【】、间隔号·、乘号×等）
4. 占位符严格守恒（[fighterName:1] 等代码变量 100% 保护，绝不篡改为 %s）
5. 标签与后缀严格对齐（如 `'s effect`、魔印属性词缀后置等）
6. 多项目完全隔离管理器（ProjectManager）：每个项目拥有独立的术语记忆库、上传与导出目录，绝对互不污染
"""

import os
import re
import json
import time
import shutil
import openpyxl
from datetime import datetime

# 专有图片词汇映射表
IMG_TERM_MAP = {
    "已通关": {"tc": "已通關", "en": "Cleared", "id": "Selesai"},
    "天下无敌": {"tc": "天下無敵", "en": "Invincible", "id": "Tak Terkalahkan"},
    "地阶初级": {"tc": "地階初級", "en": "G.Earth Primary", "id": "G.Earth Pemula"},
    "地阶高级": {"tc": "地階高級", "en": "G.Earth Adv.", "id": "G.Earth Lanjutan"},
    "黄阶初级": {"tc": "黃階初級", "en": "G.Novice Primary", "id": "G.Pemula Dasar"},
    "黄阶高级": {"tc": "黃階高級", "en": "G.Novice Adv.", "id": "G.Pemula Lanjutan"},
    "天阶初级": {"tc": "天階初級", "en": "G.Heaven Primary", "id": "G.Surga Pemula"},
    "天阶高级": {"tc": "天階高級", "en": "G.Heaven Adv.", "id": "G.Surga Lanjutan"},
    "玄阶初级": {"tc": "玄階初級", "en": "G.Mythic Primary", "id": "G.Mistik Pemula"},
    "玄阶高级": {"tc": "玄階高級", "en": "G.Mythic Adv.", "id": "G.Mistik Lanjutan"},
    "武神": {"tc": "武神", "en": "War God", "id": "Dewa Perang"},
    "禁制": {"tc": "禁制", "en": "Restriction", "id": "Larangan"},
    "礼包": {"tc": "禮包", "en": "Gift Pack", "id": "Paket Hadiah"},
    "胜利": {"tc": "勝利", "en": "Victory", "id": "Kemenangan"},
    "败": {"tc": "敗", "en": "Defeat", "id": "Kekalahan"},
    "段位提升": {"tc": "段位提升", "en": "Tier Up", "id": "Tingkat Naik"},
    "论道大会": {"tc": "論道大會", "en": "Theory Assembly", "id": "Pertemuan Teori"},
    "赛季冠军": {"tc": "賽季冠軍", "en": "Season Champion", "id": "Juara Musim"},
    "论道榜": {"tc": "論道榜", "en": "Theory Rankings", "id": "Peringkat Teori"},
    "灵运": {"tc": "靈運", "en": "Spirit Fortune", "id": "Keberuntungan Roh"},
    "凶兽来袭": {"tc": "兇獸來襲", "en": "Beasts Strike", "id": "Binatang Buas Menyerang"},
    "仙册·春": {"tc": "仙冊·春", "en": "Immortal Book·Spring", "id": "Buku Abadi·Musim Semi"},
    "仙册·夏": {"tc": "仙冊·夏", "en": "Immortal Book·Summer", "id": "Buku Abadi·Musim Panas"},
    "仙册·秋": {"tc": "仙冊·秋", "en": "Immortal Book·Autumn", "id": "Buku Abadi·Musim Gugur"},
    "仙册·冬": {"tc": "仙冊·冬", "en": "Immortal Book·Winter", "id": "Buku Abadi·Musim Dingin"},
    "福地灵运": {"tc": "福地靈運", "en": "Blessed Land Spirit Fortune", "id": "Keberuntungan Roh Tanah Berkah"},
    "福地仙册": {"tc": "福地仙冊", "en": "Blessed Land Immortal Book", "id": "Buku Abadi Tanah Berkah"},
    "完成福地挑战任务领取丰厚奖励！": {
        "tc": "完成福地挑戰任務領取豐厚獎勵！",
        "en": "Complete Blessed Land challenge quests to claim rich rewards！",
        "id": "Selesaikan misi tantangan tanah berkah untuk mengklaim hadiah berlimpah！"
    },
    "新功能开启": {"tc": "新功能開啟", "en": "New Function Unlocked", "id": "Fungsi Baru Dibuka"},
    "便捷分解": {"tc": "便捷分解", "en": "Quick Disassemble", "id": "Bongkar Cepat"}
}

def clean_str(val):
    if val is None:
        return ""
    return str(val).replace("\ufeff", "").strip()

def normalize_key(val):
    return clean_str(val).replace("\r\n", "\n").replace("\\n", "\n")

def clean_tag_spaces_and_typos(text):
    if not text:
        return text
    s = str(text)
    # 修复印尼语错误翻译的标签 warna -> color
    s = re.sub(r'<\s*warna\s*=\s*', '<color=', s, flags=re.I)
    s = re.sub(r'<\s*/\s*warna\s*>', '</color>', s, flags=re.I)
    # 修复闭合标签中的异常空格 < /color> 或 </ color>
    s = re.sub(r'<\s*/\s*color\s*>', '</color>', s, flags=re.I)
    # 修复开始标签中的异常空格 <color=# 0000FF> -> <color=#0000FF>
    s = re.sub(r'<color\s*=\s*#\s+([0-9a-fA-F]+)>', r'<color=#\1>', s)
    s = re.sub(r'<color\s*=\s*', '<color=', s, flags=re.I)
    # 修复标签首尾多余空格
    s = re.sub(r'(<color=[^>]+>)\s+', r'\1', s)
    s = re.sub(r'\s+(</color>)', r'\1', s)
    return s

def fix_placeholders(zh, tr):
    if not zh or not tr:
        return tr
    s = str(tr)
    # 针对 [fighterName:1] 变成了 %s 的特殊处理
    if '[fighterName:1]' in zh and '[fighterName:1]' not in s:
        if '%s' in s:
            s = s.replace('%s', '[fighterName:1]', 1)
        else:
            s = re.sub(r'(<color=[^>]+>)[^<]+(</color>)', r'\1[fighterName:1]\2', s, count=1)
            
    # 针对其他类似 [fighterName:2] 等
    for m in re.finditer(r'\[([a-zA-Z0-9_:]+)\]', zh):
        token = m.group(0)
        if token not in s:
            if '%s' in s and zh.count('%s') < s.count('%s'):
                s = s.replace('%s', token, 1)

    # 针对 %S 大写篡改规范化：如果原文是 %s，译文出现 %S，必须严格恢复为 %s
    if '%s' in zh and '%S' in s:
        s = s.replace('%S', '%s')

    return s

def fix_inverted_tag_phrases(zh, tr, lang_key):
    if not zh or not tr:
        return tr
    
    # 针对：<color=#9e4444>筑基期</color>至<color=#9e4444>炼虚期</color>每10级可开启1次。\n核心奖励：...
    if zh.startswith('<color=#9e4444>筑基期</color>至<color=#9e4444>炼虚期</color>'):
        parts = re.split(r'\\n|\n', tr)
        second_part = parts[1] if len(parts) > 1 else ""
        if lang_key == 'en':
            second_part = re.sub(r'^Main rewards\s*[:：]\s*', 'Main rewards：', second_part)
            second_part = second_part.replace('  ', ' ')
            first_part = "<color=#9e4444>Base Phase</color> to <color=#9e4444>Vainify Phase</color>：Can be enabled once every 10 levels."
            return f"{first_part}\\n{second_part}" if second_part else first_part
        elif lang_key == 'id':
            second_part = re.sub(r'^Hadiah utama\s*[:：]\s*', 'Hadiah utama：', second_part)
            second_part = second_part.replace('  ', ' ')
            first_part = "<color=#9e4444>Fase Basis</color> hingga <color=#9e4444>Fase Merusak</color>：Dapat diaktifkan sekali setiap 10 level."
            return f"{first_part}\\n{second_part}" if second_part else first_part

    # 针对：<color=#ad2228>[fighterName:1]</color>触发了<color=#b77f52>本命飞剑流云</color>的效果
    if "的效果" in zh and "<color=" in zh:
        if lang_key == 'en':
            tr = re.sub(r'triggered the effect of (<color=[^>]+>[^<]+</color>)', r"triggered \1's effect", tr, flags=re.I)
        elif lang_key == 'id':
            tr = re.sub(r'telah memicu efek (<color=[^>]+>[^<]+</color>)', r"memicu efek \1", tr, flags=re.I)

    # 针对魔印属性词缀位于标签后：增加<color=#458114>X点</color>YY
    if "增加<color=#458114>" in zh and lang_key == 'en':
        attr_map = {
            '金系伤害': 'Gold Damage', '水系伤害': 'Water Damage', '火系伤害': 'Fire Damage',
            '木系伤害': 'Wood Damage', '土系伤害': 'Earth Damage', '真气': 'Qi',
            '身法': 'Agility', '根骨': 'Strength', '体魄': 'Health'
        }
        m = re.search(r'增加<color=#458114>(\d+)点</color>(金系伤害|水系伤害|火系伤害|木系伤害|土系伤害|真气|身法|根骨|体魄)', zh)
        if m:
            val, attr_zh = m.group(1), m.group(2)
            attr_en = attr_map[attr_zh]
            tr = re.sub(r'to increase [^<]+ by <color=#458114>' + val + r'</color>', f'to increase <color=#458114>{val}</color> {attr_en}', tr, flags=re.I)

    # 针对：玩家<color=#9e4444>%s</color>接引码
    if zh == '玩家<color=#9e4444>%s</color>接引码' and lang_key == 'en':
        return "Player <color=#9e4444>%s</color>'s Invite Code"

    # 针对：<color=#b77f52>%s</color>不足，无法直升
    if zh == '<color=#b77f52>%s</color>不足，无法直升':
        if lang_key == 'en': return '<color=#b77f52>%s</color> is insufficient, cannot directly upgrade'
        elif lang_key == 'id': return '<color=#b77f52>%s</color> tidak cukup, tidak dapat langsung ditingkatkan'

    # 针对：<color=#ad2228>红色至宝</color>分解获得，用于<color=#ad2228>红色至宝</color>启灵
    if zh == '<color=#ad2228>红色至宝</color>分解获得，用于<color=#ad2228>红色至宝</color>启灵':
        if lang_key == 'en': return 'Obtained by dismantling <color=#ad2228>Red Secret Treasures</color>, used to Enlighten <color=#ad2228>Red Treasures</color>'
        elif lang_key == 'id': return 'Diperoleh dengan membongkar <color=#ad2228>Harta Karun Merah</color>, digunakan untuk Mencerahkan <color=#ad2228>Harta Karun Merah</color>'

    return tr

def align_text_symbols(zh_orig, tr_text, lang_key="en"):
    """
    严格对齐符号与格式，确保符号、占位符与原文绝对一致
    """
    if not zh_orig or not tr_text:
        return tr_text

    zh = str(zh_orig)
    tr = str(tr_text)

    # 1. 基础标签清洗与异常修复
    tr = clean_tag_spaces_and_typos(tr)

    # 2. 占位符与变量保护恢复（如 [fighterName:1]、%S -> %s）
    tr = fix_placeholders(zh, tr)
    if "%s" in zh and "%S" in tr:
        tr = tr.replace("%S", "%s")

    # 3. 标签语序颠倒修复
    tr = fix_inverted_tag_phrases(zh, tr, lang_key)

    # 4. 编号严格对齐：如 1、 2、 3、 ... 9、
    for i in range(1, 10):
        if f"{i}、" in zh:
            tr = re.sub(rf"(^|\\n|\n|\s+)({i})[\.\)]\s*", rf"\g<1>{i}、", tr)
        elif f"{i}." in zh:
            tr = re.sub(rf"(^|\\n|\n|\s+)({i})[、\)]\s*", rf"\g<1>{i}.", tr)
        elif f"({i})" in zh or f"（{i}）" in zh:
            sym_l = "（" if f"（{i}）" in zh else "("
            sym_r = "）" if f"（{i}）" in zh else ")"
            tr = re.sub(rf"(^|\\n|\n|\s+)[（\(]({i})[）\)]\s*", rf"\g<1>{sym_l}{i}{sym_r}", tr)

    # 5. 特殊括号对齐：【 】
    if "【" in zh and "】" in zh:
        tr = re.sub(r"\[([^\]]+)\]", r"【\1】", tr)
    elif "[" in zh and "]" in zh and not ("【" in zh):
        tr = tr.replace("【", "[").replace("】", "]")

    # 6. 书名号对齐：《 》
    if "《" in zh and "》" in zh:
        tr = re.sub(r'“([^”]+)”|"([^"]+)"|「([^」]+)」', r"《\1\2\3》", tr)

    # 7. 双引号对齐：“ ”
    if "“" in zh and "”" in zh:
        tr = tr.replace("「", "“").replace("」", "”")
        parts = tr.split('"')
        if len(parts) > 1 and len(parts) % 2 == 1:
            rebuilt = []
            for idx, p in enumerate(parts):
                rebuilt.append(p)
                if idx < len(parts) - 1:
                    rebuilt.append("“" if idx % 2 == 0 else "”")
            tr = "".join(rebuilt)

    # 8. 圆括号严格对齐：（ ） vs ( )
    if "（" in zh and "）" in zh:
        tr = tr.replace("(", "（").replace(")", "）")
    elif "(" in zh and ")" in zh:
        tr = tr.replace("（", "(").replace("）", ")")

    # 9. 间隔号对齐：· (middle dot)
    if "·" in zh:
        tr = re.sub(r"\s*[\-–—]\s*(?=Fragmen|Fragment|Pecahan|Shard|Musim|Spring|Summer|Autumn|Winter|春|夏|秋|冬|碎片)", "·", tr, flags=re.I)
        if "·碎片" in zh and "·" not in tr:
            tr = re.sub(r"\s+(Fragment|Shard|Pecahan|Fragmen)", r"·\1", tr, flags=re.I)
            if "·" not in tr and ("Fragment" in tr or "Shard" in tr):
                tr = re.sub(r"([a-zA-Z0-9]+)\s+(Fragment|Shard)", r"\1·\2", tr)
        tr = re.sub(r"\s*·\s*", "·", tr)

    # 10. 乘号对齐：×
    if "×" in zh:
        tr = re.sub(r"\s*[xX\*]\s*(?=[0-9%])", "×", tr)
        tr = re.sub(r"(?<=[0-9%])\s*[xX\*]\s*", "×", tr)

    # 11. 波浪号对齐：～ vs ~
    if "～" in zh:
        tr = tr.replace("~", "～")
    elif "~" in zh:
        tr = tr.replace("～", "~")

    # 12. 省略号对齐：……
    if "……" in zh:
        tr = re.sub(r"\.{3,6}|…{1,2}", "……", tr)

    # 13. 破折号对齐：——
    if "——" in zh:
        tr = re.sub(r"--+|——+|——", "——", tr)

    # 14. 冒号对齐：： vs :
    if "：" in zh:
        tr = tr.replace(":", "：").replace("： ", "：")
    elif ":" in zh and "：" not in zh:
        tr = tr.replace("：", ":")

    # 15. 分号对齐：； vs ;
    if "；" in zh:
        tr = tr.replace(";", "；").replace("； ", "；")
    elif ";" in zh:
        tr = tr.replace("；", ";")

    # 16. 感叹号与问号全半角对齐
    if "！" in zh:
        tr = tr.replace("!", "！")
    elif "!" in zh:
        tr = tr.replace("！", "!")

    if "？" in zh:
        tr = tr.replace("?", "？")
    elif "?" in zh:
        tr = tr.replace("？", "?")

    # 17. 顿号对齐
    if "、" in zh and ("*" in zh or "%s" in zh):
        tr = re.sub(r",\s*", "、", tr)

    # 18. 多余连续空格清洗
    tr = re.sub(r" {2,}", " ", tr)

    # 19. 首尾空白字符严格匹配
    if zh.startswith(" ") and not tr.startswith(" "):
        tr = " " + tr
    elif not zh.startswith(" ") and tr.startswith(" "):
        tr = tr.lstrip(" ")

    if zh.endswith(" ") and not tr.endswith(" "):
        tr = tr + " "
    elif not zh.endswith(" ") and tr.endswith(" "):
        tr = tr.rstrip(" ")

    # 20. 句末句号对齐
    if not zh.endswith("。") and not zh.endswith("."):
        if tr.endswith("。") or tr.endswith("."):
            tr = tr[:-1]

    return tr


class MemoryStore:
    """
    单个项目的术语库与记忆库管理类
    数据存储在项目独立的 memory_db 目录中，与其他项目完全隔离
    """
    def __init__(self, db_dir):
        self.db_dir = db_dir
        os.makedirs(self.db_dir, exist_ok=True)
        self.tc_file = os.path.join(self.db_dir, "tc_memory.json")
        self.en_file = os.path.join(self.db_dir, "en_memory.json")
        self.id_file = os.path.join(self.db_dir, "id_memory.json")
        self.incremental_file = os.path.join(self.db_dir, "incremental_translations.json")
        self.meta_file = os.path.join(self.db_dir, "meta.json")

        self.tc_data = {"text": {}, "mod": {}, "norm": {}}
        self.en_data = {"text": {}, "mod": {}, "norm": {}}
        self.id_data = {"text": {}, "mod": {}, "norm": {}}
        self.incremental_dict = {}
        self.meta = {}

        self.load_all()

    def load_all(self):
        self.tc_data = self._load_lang_data(self.tc_file)
        self.en_data = self._load_lang_data(self.en_file)
        self.id_data = self._load_lang_data(self.id_file)

        if os.path.exists(self.incremental_file):
            try:
                with open(self.incremental_file, "r", encoding="utf-8") as f:
                    self.incremental_dict = json.load(f)
            except Exception as e:
                print(f"[!] 加载增量词库失败: {e}")
                self.incremental_dict = {}
        else:
            self.incremental_dict = {}

        if os.path.exists(self.meta_file):
            try:
                with open(self.meta_file, "r", encoding="utf-8") as f:
                    self.meta = json.load(f)
            except Exception:
                self.meta = {}
        else:
            self.meta = {}

    def _load_lang_data(self, fpath):
        if os.path.exists(fpath):
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"[!] 读取记忆文件 {fpath} 失败: {e}")
        return {"text": {}, "mod": {}, "norm": {}}

    def _save_lang_data(self, fpath, data):
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

    def save_meta(self):
        with open(self.meta_file, "w", encoding="utf-8") as f:
            json.dump(self.meta, f, ensure_ascii=False, indent=2)

    def save_incremental(self):
        with open(self.incremental_file, "w", encoding="utf-8") as f:
            json.dump(self.incremental_dict, f, ensure_ascii=False, indent=2)

    def detect_language(self, filename, sample_rows=None):
        fname = filename.lower()
        if "繁体" in fname or "tc" in fname or "cht" in fname or "traditional" in fname:
            return "tc"
        if "英文" in fname or "en" in fname or "english" in fname:
            return "en"
        if "印尼" in fname or "id" in fname or "indo" in fname or "indonesia" in fname:
            return "id"
        return "tc"

    def ingest_excel(self, file_path, original_filename=""):
        fname = original_filename or os.path.basename(file_path)
        lang = self.detect_language(fname)

        wb = openpyxl.load_workbook(file_path, read_only=True, data_only=True)
        sheet_name = "语言表" if "语言表" in wb.sheetnames else wb.sheetnames[0]
        ws = wb[sheet_name]

        target_dict = getattr(self, f"{lang}_data")
        text_d = target_dict.setdefault("text", {})
        mod_d = target_dict.setdefault("mod", {})
        norm_d = target_dict.setdefault("norm", {})

        count_added = 0
        row_idx = 0
        for row in ws.iter_rows(values_only=True):
            row_idx += 1
            if row_idx == 1:
                continue
            if not row or row[0] is None or len(row) < 2 or row[1] is None:
                continue

            zh = clean_str(row[0])
            raw_trans = clean_str(row[1])
            mod = clean_str(row[2]) if len(row) > 2 and row[2] else ""

            if not zh or not raw_trans:
                continue

            trans = align_text_symbols(zh, raw_trans, lang)

            if mod:
                mod_d[f"{zh}__MOD__{mod}"] = trans
            if zh not in text_d:
                count_added += 1
            text_d[zh] = trans
            norm_d[normalize_key(zh)] = trans

        wb.close()

        fpath = getattr(self, f"{lang}_file")
        self._save_lang_data(fpath, target_dict)

        lang_label = {"tc": "繁体中文", "en": "英文", "id": "印尼语"}.get(lang, lang)
        self.meta[lang] = {
            "name": fname,
            "lang": lang,
            "label": lang_label,
            "total_terms": len(text_d),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.save_meta()

        return {
            "lang": lang,
            "label": lang_label,
            "filename": fname,
            "added": count_added,
            "total": len(text_d)
        }

    def import_seed_data(self, workspace_dir):
        inc_path = os.path.join(workspace_dir, "incremental_translations.json")
        if os.path.exists(inc_path) and not os.path.exists(self.incremental_file):
            shutil.copy2(inc_path, self.incremental_file)
            with open(self.incremental_file, "r", encoding="utf-8") as f:
                self.incremental_dict = json.load(f)

        seeds = [
            ("国际服繁体.xlsx", "tc", self.tc_file),
            ("国际服英文.xlsx", "en", self.en_file),
            ("国际服印尼.xlsx", "id", self.id_file),
        ]
        for src_name, lang, dst_file in seeds:
            src_path = os.path.join(workspace_dir, src_name)
            if os.path.exists(src_path) and not os.path.exists(dst_file):
                print(f"[*] 正在自动导入预设术语库: {src_name} ...")
                self.ingest_excel(src_path, src_name)

        self.load_all()

    def get_stats(self):
        return {
            "tc": {
                "label": "繁体中文",
                "count": len(self.tc_data.get("text", {})),
                "last_file": self.meta.get("tc", {}).get("name", "未录入"),
                "updated_at": self.meta.get("tc", {}).get("updated_at", "-")
            },
            "en": {
                "label": "英语 (English)",
                "count": len(self.en_data.get("text", {})),
                "last_file": self.meta.get("en", {}).get("name", "未录入"),
                "updated_at": self.meta.get("en", {}).get("updated_at", "-")
            },
            "id": {
                "label": "印尼语 (Indonesian)",
                "count": len(self.id_data.get("text", {})),
                "last_file": self.meta.get("id", {}).get("name", "未录入"),
                "updated_at": self.meta.get("id", {}).get("updated_at", "-")
            },
            "incremental": {
                "label": "版本增量专有词库",
                "count": len(self.incremental_dict),
                "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        }

    def set_term(self, zh, trans, lang):
        """永久保存单个词条的质检修复与人工调整到增量词库与主记忆库"""
        if not zh or not trans or not lang:
            return
        zh_clean = clean_str(zh)
        zh_norm = normalize_key(zh_clean)

        # 1. 写入增量记忆
        if zh_clean not in self.incremental_dict:
            self.incremental_dict[zh_clean] = {}
        self.incremental_dict[zh_clean][lang] = trans
        self.save_incremental()

        # 2. 写入主语言字典
        target_dict = getattr(self, f"{lang}_data", None)
        if target_dict:
            target_dict.setdefault("text", {})[zh_clean] = trans
            target_dict.setdefault("norm", {})[zh_norm] = trans
            fpath = getattr(self, f"{lang}_file")
            self._save_lang_data(fpath, target_dict)

    def query(self, zh, mod, lang):
        if not zh:
            return None
        zh_clean = clean_str(zh)
        zh_norm = normalize_key(zh_clean)
        mod_str = clean_str(mod) if mod else ""

        # 1. 最高优先级：增量字典 (质检修复、人工校对的高保真记忆)
        if zh_clean in self.incremental_dict and lang in self.incremental_dict[zh_clean]:
            return self.incremental_dict[zh_clean][lang]
        if zh_norm in self.incremental_dict and lang in self.incremental_dict[zh_norm]:
            return self.incremental_dict[zh_norm][lang]

        # 2. 模块级专属字典与语言总表
        target_dict = getattr(self, f"{lang}_data", None)
        if target_dict:
            text_d = target_dict.get("text", {})
            mod_d = target_dict.get("mod", {})
            norm_d = target_dict.get("norm", {})

            if mod_str and f"{zh_clean}__MOD__{mod_str}" in mod_d:
                return mod_d[f"{zh_clean}__MOD__{mod_str}"]
            if zh_clean in text_d:
                return text_d[zh_clean]
            if zh_norm in norm_d:
                return norm_d[zh_norm]

        # 3. 专有图片词汇表
        if zh_clean in IMG_TERM_MAP and lang in IMG_TERM_MAP[zh_clean]:
            return IMG_TERM_MAP[zh_clean][lang]

        return None


class TranslationEngine:
    def __init__(self, memory_store: MemoryStore, outputs_dir: str):
        self.memory = memory_store
        self.outputs_dir = outputs_dir
        os.makedirs(self.outputs_dir, exist_ok=True)

    def process_file(self, file_path, original_filename=""):
        fname = original_filename or os.path.basename(file_path)
        wb = openpyxl.load_workbook(file_path)

        is_picture_table = False
        if "图片" in fname or "image" in fname.lower() or (len(wb.sheetnames) == 1 and wb.active.max_column >= 5 and "印尼" in str(wb.active.cell(1, 5).value or "")):
            is_picture_table = True

        out_fname = f"已完成翻译_{fname}"
        out_path = os.path.join(self.outputs_dir, out_fname)

        issues = []
        stats = {
            "filename": fname,
            "out_filename": out_fname,
            "is_picture_table": is_picture_table,
            "total_rows": 0,
            "matched_rows": 0,
            "filled_rows": 0,
            "issue_count": 0,
            "sheets": []
        }

        if is_picture_table:
            ws = wb.active
            total_rows = ws.max_row - 1
            matched = 0
            stats["total_rows"] = total_rows

            for r in range(2, ws.max_row + 1):
                zh_val = ws.cell(row=r, column=2).value
                if not zh_val:
                    continue

                for col_idx, lang, lang_name in [(3, "tc", "繁体"), (4, "en", "英文"), (5, "id", "印尼")]:
                    cur_val = clean_str(ws.cell(row=r, column=col_idx).value)
                    trans = self.memory.query(zh_val, None, lang)
                    if not trans:
                        trans = cur_val

                    if trans:
                        final_trans = align_text_symbols(zh_val, trans, lang)
                        ws.cell(row=r, column=col_idx, value=final_trans)
                        issue = self._check_cell_issue(zh_val, final_trans, lang, ws.title, r, col_idx, lang_name)
                        if issue:
                            issues.append(issue)
                    else:
                        issues.append({
                            "id": f"issue_{len(issues)+1}",
                            "sheet": ws.title,
                            "row": r,
                            "col": col_idx,
                            "col_name": lang_name,
                            "lang": lang,
                            "zh": str(zh_val),
                            "cur_trans": "",
                            "issue_type": "EMPTY",
                            "issue_desc": f"【{lang_name}】未翻译，单元格为空",
                            "suggested_fix": zh_val if lang == "tc" else ""
                        })

                matched += 1

            stats["matched_rows"] = matched
            stats["filled_rows"] = matched
            stats["sheets"].append({"name": ws.title, "rows": total_rows, "matched": matched})

        else:
            sheet_meta = [
                ("英文 (English)", "en", "英文"),
                ("繁体 (Traditional Chinese)", "tc", "繁体"),
                ("印尼语 (Indonesian)", "id", "印尼"),
            ]

            total_all = 0
            matched_all = 0

            for sname, lang, lang_name in sheet_meta:
                if sname not in wb.sheetnames:
                    matched_names = [n for n in wb.sheetnames if lang_name in n or lang in n.lower()]
                    if matched_names:
                        ws = wb[matched_names[0]]
                    else:
                        continue
                else:
                    ws = wb[sname]

                sheet_rows = ws.max_row - 1
                total_all += sheet_rows
                sheet_matched = 0

                for r in range(2, ws.max_row + 1):
                    zh_val = ws.cell(row=r, column=2).value
                    mod_val = ws.cell(row=r, column=4).value
                    if not zh_val:
                        continue

                    cur_val = clean_str(ws.cell(row=r, column=3).value)
                    trans = self.memory.query(zh_val, mod_val, lang)
                    if not trans:
                        trans = cur_val

                    if trans:
                        final_trans = align_text_symbols(zh_val, trans, lang)
                        ws.cell(row=r, column=3, value=final_trans)
                        sheet_matched += 1

                        issue = self._check_cell_issue(zh_val, final_trans, lang, ws.title, r, 3, lang_name)
                        if issue:
                            issues.append(issue)
                    else:
                        issues.append({
                            "id": f"issue_{len(issues)+1}",
                            "sheet": ws.title,
                            "row": r,
                            "col": 3,
                            "col_name": lang_name,
                            "lang": lang,
                            "zh": str(zh_val),
                            "cur_trans": "",
                            "issue_type": "EMPTY",
                            "issue_desc": f"【{lang_name}】未翻译，单元格为空",
                            "suggested_fix": zh_val if lang == "tc" else ""
                        })

                matched_all += sheet_matched
                stats["sheets"].append({"name": ws.title, "rows": sheet_rows, "matched": sheet_matched})

            stats["total_rows"] = total_all
            stats["matched_rows"] = matched_all
            stats["filled_rows"] = matched_all

        wb.save(out_path)
        wb.close()

        stats["issue_count"] = len(issues)
        return {
            "stats": stats,
            "issues": issues,
            "output_path": out_path,
            "download_filename": out_fname
        }

    def _check_cell_issue(self, zh, trans, lang, sheet, row, col, col_name):
        if not trans:
            return {
                "id": f"issue_{sheet}_{row}_{col}",
                "sheet": sheet,
                "row": row,
                "col": col,
                "col_name": col_name,
                "lang": lang,
                "zh": str(zh),
                "cur_trans": "",
                "issue_type": "EMPTY",
                "issue_desc": f"未翻译，单元格为空",
                "suggested_fix": str(zh) if lang == "tc" else ""
            }

        zh_str = str(zh)
        tr_str = str(trans)

        # 0. 占位符与变量检查（例如 [fighterName:1]）
        for m in re.finditer(r'\[([a-zA-Z0-9_:]+)\]', zh_str):
            token = m.group(0)
            if token not in tr_str:
                return {
                    "id": f"issue_{sheet}_{row}_{col}",
                    "sheet": sheet,
                    "row": row,
                    "col": col,
                    "col_name": col_name,
                    "lang": lang,
                    "zh": zh_str,
                    "cur_trans": tr_str,
                    "issue_type": "TOKEN_MISMATCH",
                    "issue_desc": f"代码占位符 '{token}' 缺失或被篡改",
                    "suggested_fix": fix_placeholders(zh_str, tr_str)
                }

        # 1. 英文/印尼语中残留中文字符检查
        if lang in ["en", "id"]:
            cleaned_tr = re.sub(r"[【】《》（）·×～……——“”\s\d\w\.,!?:;'\"\-_/\\#<>=+%&*]+", "", tr_str)
            chinese_chars = re.findall(r"[\u4e00-\u9fa5]", cleaned_tr)
            if chinese_chars:
                sample_chars = "".join(chinese_chars[:8])
                fixed = align_text_symbols(zh_str, tr_str, lang)
                return {
                    "id": f"issue_{sheet}_{row}_{col}",
                    "sheet": sheet,
                    "row": row,
                    "col": col,
                    "col_name": col_name,
                    "lang": lang,
                    "zh": zh_str,
                    "cur_trans": tr_str,
                    "issue_type": "LEFTOVER_CHINESE",
                    "issue_desc": f"外语译文中混入中文字符: '{sample_chars}'",
                    "suggested_fix": fixed
                }

        # 2. 编号符号检查：1、 vs 1. (避免误判 1.8% 等浮点百分比)
        for i in range(1, 10):
            if f"{i}、" in zh_str and re.search(rf'(?:^|[\r\n\s]){i}\.(?!\d)', tr_str):
                fixed = align_text_symbols(zh_str, tr_str, lang)
                return {
                    "id": f"issue_{sheet}_{row}_{col}",
                    "sheet": sheet,
                    "row": row,
                    "col": col,
                    "col_name": col_name,
                    "lang": lang,
                    "zh": zh_str,
                    "cur_trans": tr_str,
                    "issue_type": "NUMBERING_MISMATCH",
                    "issue_desc": f"编号未按项目规范使用顿号 ({i}、)",
                    "suggested_fix": fixed
                }

        # 3. 特殊括号检查：【】 vs []
        if ("【" in zh_str and "】" in zh_str) and ("[" in tr_str and "]" in tr_str) and ("【" not in tr_str):
            fixed = align_text_symbols(zh_str, tr_str, lang)
            return {
                "id": f"issue_{sheet}_{row}_{col}",
                "sheet": sheet,
                "row": row,
                "col": col,
                "col_name": col_name,
                "lang": lang,
                "zh": zh_str,
                "cur_trans": tr_str,
                "issue_type": "BRACKET_MISMATCH",
                "issue_desc": f"括号符号未按原文保持【】",
                "suggested_fix": fixed
            }

        # 4. 颜色标签异常空格检查
        if '< /color>' in tr_str or '</ color>' in tr_str or '< /warna>' in tr_str or re.search(r'<color(?:\s+=\s*|=\s+|=[^>]*#\s+)', tr_str):
            return {
                "id": f"issue_{sheet}_{row}_{col}",
                "sheet": sheet,
                "row": row,
                "col": col,
                "col_name": col_name,
                "lang": lang,
                "zh": zh_str,
                "cur_trans": tr_str,
                "issue_type": "TAG_MALFORMED",
                "issue_desc": "颜色标签中含有多余空格或错误拼写",
                "suggested_fix": clean_tag_spaces_and_typos(tr_str)
            }

        # 5. 颜色标签数量检查
        zh_colors = len(re.findall(r'<color=[^>]+>', zh_str))
        tr_colors = len(re.findall(r'<color=[^>]+>', tr_str))
        if zh_colors != tr_colors:
            # 优先从已修正的高保真记忆库中提取完美对齐译文
            suggested = self.memory.query(zh_str, None, lang) or align_text_symbols(zh_str, tr_str, lang)
            return {
                "id": f"issue_{sheet}_{row}_{col}",
                "sheet": sheet,
                "row": row,
                "col": col,
                "col_name": col_name,
                "lang": lang,
                "zh": zh_str,
                "cur_trans": tr_str,
                "issue_type": "TAG_MISMATCH",
                "issue_desc": f"颜色标签数量不符 (原文 {zh_colors} 个, 译文 {tr_colors} 个)",
                "suggested_fix": suggested
            }

        # 6. 占位符匹配检查：%s
        zh_pct = zh_str.count("%s")
        tr_pct = tr_str.count("%s")
        if zh_pct != tr_pct:
            suggested = fix_placeholders(zh_str, tr_str)
            return {
                "id": f"issue_{sheet}_{row}_{col}",
                "sheet": sheet,
                "row": row,
                "col": col,
                "col_name": col_name,
                "lang": lang,
                "zh": zh_str,
                "cur_trans": tr_str,
                "issue_type": "PLACEHOLDER_MISMATCH",
                "issue_desc": f"占位符 %s 数量不符 (原文 {zh_pct} 个, 译文 {tr_pct} 个)",
                "suggested_fix": suggested
            }

        return None

    def execute_auto_fix(self, file_path, manual_fixes=None):
        wb = openpyxl.load_workbook(file_path)
        fixes_applied = 0

        if manual_fixes and isinstance(manual_fixes, list):
            for fix in manual_fixes:
                sheet_name = fix.get("sheet")
                row_idx = int(fix.get("row", 0))
                col_idx = int(fix.get("col", 0))
                new_val = fix.get("value")
                zh_val = fix.get("zh")
                lang = fix.get("lang") or ("en" if "英" in sheet_name else ("tc" if "繁" in sheet_name else "id"))

                if sheet_name in wb.sheetnames and row_idx > 0 and col_idx > 0 and new_val is not None:
                    ws = wb[sheet_name]
                    final_val = align_text_symbols(zh_val or "", new_val, lang)
                    ws.cell(row=row_idx, column=col_idx, value=final_val)
                    fixes_applied += 1

                    if zh_val and lang:
                        self.memory.set_term(zh_val, final_val, lang)

        for sname in wb.sheetnames:
            ws = wb[sname]
            is_pic = len(wb.sheetnames) == 1 and ws.max_column >= 5

            for r in range(2, ws.max_row + 1):
                zh_val = ws.cell(row=r, column=2).value
                if not zh_val:
                    continue

                if is_pic:
                    for c, l in [(3, "tc"), (4, "en"), (5, "id")]:
                        cur = ws.cell(row=r, column=c).value
                        if cur:
                            fixed = align_text_symbols(zh_val, str(cur), l)
                            if fixed != cur:
                                ws.cell(row=r, column=c, value=fixed)
                                fixes_applied += 1
                        else:
                            trans = self.memory.query(zh_val, None, l)
                            if trans:
                                ws.cell(row=r, column=c, value=align_text_symbols(zh_val, trans, l))
                                fixes_applied += 1
                else:
                    cur = ws.cell(row=r, column=3).value
                    lang_code = "en" if "英" in sname else ("tc" if "繁" in sname else "id")
                    if cur:
                        fixed = align_text_symbols(zh_val, str(cur), lang_code)
                        if fixed != cur:
                            ws.cell(row=r, column=3, value=fixed)
                            fixes_applied += 1
                    else:
                        trans = self.memory.query(zh_val, ws.cell(row=r, column=4).value, lang_code)
                        if trans:
                            ws.cell(row=r, column=3, value=align_text_symbols(zh_val, trans, lang_code))
                            fixes_applied += 1

        wb.save(file_path)
        wb.close()

        self.memory.save_incremental()

        try:
            root_out = "已完成翻译_需要翻译的文本.xlsx"
            if "需要翻译的文本" in file_path and os.path.exists(root_out):
                shutil.copy2(file_path, root_out)
        except Exception:
            pass

        return {
            "success": True,
            "fixes_applied": fixes_applied,
            "message": f"成功执行一键修复！共对齐并纠错 {fixes_applied} 处。"
        }


class ProjectManager:
    """
    多项目完全隔离管理器
    每个项目拥有独立的项目配置、记忆库(memory_db)、上传区(uploads)及成果区(outputs)
    支持项目动态切换与新增，彻底杜绝多项目互相污染
    """
    def __init__(self, workbench_dir):
        self.workbench_dir = workbench_dir
        self.projects_dir = os.path.join(self.workbench_dir, "projects")
        os.makedirs(self.projects_dir, exist_ok=True)
        self._stores = {}
        self._engines = {}
        self.ensure_default_project()

    def ensure_default_project(self):
        wuji_dir = os.path.join(self.projects_dir, "wuji")
        wuji_mem = os.path.join(wuji_dir, "memory_db")
        wuji_up = os.path.join(wuji_dir, "uploads")
        wuji_out = os.path.join(wuji_dir, "outputs")
        wuji_meta_file = os.path.join(wuji_dir, "project.json")

        for d in [wuji_dir, wuji_mem, wuji_up, wuji_out]:
            os.makedirs(d, exist_ok=True)

        if not os.path.exists(wuji_meta_file):
            proj_data = {
                "id": "wuji",
                "name": "无极仙途国际化翻译",
                "desc": "无极仙途游戏官方多语言出海翻译与本地化",
                "icon": "仙",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            with open(wuji_meta_file, "w", encoding="utf-8") as f:
                json.dump(proj_data, f, ensure_ascii=False, indent=2)

        # 检查是否需要从 legacy memory_db 迁移数据
        legacy_mem = os.path.join(self.workbench_dir, "memory_db")
        if os.path.exists(legacy_mem):
            for item in os.listdir(legacy_mem):
                src = os.path.join(legacy_mem, item)
                dst = os.path.join(wuji_mem, item)
                if os.path.isfile(src) and not os.path.exists(dst):
                    shutil.copy2(src, dst)

    def list_projects(self):
        projects = []
        if not os.path.exists(self.projects_dir):
            return projects

        for pid in sorted(os.listdir(self.projects_dir)):
            pdir = os.path.join(self.projects_dir, pid)
            if not os.path.isdir(pdir):
                continue
            meta_file = os.path.join(pdir, "project.json")
            if os.path.exists(meta_file):
                try:
                    with open(meta_file, "r", encoding="utf-8") as f:
                        pinfo = json.load(f)
                except Exception:
                    pinfo = {"id": pid, "name": pid, "icon": pid[:1].upper(), "desc": ""}
            else:
                pinfo = {"id": pid, "name": pid, "icon": pid[:1].upper(), "desc": ""}

            # 统计词条总数
            store, _ = self.get_project(pid)
            stats = store.get_stats()
            total_terms = sum(stats[k]["count"] for k in ["tc", "en", "id", "incremental"])
            pinfo["total_terms"] = total_terms
            projects.append(pinfo)

        return projects

    def create_project(self, name, desc="", icon=""):
        name_clean = clean_str(name)
        if not name_clean:
            raise ValueError("项目名称不能为空！")

        pid = f"proj_{int(time.time())}"
        pdir = os.path.join(self.projects_dir, pid)
        os.makedirs(os.path.join(pdir, "memory_db"), exist_ok=True)
        os.makedirs(os.path.join(pdir, "uploads"), exist_ok=True)
        os.makedirs(os.path.join(pdir, "outputs"), exist_ok=True)

        chosen_icon = icon.strip()[:1] if icon else name_clean[:1]
        pinfo = {
            "id": pid,
            "name": name_clean,
            "desc": desc.strip(),
            "icon": chosen_icon,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        with open(os.path.join(pdir, "project.json"), "w", encoding="utf-8") as f:
            json.dump(pinfo, f, ensure_ascii=False, indent=2)

        return pinfo

    def get_project(self, project_id="wuji"):
        pid = project_id or "wuji"
        pdir = os.path.join(self.projects_dir, pid)
        if not os.path.exists(pdir):
            pid = "wuji"
            pdir = os.path.join(self.projects_dir, "wuji")

        if pid not in self._stores:
            mem_dir = os.path.join(pdir, "memory_db")
            out_dir = os.path.join(pdir, "outputs")
            store = MemoryStore(mem_dir)
            eng = TranslationEngine(store, out_dir)
            self._stores[pid] = store
            self._engines[pid] = eng

        return self._stores[pid], self._engines[pid]

    def get_project_dirs(self, project_id="wuji"):
        pid = project_id or "wuji"
        pdir = os.path.join(self.projects_dir, pid)
        if not os.path.exists(pdir):
            pid = "wuji"
            pdir = os.path.join(self.projects_dir, "wuji")

        return {
            "root": pdir,
            "memory_db": os.path.join(pdir, "memory_db"),
            "uploads": os.path.join(pdir, "uploads"),
            "outputs": os.path.join(pdir, "outputs")
        }

    def get_project_info(self, project_id="wuji"):
        pid = project_id or "wuji"
        pdir = os.path.join(self.projects_dir, pid)
        if not os.path.exists(pdir):
            pid = "wuji"
            pdir = os.path.join(self.projects_dir, "wuji")
        meta_file = os.path.join(pdir, "project.json")
        if os.path.exists(meta_file):
            try:
                with open(meta_file, "r", encoding="utf-8") as f:
                    pinfo = json.load(f)
            except Exception:
                pinfo = {"id": pid, "name": pid, "icon": pid[:1].upper(), "desc": ""}
        else:
            pinfo = {"id": pid, "name": pid, "icon": pid[:1].upper(), "desc": ""}
        store, _ = self.get_project(pid)
        stats = store.get_stats()
        pinfo["total_terms"] = sum(stats[k]["count"] for k in ["tc", "en", "id", "incremental"])
        pinfo["stats"] = stats
        return pinfo

    def delete_project(self, project_id):
        if project_id == "wuji":
            raise ValueError("系统默认核心项目【无极仙途国际化翻译】不允许删除！")
        pdir = os.path.join(self.projects_dir, project_id)
        if not os.path.exists(pdir):
            raise ValueError(f"项目 {project_id} 不存在！")
        shutil.rmtree(pdir, ignore_errors=True)
        if project_id in self._stores:
            del self._stores[project_id]
        if project_id in self._engines:
            del self._engines[project_id]
        return True
