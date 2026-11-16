# -*- coding: utf-8 -*-
import json
import re

chunk_path = r'F:\项目\无极国际版\chunk_2.json'
result_path = r'F:\项目\无极国际版\result_chunk_2.json'

with open(chunk_path, 'r', encoding='utf-8') as f:
    chunk_data = json.load(f)

with open(result_path, 'r', encoding='utf-8') as f:
    result_data = json.load(f)

print(f"Original keys count: {len(chunk_data)}")
print(f"Result keys count: {len(result_data)}")

assert len(chunk_data) == 115, "Chunk data must have 115 items"
assert len(result_data) == 115, "Result data must have 115 items"

errors = []

# Term check mappings
en_terms = {
    '修为': 'Attainment',
    '灵玉': 'Div.Jade',
    '双修': 'Dual-Cultivation',
    '真气': 'Qi',
    '身法': 'Agility',
    '灵兽': 'Pet',
    '道场守卫': 'Dojo Guard',
    '魔印': 'Demonic Seal',
    '仙帝': 'Deity Emperor',
    '天品': 'G.Heaven',
    '地品': 'G.Earth',
    '玄品': 'G.Mythic',
    '黄品': 'G.Novice',
    '功法': 'Technique',
    '法宝': 'Artifact',
    '羁绊': 'Bond',
    '图鉴': 'Codex'
}

id_terms = {
    '修为': 'Capaian',
    '灵玉': 'Batu Giok',
    '双修': 'Kultivasi Ganda',
    '真气': 'Qi',
    '身法': 'Kelincahan',
    '灵兽': 'Peliharaan',
    '道场守卫': 'Penjaga Dojo',
    '魔印': 'Segel Setan',
    '仙帝': 'Kaisar Dewa',
    '天品': 'G.Surga',
    '地品': 'G.Earth',
    '玄品': 'G.Mistik',
    '黄品': 'G.Pemula',
    '功法': 'Teknik',
    '法宝': 'Artefak',
    '羁绊': 'Ikatan',
    '图鉴': 'Kodeks'
}

for i, k in enumerate(chunk_data):
    if k not in result_data:
        errors.append(f"Missing key in result: {repr(k)}")
        continue
    
    val = result_data[k]
    for lang in ['tc', 'en', 'id']:
        if lang not in val:
            errors.append(f"Missing {lang} in key {i}: {repr(k)}")
            continue
        v = val[lang]
        if not v or not isinstance(v, str):
            errors.append(f"Empty or non-string {lang} in key {i}: {repr(k)}")
            continue

        # Placeholder check
        orig_ph = re.findall(r'%[0-9]*[a-zA-Z%]', k)
        val_ph = re.findall(r'%[0-9]*[a-zA-Z%]', v)
        if sorted(orig_ph) != sorted(val_ph):
            errors.append(f"[{lang}] Key {i} placeholder mismatch: orig={orig_ph}, trans={val_ph}")

        # Color tag check
        orig_col = re.findall(r'<color=#[0-9a-fA-F]{6}>', k)
        val_col = re.findall(r'<color=#[0-9a-fA-F]{6}>', v)
        if orig_col != val_col:
            errors.append(f"[{lang}] Key {i} color tag open mismatch: orig={orig_col}, trans={val_col}")
        
        orig_close = re.findall(r'</color>', k)
        val_close = re.findall(r'</color>', v)
        if len(orig_close) != len(val_close):
            errors.append(f"[{lang}] Key {i} color tag close mismatch: orig={len(orig_close)}, trans={len(val_close)}")

        # Literal \n check
        if k.count(r'\n') != v.count(r'\n'):
            errors.append(f"[{lang}] Key {i} literal \\n mismatch: orig={k.count(r'\\n')}, trans={v.count(r'\\n')}")

    # Terminology checks
    for zh, term in en_terms.items():
        if zh in k:
            if term.lower() not in val['en'].lower():
                errors.append(f"[EN Term] Key {i}: '{zh}' -> expected '{term}' in '{val['en']}'")

    for zh, term in id_terms.items():
        if zh in k:
            if term.lower() not in val['id'].lower():
                errors.append(f"[ID Term] Key {i}: '{zh}' -> expected '{term}' in '{val['id']}'")

if errors:
    print(f"Validation FAILED with {len(errors)} issues:")
    for err in errors:
        print(" ", err)
else:
    print("SUCCESS: All 115 items passed every single validation check!")
