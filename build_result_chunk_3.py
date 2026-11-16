# -*- coding: utf-8 -*-
import json
import re

with open('F:/项目/无极国际版/chunk_3.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Guard logic
realm_map = {
    '元婴': {'tc': '元嬰', 'en': 'Nascence', 'id': 'Nascence'},
    '分神': {'tc': '分神', 'en': 'Severance', 'id': 'Sengsara'},
    '合体': {'tc': '合體', 'en': 'Embodiment', 'id': 'Menjelma'},
    '炼虚': {'tc': '煉虛', 'en': 'Vainify', 'id': 'Merusak'},
    '大乘': {'tc': '大乘', 'en': 'Mahayana', 'id': 'Mahayana'},
    '游仙': {'tc': '遊仙', 'en': 'Wanderer', 'id': 'Tualang'},
    '真仙': {'tc': '真仙', 'en': 'Deity', 'id': 'Dewa'},
    '玄仙': {'tc': '玄仙', 'en': 'Mythic Deity', 'id': 'Dewa Mistikal'},
    '天仙': {'tc': '天仙', 'en': 'Heaven Deity', 'id': 'Dewa Surgawi'},
    '太乙玉仙': {'tc': '太乙玉仙', 'en': 'Taiyi', 'id': 'Taiyi'},
    '大罗金仙': {'tc': '大羅金仙', 'en': 'Daluo', 'id': 'Daluo'},
    '仙尊': {'tc': '仙尊', 'en': 'Deity Lord', 'id': 'Mahadewa Raja'},
    '仙帝': {'tc': '仙帝', 'en': 'Deity Emperor', 'id': 'Kaisar Dewa'}
}

stage_num_map = {
    '一阶': {'tc': '一階', 'en': 'G.1', 'id': 'G.1'},
    '二阶': {'tc': '二階', 'en': 'G.2', 'id': 'G.2'},
    '三阶': {'tc': '三階', 'en': 'G.3', 'id': 'G.3'},
    '四阶': {'tc': '四階', 'en': 'G.4', 'id': 'G.4'},
    '五阶': {'tc': '五階', 'en': 'G.5', 'id': 'G.5'},
    '六阶': {'tc': '六階', 'en': 'G.6', 'id': 'G.6'},
    '七阶': {'tc': '七階', 'en': 'G.7', 'id': 'G.7'},
    '八阶': {'tc': '八階', 'en': 'G.8', 'id': 'G.8'},
    '九阶': {'tc': '九階', 'en': 'G.9', 'id': 'G.9'},
    '十阶': {'tc': '十階', 'en': 'G.10', 'id': 'G.10'}
}

custom_dict = {
    # 0: 红枫妙法
    "红枫妙法": {
        "tc": "紅楓妙法",
        "en": "Red Maple Sutra",
        "id": "Sutra Maple Merah"
    },
    # 2: 伏暑
    "伏暑": {
        "tc": "伏暑",
        "en": "Summer Heat",
        "id": "Panas Terik"
    },
    # 3: 试剑天下礼包
    "试剑天下礼包": {
        "tc": "試劍天下禮包",
        "en": "Sword Trial Giftpack",
        "id": "Paket Hadiah Uji Pedang Dunia"
    },
    # 5: 诛仙阵和九州商会...
    "诛仙阵和九州商会<color=#9e4444>轮流开放</color>，时光秘境<color=#9e4444>每月1号</color>开启。地府判鬼，<color=#9e4444>每周二至周日</color>都会开启。四季福地，<color=#9e4444>每月1号</color>开启。\\n\\n<color=#0c5a8b>诛仙阵</color>：\\n1、1~2栏位<color=#9e4444>优先</color>放置辅助招式，剩余栏位可全部放输出招式。\\n2、诛、戮、陷和绝四偏阵打掉后，可以<color=#9e4444>降低</color>通天教主的属性，\\n3、为防止首领打完了，箱子没拿完，可以先把箱子拿了，再打首领。\\n\\n<color=#0c5a8b>诛仙阵小技巧</color>：\\n1、<color=#9e4444>戮仙门</color>推荐先把左上角和右下角的金箱子拿了，算是比较好拿的，10来个怪就行，之后看自己实力多拿点银箱子，或者直接出去\\n2、<color=#9e4444>陷仙门</color>出口下右上角，不追求很多箱子只要速通的话，最快通关路线，是从地图下面的格子走过去\\n3、<color=#9e4444>绝仙门</color>从左边数，入口位置是第1列，第3、6、10和15列的阵眼可以激活。\\n\\n<color=#0c5a8b>九州商会</color>：\\n<color=#9e4444>模拟经商玩法</color>，活动获取的<color=#9e4444>九州令</color>，可在<color=#9e4444>秘境商人</color>处兑换<color=#9e4444>仙玉、天阶招式礼包、精元丹</color>等珍稀资源。\\n\\n<color=#0c5a8b>时光秘境</color>：\\n<color=#9e4444>肉鸽玩法</color>，参与获取的<color=#9e4444>时光沙漏</color>，可在<color=#9e4444>秘境商人</color>处兑换<color=#9e4444>神火，高级、神级点化石</color>。\\n\\n<color=#0c5a8b>地府判鬼</color>：\\n<color=#9e4444>文字模拟的角色扮演玩法</color>。玩法核心奖励：<color=#9e4444>灵童修为丹</color>。\\n\\n<color=#0c5a8b>地府判鬼小技巧</color>：\\n<color=#0c5a8b>大善</color>→涉及到救人，因为救人牺牲等\\n<color=#0c5a8b>小善</color>→老年道歉，行侠仗义，帮助他人和流浪狗，清官等\\n<color=#0c5a8b>小恶</color>→不涉及性命的恶，如懒惰，偷抢，赌博，逃兵等\\n<color=#0c5a8b>大恶</color>→涉及到性命的恶，如自刀人（战场杀敌杀寇除外），被凌迟\\n\\n<color=#0c5a8b>四季福地</color>：\\n<color=#9e4444>宗门弟子玩法</color>，通过弟子完成<color=#9e4444>机缘任务</color>和击败<color=#9e4444>入侵凶兽</color>、<color=#9e4444>洞窟魔物</color>获得物品和福玉奖励，福玉可在<color=#9e4444>福地商店</color>中兑换珍惜资源\\n\\n": {
        "tc": "誅仙陣和九州商會<color=#9e4444>輪流開放</color>，時光秘境<color=#9e4444>每月1號</color>開啟。地府判鬼，<color=#9e4444>每週二至週日</color>都會開啟。四季福地，<color=#9e4444>每月1號</color>開啟。\\n\\n<color=#0c5a8b>誅仙陣</color>：\\n1、1~2欄位<color=#9e4444>優先</color>放置輔助招式，剩餘欄位可全部放輸出招式。\\n2、誅、戮、陷和絕四偏陣打掉後，可以<color=#9e4444>降低</color>通天教主的屬性，\\n3、為防止首領打完了，箱子沒拿完，可以先把箱子拿了，再打首領。\\n\\n<color=#0c5a8b>誅仙陣小技巧</color>：\\n1、<color=#9e4444>戮仙門</color>推薦先把左上角和右下角的金箱子拿了，算是比較好拿的，10來個怪就行，之後看自己實力多拿點銀箱子，或者直接出去\\n2、<color=#9e4444>陷仙門</color>出口下右上角，不追求很多箱子只要速通的話，最快通關路線，是從地圖下面的格子走過去\\n3、<color=#9e4444>絕仙門</color>從左邊數，入口位置是第1列，第3、6、10和15列的陣眼可以激活。\\n\\n<color=#0c5a8b>九州商會</color>：\\n<color=#9e4444>模擬經商玩法</color>，活動獲取的<color=#9e4444>九州令</color>，可在<color=#9e4444>秘境商人</color>處兌換<color=#9e4444>仙玉、天階招式禮包、精元丹</color>等珍稀資源。\\n\\n<color=#0c5a8b>時光秘境</color>：\\n<color=#9e4444>肉鴿玩法</color>，參與獲取的<color=#9e4444>時光沙漏</color>，可在<color=#9e4444>秘境商人</color>處兌換<color=#9e4444>神火，高級、神級點化石</color>。\\n\\n<color=#0c5a8b>地府判鬼</color>：\\n<color=#9e4444>文字模擬的角色扮演玩法</color>。玩法核心獎勵：<color=#9e4444>靈童修為丹</color>。\\n\\n<color=#0c5a8b>地府判鬼小技巧</color>：\\n<color=#0c5a8b>大善</color>→涉及到救人，因為救人犧牲等\\n<color=#0c5a8b>小善</color>→老年道歉，行俠仗義，幫助他人和流浪狗，清官等\\n<color=#0c5a8b>小惡</color>→不涉及性命的惡，如懶惰，偷搶，賭博，逃兵等\\n<color=#0c5a8b>大惡</color>→涉及到性命的惡，如自刀人（戰場殺敵殺寇除外），被凌遲\\n\\n<color=#0c5a8b>四季福地</color>：\\n<color=#9e4444>宗門弟子玩法</color>，通過弟子完成<color=#9e4444>機緣任務</color>和擊敗<color=#9e4444>入侵兇獸</color>、<color=#9e4444>洞窟魔物</color>獲得物品和福玉獎勵，福玉可在<color=#9e4444>福地商店</color>中兌換珍惜資源\\n\\n",
        "en": "Deity Slain Array and Jiuzhou Commerce Chamber are <color=#9e4444>open in rotation</color>, and Times Realm opens <color=#9e4444>on the 1st of each month</color>. Nether Judge opens <color=#9e4444>every Tuesday to Sunday</color>. Seasonal Domain opens <color=#9e4444>on the 1st of each month</color>.\\n\\n<color=#0c5a8b>Deity Slain Array</color>:\\n1. Slots 1-2 <color=#9e4444>prioritize</color> placing support skills, while the remaining slots can all be filled with damage skills.\\n2. Defeating the four sub-arrays of Zhu, Lu, Xian, and Jue can <color=#9e4444>reduce</color> the attributes of Sky Bishop.\\n3. To prevent defeating the boss before collecting all chests, you can collect chests first before fighting the boss.\\n\\n<color=#0c5a8b>Deity Slain Array Tips</color>:\\n1. At <color=#9e4444>Slaying Way</color>, it is recommended to get the gold chests at the upper-left and lower-right corners first, which are relatively easy to get with around 10 monsters. Afterward, collect more silver chests according to your strength, or exit directly.\\n2. At <color=#9e4444>Trapping Way</color>, the exit is at the upper-right corner. If not pursuing many chests and only aiming for speedrun, the fastest route is walking through the grid below the map.\\n3. At <color=#9e4444>Striking Way</color>, counting from the left, the entrance is at column 1; array cores in columns 3, 6, 10, and 15 can be activated.\\n\\n<color=#0c5a8b>Jiuzhou Commerce Chamber</color>:\\n<color=#9e4444>Business simulation gameplay</color>. The <color=#9e4444>Jiuzhou Tokens</color> obtained from events can be exchanged at the <color=#9e4444>Realm Merchant</color> for rare resources such as <color=#9e4444>Jade, G.Heaven Skill Giftpacks, Pure Quiddity Orbs</color>, etc.\\n\\n<color=#0c5a8b>Times Realm</color>:\\n<color=#9e4444>Roguelike gameplay</color>. The <color=#9e4444>Hourglass of Time</color> obtained can be exchanged at the <color=#9e4444>Realm Merchant</color> for <color=#9e4444>Divine Fire, Adv. and Divine Enlightenment Stones</color>.\\n\\n<color=#0c5a8b>Nether Judge</color>:\\n<color=#9e4444>Text-based role-playing gameplay</color>. Core reward: <color=#9e4444>Spiritual Child Attainment Orb</color>.\\n\\n<color=#0c5a8b>Nether Judge Tips</color>:\\n<color=#0c5a8b>Great Good</color>→ Involves saving lives, sacrificing oneself for others, etc.\\n<color=#0c5a8b>Minor Good</color>→ Apologizing in old age, knightly deeds, helping others and stray dogs, honest officials, etc.\\n<color=#0c5a8b>Minor Evil</color>→ Evils not involving lives, such as laziness, theft, gambling, desertion, etc.\\n<color=#0c5a8b>Great Evil</color>→ Evils involving lives, such as suicide/murder (except slaying enemies on the battlefield), death by lingering slicing\\n\\n<color=#0c5a8b>Seasonal Domain</color>:\\n<color=#9e4444>Sect Disciple gameplay</color>. Send disciples to complete <color=#9e4444>Chance Quests</color> and defeat <color=#9e4444>Invading Fierce Beasts</color> and <color=#9e4444>Cave Monsters</color> to obtain items and Blessed Jade rewards. Blessed Jade can be exchanged for rare resources in the <color=#9e4444>Domain Shop</color>\\n\\n",
        "id": "Array Pengutuk Dewa dan Kamar Dagang Jiuzhou <color=#9e4444>dibuka bergantian</color>, Alam Alam Lain dibuka <color=#9e4444>pada tanggal 1 setiap bulan</color>. Hakim Nether dibuka <color=#9e4444>setiap hari Selasa hingga Minggu</color>. Domain Musiman dibuka <color=#9e4444>pada tanggal 1 setiap bulan</color>.\\n\\n<color=#0c5a8b>Array Pengutuk Dewa</color>:\\n1. Slot 1-2 <color=#9e4444>diprioritaskan</color> untuk jurus pendukung, slot tersisa dapat diisi dengan jurus penyerang.\\n2. Mengalahkan empat sub-array Zhu, Lu, Xian, dan Jue dapat <color=#9e4444>menurunkan</color> atribut Uskup Langit.\\n3. Untuk mencegah peti tertinggal setelah mengalahkan boss, Anda dapat mengambil peti terlebih dahulu sebelum melawan boss.\\n\\n<color=#0c5a8b>Tips Array Pengutuk Dewa</color>:\\n1. Di <color=#9e4444>Cara yang Membunuh</color>, disarankan mengambil peti emas di pojok kiri atas dan kanan bawah terlebih dahulu, relatif mudah didapat dengan sekitar 10 monster, lalu ambil lebih banyak peti perak sesuai kemampuan, atau langsung keluar.\\n2. Pintu keluar <color=#9e4444>Cara yang Menjebak</color> berada di kanan atas. Jika tidak mengejar banyak peti dan ingin cepat selesai, rute tercepat adalah berjalan melalui petak di bagian bawah peta.\\n3. Di <color=#9e4444>Cara Menyerang</color>, dihitung dari kiri, pintu masuk berada di kolom ke-1; mata formasi di kolom ke-3, 6, 10, dan 15 dapat diaktifkan.\\n\\n<color=#0c5a8b>Kamar Dagang Jiuzhou</color>:\\n<color=#9e4444>Gameplay simulasi bisnis</color>. <color=#9e4444>Token Jiuzhou</color> yang diperoleh dari event dapat ditukarkan di <color=#9e4444>Pedagang Alam</color> untuk sumber daya langka seperti <color=#9e4444>Batu Giok, Paket Hadiah Skill G.Surga, Orb Quiddity Murni</color>, dll.\\n\\n<color=#0c5a8b>Alam Alam Lain</color>:\\n<color=#9e4444>Gameplay Roguelike</color>. <color=#9e4444>Jam Pasir Waktu</color> yang diperoleh dari partisipasi dapat ditukarkan di <color=#9e4444>Pedagang Alam</color> untuk <color=#9e4444>Api Ilahi, Batu Pencerahan Tingkat Lanjut & Tingkat Ilahi</color>.\\n\\n<color=#0c5a8b>Hakim Nether</color>:\\n<color=#9e4444>Gameplay RPG simulasi teks</color>. Hadiah utama gameplay: <color=#9e4444>Orb Capaian Anak Roh</color>.\\n\\n<color=#0c5a8b>Tips Hakim Nether</color>:\\n<color=#0c5a8b>Kebaikan Besar</color>→ Berkaitan dengan menyelamatkan nyawa, berkorban demi orang lain, dll.\\n<color=#0c5a8b>Kebaikan Kecil</color>→ Meminta maaf di hari tua, membela kebenaran, menolong orang lain dan anjing liar, pejabat jujur, dll.\\n<color=#0c5a8b>Kejahatan Kecil</color>→ Kejahatan yang tidak melibatkan nyawa, seperti malas, mencuri/merampok, berjudi, desersi, dll.\\n<color=#0c5a8b>Kejahatan Besar</color>→ Kejahatan yang melibatkan nyawa, seperti bunuh diri/pembunuhan (kecuali membunuh musuh di medan perang), dieksekusi potong perlahan\\n\\n<color=#0c5a8b>Domain Musiman</color>:\\n<color=#9e4444>Gameplay Murid Sekte</color>. Melalui murid yang menyelesaikan <color=#9e4444>Misi Peluang</color> serta mengalahkan <color=#9e4444>Binatang Buas Penyerbu</color> dan <color=#9e4444>Monster Gua</color> untuk memperoleh item dan hadiah Giok Berkah. Giok Berkah dapat ditukarkan dengan sumber daya langka di <color=#9e4444>Toko Domain Berkah</color>\\n\\n"
    },
    # 6: 使用后习得灵级凝土神丹的炼制之法...
    "使用后习得灵级凝土神丹的炼制之法。（天品炼丹师方可使用）\\n凝土神丹服用后提升真气和土系伤害。": {
        "tc": "使用後習得靈級凝土神丹的煉製之法。（天品煉丹師方可使用）\\n凝土神丹服用後提升真氣和土系傷害。",
        "en": "Use to learn how to refine Spirit Grade Soil Consolidation Divine Orb. (Usable by G.Heaven Alchemist)\\nSoil Consolidation Divine Orb increases Qi and Earth DMG when taken.",
        "id": "Gunakan untuk mempelajari metode pemurnian Orb Dewa Pemadat Tanah Tingkat Roh. (Dapat digunakan oleh G.Surga Alkimis)\\nMengonsumsi Orb Dewa Pemadat Tanah meningkatkan Qi dan DMG Bumi."
    },
    # 7: 论道大会赛季奖励
    "论道大会赛季奖励": {
        "tc": "論道大會賽季獎勵",
        "en": "Theory Assembly Season Rewards",
        "id": "Hadiah Musim Pertemuan Teori"
    },
    # 8: 灵兽十五
    "灵兽十五": {
        "tc": "靈獸十五",
        "en": "Pet 15",
        "id": "Peliharaan 15"
    },
    # 9: 收集[红叶信笺]
    "收集[红叶信笺]": {
        "tc": "收集[紅葉信箋]",
        "en": "Collect [Hong Ye's Letter]",
        "id": "Kumpulkan [Surat Hong Ye]"
    },
    # 10: 服用后凝练修士修为...
    "服用后凝练修士修为，增加210体魄、700点金系伤害。（最多服用80个）": {
        "tc": "服用後凝練修士修為，增加210體魄、700點金系傷害。（最多服用80個）",
        "en": "Condenses cultivator's Attainment after taken, increasing Health by 210 and Metal DMG by 700. (Can take up to 80)",
        "id": "Mengonsumsi ini memadatkan Capaian kultivator, meningkatkan 210 Kesehatan dan 700 DMG Logam. (Dapat digunakan hingga 80)"
    },
    # 11: 收集[叶凝烟信笺]
    "收集[叶凝烟信笺]": {
        "tc": "收集[葉凝煙信箋]",
        "en": "Collect [Ye Ningyan's Letter]",
        "id": "Kumpulkan [Surat Ye Ningyan]"
    },
    # 12: 当前秘宝未解锁
    "当前秘宝未解锁": {
        "tc": "當前秘寶未解鎖",
        "en": "Current Secret Treasure is locked",
        "id": "Harta Karun Rahasia saat ini belum dibuka"
    },
    # 13: 收集[严诗雨信笺]
    "收集[严诗雨信笺]": {
        "tc": "收集[嚴詩雨信箋]",
        "en": "Collect [Yan Shiyu's Letter]",
        "id": "Kumpulkan [Surat Yan Shiyu]"
    },
    # 14: 收集[明河信笺]
    "收集[明河信笺]": {
        "tc": "收集[明河信箋]",
        "en": "Collect [Minghe's Letter]",
        "id": "Kumpulkan [Surat Minghe]"
    },
    # 15: 灵级御水神丹方
    "灵级御水神丹方": {
        "tc": "靈級御水神丹方",
        "en": "Spirit Grade Water Ward Divine Orb Recipe",
        "id": "Resep Orb Dewa Pengendali Air Tingkat Roh"
    },
    # 16: 神秘灵兽蛋-秋
    "神秘灵兽蛋-秋": {
        "tc": "神秘靈獸蛋-秋",
        "en": "Mysterious Pet Egg - Autumn",
        "id": "Telur Peliharaan Misterius - Musim Gugur"
    },
    # 17: 悲秋
    "悲秋": {
        "tc": "悲秋",
        "en": "Autumn Grief",
        "id": "Duka Musim Gugur"
    },
    # 19: 不知何时被封存的珍宝...
    "不知何时被封存的珍宝，已经化为了灵珀一样的矿石，小心打开后90%概率获得随机1至3个珍宝碎片，10%概率随机获得1个完整的珍宝。": {
        "tc": "不知何時被封存的珍寶，已經化為了靈珀一樣的礦石，小心打開後90%概率獲得隨機1至3個珍寶碎片，10%概率隨機獲得1個完整的珍寶。",
        "en": "A sealed treasure from unknown times, turned into ore like spirit amber. Carefully open it to have a 90% chance to randomly obtain 1-3 Treasure Shards, and a 10% chance to randomly obtain 1 complete Treasure.",
        "id": "Harta karun yang disegel sejak waktu yang tidak diketahui, telah berubah menjadi bijih seperti ambar roh. Buka dengan hati-hati untuk peluang 90% mendapatkan 1-3 Pecahan Harta secara acak, dan peluang 10% mendapatkan 1 Harta lengkap secara acak."
    },
    # 21: 受到伤害后，恢复五行伤害总值%s生命值，持续6回合
    "受到伤害后，恢复五行伤害总值%s生命值，持续6回合": {
        "tc": "受到傷害後，恢復五行傷害總值%s生命值，持續6回合",
        "en": "After taking DMG, restores HP equal to %s of total 5-Element DMG, lasting 6 rounds",
        "id": "Setelah menerima DMG, pulihkan HP sebesar %s dari total DMG 5-Elemen, berlangsung selama 6 ronde"
    },
    # 22: 灵级破浪神丹
    "灵级破浪神丹": {
        "tc": "靈級破浪神丹",
        "en": "Spirit Grade Wave Breaking Divine Orb",
        "id": "Orb Dewa Pemecah Gelombang Tingkat Roh"
    },
    # 23: 剑仙伴侣
    "剑仙伴侣": {
        "tc": "劍仙伴侶",
        "en": "Sword Immortal Companion",
        "id": "Pendamping Pendekar Pedang Abadi"
    },
    # 24: 衣香鬓影
    "衣香鬓影": {
        "tc": "衣香鬢影",
        "en": "Silken Elegance",
        "id": "Keanggunan Sutra"
    },
    # 25: 蕙心纨质
    "蕙心纨质": {
        "tc": "蕙心紈質",
        "en": "Pure Heart and Elegance",
        "id": "Hati Murni dan Anggun"
    },
    # 26: 绿肥红瘦
    "绿肥红瘦": {
        "tc": "綠肥紅瘦",
        "en": "Lush Greens and Fading Reds",
        "id": "Daun Rimbun Bunga Memudar"
    },
    # 27: 修行界顶级功法需要<color=#458114>太乙玉仙</color>方可参悟\n效果：<color=#458114>攻击增强</color>
    "修行界顶级功法需要<color=#458114>太乙玉仙</color>方可参悟\\n效果：<color=#458114>攻击增强</color>": {
        "tc": "修行界頂級功法需要<color=#458114>太乙玉仙</color>方可參悟\\n效果：<color=#458114>攻擊增強</color>",
        "en": "Cultivation world's top Technique requires <color=#458114>Taiyi</color> to comprehend\\nEffect: <color=#458114>ATK Increased</color>",
        "id": "Teknik tingkat atas dunia kultivasi membutuhkan <color=#458114>Taiyi</color> untuk dipahami\\nEfek: <color=#458114>ATK Meningkat</color>"
    },
    # 28: 抽取后无法改变奖池
    "抽取后无法改变奖池": {
        "tc": "抽取後無法改變獎池",
        "en": "Prize pool cannot be changed after drawing",
        "id": "Kumpulan hadiah tidak dapat diubah setelah undian"
    },
    # 29: 使用后可获得随机灵兽材料...
    "使用后可获得随机灵兽材料。\\n包含：灵兽口粮、月华灵草、莲华仙草、真灵心血、兽灵金丹、灵兽仙丹、灵兽真丹、灵兽骨丹、灵兽玄丹、灵兽幻丹、灵兽圣丹": {
        "tc": "使用後可獲得隨機靈獸材料。\\n包含：靈獸口糧、月華靈草、蓮華仙草、真靈心血、獸靈金丹、靈獸仙丹、靈獸真丹、靈獸骨丹、靈獸玄丹、靈獸幻丹、靈獸聖丹",
        "en": "Use to obtain random Pet materials.\\nIncludes: Pet Food, Lunar Herb, Lotus Grass, Spirit Blood, Spirit Golden Orb, Pet Deity Orb, Pet Orb, Pet Strength Orb, Pet Mythic Orb, Pet Magical Orb, Pet Sage Orb",
        "id": "Gunakan untuk mendapatkan material Peliharaan acak.\\nTermasuk: Makanan Peliharaan, Ramuan Bulan, Rumput Teratai, Darah Roh, Orb Golden Roh, Orb Dewa Peliharaan, Orb Peliharaan, Orb Kekuatan Peliharaan, Orb Mistik Peliharaan, Orb Sakti Peliharaan, Orb Sage Peliharaan"
    },
    # 30: 排名奖励每个赛季结算一次，以邮件形式发放
    "排名奖励每个赛季结算一次，以邮件形式发放": {
        "tc": "排名獎勵每個賽季結算一次，以郵件形式發放",
        "en": "Rank rewards are settled once per season and sent via mail",
        "id": "Hadiah peringkat diselesaikan sekali per musim dan dikirimkan melalui surat"
    },
    # 31: 洞窟魔物·戮
    "洞窟魔物·戮": {
        "tc": "洞窟魔物·戮",
        "en": "Cave Monster · Slaughter",
        "id": "Monster Gua · Pembantai"
    },
    # 32: 凶兽礼盒-春
    "凶兽礼盒-春": {
        "tc": "兇獸禮盒-春",
        "en": "Fierce Beast Gift Box - Spring",
        "id": "Kotak Hadiah Binatang Buas - Musim Semi"
    },
    # 33: 灵级地心神丹方
    "灵级地心神丹方": {
        "tc": "靈級地心神丹方",
        "en": "Spirit Grade Earth Core Divine Orb Recipe",
        "id": "Resep Orb Dewa Inti Bumi Tingkat Roh"
    },
    # 35: 残冬心法
    "残冬心法": {
        "tc": "殘冬心法",
        "en": "Waning Winter Mental Sutra",
        "id": "Sutra Batin Akhir Musim Dingin"
    },
    # 36: 打开后，可从灵兽蛋·魔蛟、灵兽蛋·凤凰和灵兽蛋·白虎中随机获得一个
    "打开后，可从灵兽蛋·魔蛟、灵兽蛋·凤凰和灵兽蛋·白虎中随机获得一个": {
        "tc": "打開後，可從靈獸蛋·魔蛟、靈獸蛋·鳳凰和靈獸蛋·白虎中隨機獲得一個",
        "en": "Open to randomly obtain one from Pet Egg · Sea Demon, Pet Egg · Phoenix, and Pet Egg · Byako",
        "id": "Buka untuk mendapatkan secara acak salah satu dari Telur Peliharaan · Setan Laut, Telur Peliharaan · Phoenix, dan Telur Peliharaan · Byako"
    },
    # 37: 四季福地-凶兽-秋
    "四季福地-凶兽-秋": {
        "tc": "四季福地-兇獸-秋",
        "en": "Seasonal Domain - Fierce Beast - Autumn",
        "id": "Domain Musiman - Binatang Buas - Musim Gugur"
    },
    # 39: 使用后将“鹤舞丹青”法相加入衣阁。
    "使用后将“鹤舞丹青”法相加入衣阁。": {
        "tc": "使用後將“鶴舞丹青”法相加入衣閣。",
        "en": "Use to add \"Crane Dance on Ink\" Deity Form into Closet.",
        "id": "Gunakan untuk menambahkan Pendewaan \"Tarian Bangau dalam Lukisan\" ke dalam lemari."
    },
    # 40: 使用后可随机获得一本伏暑功法。
    "使用后可随机获得一本伏暑功法。": {
        "tc": "使用後可隨機獲得一本伏暑功法。",
        "en": "Use to randomly obtain a Summer Heat Technique book.",
        "id": "Gunakan untuk mendapatkan satu buku Teknik Panas Terik secara acak."
    },
    # 41: 收集[秦羽彤信笺]
    "收集[秦羽彤信笺]": {
        "tc": "收集[秦羽彤信箋]",
        "en": "Collect [Qin Yutong's Letter]",
        "id": "Kumpulkan [Surat Qin Yutong]"
    },
    # 42: 1、福地的凶兽每日刷新2只...
    "1、福地的凶兽每日刷新2只，第二次出现的凶兽会难度提高，奖励也更加丰厚\\n2、未击败的凶兽会在第二天刷新后移出\\n3、凶兽奖励类型会随着季度变化而变化": {
        "tc": "1、福地的兇獸每日刷新2隻，第二次出現的兇獸會難度提高，獎勵也更加豐厚\\n2、未擊敗的兇獸會在第二天刷新後移出\\n3、兇獸獎勵類型會隨著季度變化而變化",
        "en": "1. 2 Fierce Beasts in the Blessed Land are refreshed daily. The second Fierce Beast has increased difficulty and richer rewards\\n2. Undefeated Fierce Beasts will be removed after the next day's refresh\\n3. Fierce Beast reward types will change with the seasons",
        "id": "1. 2 Binatang Buas di Tanah Berkah diperbarui setiap hari. Binatang Buas kedua yang muncul memiliki tingkat kesulitan lebih tinggi dan hadiah lebih melimpah\\n2. Binatang Buas yang belum dikalahkan akan dipindahkan setelah pembaruan hari berikutnya\\n3. Jenis hadiah Binatang Buas akan berubah seiring pergantian musim"
    },
    # 43: 四绝剑法
    "四绝剑法": {
        "tc": "四絕劍法",
        "en": "Four Perfections Sword Technique",
        "id": "Teknik Pedang Empat Kesempurnaan"
    },
    # 44: 怪物已死\n有事烧纸
    "怪物已死\\n有事烧纸": {
        "tc": "怪物已死\\n有事燒紙",
        "en": "Monster is dead\\nBurn paper if needed",
        "id": "Monster sudah mati\\nBakar kertas jika perlu"
    },
    # 45: 天仙限时礼包
    "天仙限时礼包": {
        "tc": "天仙限時禮包",
        "en": "Heaven Deity Limited Giftpack",
        "id": "Paket Hadiah Terbatas Dewa Surgawi"
    },
    # 46: 玄仙限时礼包
    "玄仙限时礼包": {
        "tc": "玄仙限時禮包",
        "en": "Mythic Deity Limited Giftpack",
        "id": "Paket Hadiah Terbatas Dewa Mistikal"
    },
    # 47: 30元论道大会礼包
    "30元论道大会礼包": {
        "tc": "30元論道大會禮包",
        "en": "$30 Theory Assembly Giftpack",
        "id": "Paket Hadiah $30 Pertemuan Teori"
    },
    # 48: 福地灵运
    "福地灵运": {
        "tc": "福地靈運",
        "en": "Blessed Land Spirit Fortune",
        "id": "Keberuntungan Roh Tanah Berkah"
    },
    # 49: 凶兽礼盒-秋
    "凶兽礼盒-秋": {
        "tc": "兇獸禮盒-秋",
        "en": "Fierce Beast Gift Box - Autumn",
        "id": "Kotak Hadiah Binatang Buas - Musim Gugur"
    },
    # 51: 精英魔物·疗
    "精英魔物·疗": {
        "tc": "精英魔物·療",
        "en": "Elite Monster · Heal",
        "id": "Monster Elit · Pemulihan"
    },
    # 52: 使用后将“永结同心”称号加入衣阁。
    "使用后将“永结同心”称号加入衣阁。": {
        "tc": "使用後將“永結同心”稱號加入衣閣。",
        "en": "Use to add \"Eternal Union\" Title into Closet.",
        "id": "Gunakan untuk menambahkan Judul \"Ikatan Sanubari Abadi\" ke dalam lemari."
    },
    # 53: 通关指定层数可领取奖励
    "通关指定层数可领取奖励": {
        "tc": "通關指定層數可領取獎勵",
        "en": "Clear specified floors to claim rewards",
        "id": "Selesaikan lantai yang ditentukan untuk mengklaim hadiah"
    },
    # 60: 使用后习得灵级生息神丹的炼制之法...
    "使用后习得灵级生息神丹的炼制之法。（天品炼丹师方可使用）\\n生息神丹服用后提升身法和木系伤害。": {
        "tc": "使用後習得靈級生息神丹的煉製之法。（天品煉丹師方可使用）\\n生息神丹服用後提升身法和木系傷害。",
        "en": "Use to learn how to refine Spirit Grade Life Vitality Divine Orb. (Usable by G.Heaven Alchemist)\\nLife Vitality Divine Orb increases Agility and Wood DMG when taken.",
        "id": "Gunakan untuk mempelajari metode pemurnian Orb Dewa Pertumbuhan Hidup Tingkat Roh. (Dapat digunakan oleh G.Surga Alkimis)\\nMengonsumsi Orb Dewa Pertumbuhan Hidup meningkatkan Kelincahan dan DMG Kayu."
    },
    # 68: 连绵不绝的牡丹花海...
    "连绵不绝的牡丹花海，姹紫嫣红，似朝霞绽放于漫山遍野之间。若仙家景象，然花海深远，不可知之地甚多，于此历练福祸难料。": {
        "tc": "連綿不絕的牡丹花海，姹紫嫣紅，似朝霞綻放於漫山遍野之間。若仙家景象，然花海深遠，不可知之地甚多，於此歷練福禍難料。",
        "en": "An endless sea of peony flowers, brilliant and blooming with vibrant colors like morning glow across the mountains and fields. A sight akin to an immortal realm, yet the floral expanse is vast and profound with many uncharted territories; trials here hold unpredictable fortunes and perils.",
        "id": "Lautan bunga peoni yang tak berujung, semarak penuh warna bagai cahaya fajar bermekaran di seluruh penjuru gunung dan ladang. Bagai pemandangan alam para dewa, namun lautan bunga terbentang luas dan penuh tempat yang tak terjamah; berlatih di sini membawa nasib baik dan bahaya yang tak terduga."
    },
    # 85: 1、每步消耗1点体力...
    "1、每步消耗1点体力，体力上限100点，每天0点补满100点体力。（购买官职后，可提升体力存储上限。）\\n2、击败守卫可往前进入下一重天的传送门\\n3、九重天为跨服场景，地图内的资源、奇遇任何道友触发后消失\\n4、被除盗宝仙人外的怪物击败会退出场景，每只盗宝仙人只能挑战一次\\n5、仙官可以获得一个九重天生效的增益，每重天每天只能获取一次\\n6、兑换仙人处可以换取仙界稀有道具\\n7、地图内所有怪物和采集都会定时刷新，每天0点重置后，地图怪物等信息会被重置\\n8、当前在地图内时，切换九重天地图扣除1点体力\\n9、如外部奇遇存储达到上限，则九重天内无法触发新奇遇": {
        "tc": "1、每步消耗1點體力，體力上限100點，每天0點補滿100點體力。（購買官職後，可提升體力存儲上限。）\\n2、擊敗守衛可往前進入下一重天的傳送門\\n3、九重天為跨服場景，地圖內的資源、奇遇任何道友觸發後消失\\n4、被除盜寶仙人外的怪物擊敗會退出場景，每隻盜寶仙人只能挑戰一次\\n5、仙官可以獲得一個九重天生效的增益，每重天每天只能獲取一次\\n6、兌換仙人處可以換取仙界稀有道具\\n7、地圖內所有怪物和採集都會定時刷新，每天0點重置後，地圖怪物等信息會被重置\\n8、當前在地圖內時，切換九重天地圖扣除1點體力\\n9、如外部奇遇存儲達到上限，則九重天內無法觸發新奇遇",
        "en": "1. Each step consumes 1 Action Point, max Action Points: 100, restored to 100 Action Points daily at 00:00. (Purchasing an official rank increases the Action Point storage cap.)\\n2. Defeat guards to advance to the portal of the next realm of heaven\\n3. Cloud Nine is a cross-server scene; resources and encounters on the map disappear once triggered by any player\\n4. Being defeated by monsters other than the Treasure Stealing Immortal will exit the scene; each Treasure Stealing Immortal can only be challenged once\\n5. Immortal Officials can obtain a buff effective in Cloud Nine, which can only be obtained once per realm per day\\n6. Rare immortal realm items can be exchanged at the Exchange Immortal\\n7. All monsters and gathering nodes in the map refresh regularly; map monsters and other data are reset after 00:00 daily\\n8. While currently inside the map, switching Cloud Nine maps deducts 1 Action Point\\n9. If outside encounter storage reaches its limit, new encounters cannot be triggered in Cloud Nine",
        "id": "1. Setiap langkah mengonsumsi 1 Action Point, batas maksimal 100 poin, dipulihkan penuh 100 poin setiap hari pukul 00:00. (Membeli jabatan resmi dapat meningkatkan batas penyimpanan Action Point.)\\n2. Kalahkan penjaga untuk melangkah maju ke portal tingkat langit berikutnya\\n3. Awan Sembilan adalah area lintas-server; sumber daya dan petualangan di dalam peta akan lenyap setelah dipicu oleh rekan mana pun\\n4. Dikalahkan oleh monster selain Peri Pencuri Harta akan keluar dari area; setiap Peri Pencuri Harta hanya dapat ditantang satu kali\\n5. Pejabat Abadi dapat memperoleh satu buff yang berlaku di Awan Sembilan, hanya dapat diperoleh satu kali per tingkat langit per hari\\n6. Item langka dunia dewa dapat ditukarkan di Peri Penukaran\\n7. Semua monster dan titik pengumpulan di dalam peta diperbarui secara berkala; setelah reset pada pukul 00:00 setiap hari, informasi monster peta akan direset\\n8. Saat berada di dalam peta, beralih peta Awan Sembilan memotong 1 Action Point\\n9. Jika batas penyimpanan petualangan luar telah tercapai, petualangan baru tidak dapat dipicu di Awan Sembilan"
    },
    # 86: <color=#008000>【新效果】</color>
    "<color=#008000>【新效果】</color>": {
        "tc": "<color=#008000>【新效果】</color>",
        "en": "<color=#008000>[New Effect]</color>",
        "id": "<color=#008000>[Efek Baru]</color>"
    },
    # 98: 是否花费<color=#ad2228>%s体力</color>进行<color=#ad2228>%s</color>次扫荡？\n\n通关层数奖励自动获取，无需手动领取
    "是否花费<color=#ad2228>%s体力</color>进行<color=#ad2228>%s</color>次扫荡？\\n\\n通关层数奖励自动获取，无需手动领取": {
        "tc": "是否花費<color=#ad2228>%s體力</color>進行<color=#ad2228>%s</color>次掃蕩？\\n\\n通關層數獎勵自動獲取，無需手動領取",
        "en": "Spend <color=#ad2228>%s Action Points</color> to sweep <color=#ad2228>%s</color> times?\\n\\nCleared floor rewards are automatically collected, no manual claim required",
        "id": "Apakah ingin menggunakan <color=#ad2228>%s Action Point</color> untuk melakukan pembersihan <color=#ad2228>%s</color> kali?\\n\\nHadiah penyelesaian lantai diperoleh secara otomatis, tidak perlu diambil secara manual"
    },
    # 107: 灵级明悟神丹方
    "灵级明悟神丹方": {
        "tc": "靈級明悟神丹方",
        "en": "Spirit Grade Enlightenment Divine Orb Recipe",
        "id": "Resep Orb Dewa Pencerahan Tingkat Roh"
    },
    # 111: 活动说明：...
    "活动说明：\\n1.活动开启后，通过完成任务可以获得仙册经验，仙册升级后可以领取对应的奖励，提升等级越高可以领取的等级奖励越多。\\n2.付费解锁高阶奖励后，在达到等级后可以领取高阶奖励，并且直接提升10级。\\n3.付费解锁高阶奖励后可以通过花费仙玉来购买等级，每花费60仙玉可以直接提升1级。\\n4、福地仙册持续时间仅与购买时间有关，福地重新开启后可以继续完成仙册任务。": {
        "tc": "活動說明：\\n1.活動開啟後，通過完成任務可以獲得仙冊經驗，仙冊升級後可以領取對應的獎勵，提升等級越高可以領取的等級獎勵越多。\\n2.付費解鎖高階獎勵後，在達到等級後可以領取高階獎勵，並且直接提升10級。\\n3.付費解鎖高階獎勵後可以通過花費仙玉來購買等級，每花費60仙玉可以直接提升1級。\\n4、福地仙冊持續時間僅與購買時間有關，福地重新開啟後可以繼續完成仙冊任務。",
        "en": "Event Description:\\n1. After event opens, complete quests to gain Divine Book EXP. Upgrade the Divine Book to claim corresponding rewards; the higher the level, the more level rewards you can claim.\\n2. After unlocking Advanced Rewards, you can claim advanced rewards upon reaching levels, and immediately gain 10 levels.\\n3. After unlocking Advanced Rewards, you can purchase levels by spending Jade; each 60 Jade spent increases 1 level directly.\\n4. Blessed Land Divine Book duration depends solely on purchase time. You can continue completing Divine Book quests when Blessed Land reopens.",
        "id": "Deskripsi Event:\\n1. Setelah event dibuka, selesaikan misi untuk memperoleh EXP Buku Ilahi. Tingkatkan level Buku Ilahi untuk mengklaim hadiah yang sesuai; semakin tinggi level yang dicapai, semakin banyak hadiah level yang dapat diklaim.\\n2. Setelah membuka Hadiah Tingkat Lanjut berbayar, Anda dapat mengklaim hadiah tingkat lanjut setelah mencapai level yang sesuai, dan langsung meningkatkan 10 level.\\n3. Setelah membuka Hadiah Tingkat Lanjut berbayar, Anda dapat membeli level dengan menghabiskan Batu Giok; setiap 60 Batu Giok yang dihabiskan dapat langsung menaikkan 1 level.\\n4. Durasi Buku Ilahi Tanah Berkah hanya berkaitan dengan waktu pembelian. Anda dapat terus menyelesaikan misi Buku Ilahi saat Tanah Berkah dibuka kembali."
    },
    # 112: 修行界初级功法需要...
    "修行界初级功法需要<color=#458114>金丹</color>方可参悟\\n停车坐爱枫林晚，霜叶红于二月花。\\n效果：<color=#458114>攻击增强</color>": {
        "tc": "修行界初級功法需要<color=#458114>金丹</color>方可參悟\\n停車坐愛楓林晚，霜葉紅於二月花。\\n效果：<color=#458114>攻擊增強</color>",
        "en": "Cultivation world's elementary Technique requires <color=#458114>Formation</color> to comprehend\\nStopping the carriage to admire the maple woods at dusk, frosty leaves are redder than spring flowers.\\nEffect: <color=#458114>ATK Increased</color>",
        "id": "Teknik dasar dunia kultivasi membutuhkan <color=#458114>Formasi</color> untuk dipahami\\nBerhenti sejenak mengagumi hutan maple di kala senja, daun beku lebih merah daripada bunga musim semi.\\nEfek: <color=#458114>ATK Meningkat</color>"
    },
    # 113: 祝贺道友本赛季论道大会荣誉上榜...
    "祝贺道友本赛季论道大会荣誉上榜，位列前1000名，名传三界，威名赫赫。": {
        "tc": "祝賀道友本賽季論道大會榮譽上榜，位列前1000名，名傳三界，威名赫赫。",
        "en": "Congratulations, Fellow Daoist, for earning an honorable spot on the Theory Assembly leaderboard this season, ranking in the top 1,000! Your fame echoes across the Three Realms with great renown.",
        "id": "Selamat kepada Rekan Daois yang berhasil masuk daftar kehormatan Pertemuan Teori musim ini, menempati peringkat 1.000 teratas! Kemasyhuran Anda menggema di Tiga Alam dengan kemuliaan yang agung."
    },
    # 114: 精英魔物·甲
    "精英魔物·甲": {
        "tc": "精英魔物·甲",
        "en": "Elite Monster · Armor",
        "id": "Monster Elit · Armor"
    }
}

result = {}
missing = []

for it in items:
    if it in custom_dict:
        result[it] = custom_dict[it]
    elif '道场守卫' in it:
        m = re.match(r'^名称：道场守卫\\n修为：(.+?)(一阶|二阶|三阶|四阶|五阶|六阶|七阶|八阶|九阶|十阶)\\n修炼：(\d+)年$', it)
        if m:
            realm, stage, years = m.groups()
            r_tc = realm_map[realm]['tc']
            r_en = realm_map[realm]['en']
            r_id = realm_map[realm]['id']

            s_tc = stage_num_map[stage]['tc']
            s_en = stage_num_map[stage]['en']
            s_id = stage_num_map[stage]['id']

            result[it] = {
                "tc": f"名稱：道場守衛\\n修為：{r_tc}{s_tc}\\n修煉：{years}年",
                "en": f"Name: Dojo Guard\\nAttainment: {r_en} {s_en}\\nPracticing: {years} years",
                "id": f"Nama: Penjaga Dojo\\nCapaian: {r_id} {s_id}\\nLatihan: {years} tahun"
            }
        else:
            missing.append(it)
    else:
        missing.append(it)

print(f"Total processed: {len(result)} / {len(items)}")
if missing:
    print(f"Missing items ({len(missing)}):")
    for m in missing:
        print("  MISSING:", repr(m))
else:
    print("ALL 115 ITEMS PROCESSED SUCCESSFULLY!")

    # Now run strict verification
    print("\n--- Running Strict Validation ---")
    ph_re = re.compile(r'%[0-9]*\.?[0-9]*[sdf%]')
    color_re = re.compile(r'<color=#[0-9a-fA-F]+>|</color>')

    errors = 0
    for k, v in result.items():
        # check keys
        for lang in ['tc', 'en', 'id']:
            if lang not in v or not v[lang]:
                print(f"ERROR: missing {lang} for {k}")
                errors += 1

            # check placeholders
            orig_phs = ph_re.findall(k)
            trans_phs = ph_re.findall(v[lang])
            if orig_phs != trans_phs:
                print(f"ERROR: placeholder mismatch in {lang} for {k}: {orig_phs} vs {trans_phs}")
                errors += 1

            # check colors
            orig_colors = color_re.findall(k)
            trans_colors = color_re.findall(v[lang])
            if orig_colors != trans_colors:
                print(f"ERROR: color mismatch in {lang} for {k}: {orig_colors} vs {trans_colors}")
                errors += 1

            # check literal \n count
            orig_nl = k.count('\\n')
            trans_nl = v[lang].count('\\n')
            if orig_nl != trans_nl:
                print(f"ERROR: newline mismatch in {lang} for {k}: {orig_nl} vs {trans_nl}")
                errors += 1

    if errors == 0:
        print("ALL STRICT VALIDATIONS PASSED PERFECTLY!")
        # Save to result_chunk_3.json
        out_path = 'F:/项目/无极国际版/result_chunk_3.json'
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"Successfully saved to {out_path}")
    else:
        print(f"Validation found {errors} errors!")
