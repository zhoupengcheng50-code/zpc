# -*- coding: utf-8 -*-
import json
import re

# Load source chunk_2
with open(r'F:\项目\无极国际版\chunk_2.json', 'r', encoding='utf-8') as f:
    chunk_2 = json.load(f)

translations = {}

translations[chunk_2[0]] = {
    "tc": "靈級樹魄神丹",
    "en": "G.Spirit Wood Soul Orb",
    "id": "G.Roh Wood Soul Orb"
}

translations[chunk_2[1]] = {
    "tc": "任意一個靈獸解鎖血脈功能(1轉50級)",
    "en": "Any Pet unlocks the Vein function (Tra.1 Lv.50)",
    "id": "Peliharaan apa pun membuka fungsi Garis Keturunan (Tra.1 Lv.50)"
}

translations[chunk_2[2]] = {
    "tc": "收集[嫡仙兒信箋]",
    "en": "Collect [Di Xian'er Letter]",
    "id": "Kumpulkan [Surat Di Xian'er]"
}

translations[chunk_2[3]] = {
    "tc": "未有道侶",
    "en": "No Partner yet",
    "id": "Belum ada Pasangan"
}

translations[chunk_2[4]] = {
    "tc": r"名稱：道場守衛\n修為：元嬰六階\n修煉：741年",
    "en": r"Name：Dojo Guard\nAttainment：Nascence G.6\nPracticing：741 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Nascence G.6\nLatihan：741 tahun"
}

translations[chunk_2[5]] = {
    "tc": "服用後凝練修士修為，增加210身法、700點金系傷害。（最多服用80個）",
    "en": "Able to condense the attainment, increase Agility by 210, Metal DMG by 700.(Max 80 can be used)",
    "id": "Mampu memadatkan Capaian, meningkatkan Kelincahan sebesar 210, DMG Logam sebesar 700.(Maks 80 dapat digunakan)"
}

translations[chunk_2[6]] = {
    "tc": "當前不滿足領取條件",
    "en": "Currently doesn't meet the acquiring conditions",
    "id": "Saat ini tidak memenuhi persyaratan perolehan"
}

translations[chunk_2[7]] = {
    "tc": "靈級金焰神丹方",
    "en": "G.Spirit Golden Flame Orb Recipe",
    "id": "Resep G.Roh Golden Flame Orb"
}

translations[chunk_2[8]] = {
    "tc": r"名稱：道場守衛\n修為：太乙玉仙三階\n修煉：1354年",
    "en": r"Name：Dojo Guard\nAttainment：Taiyi G.3\nPracticing：1354 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Taiyi G.3\nLatihan：1354 tahun"
}

translations[chunk_2[9]] = {
    "tc": "完成極品機緣有幾率獲得以下道具",
    "en": "Complete Supreme Fortune for a chance to obtain the following items",
    "id": "Selesaikan Peluang Terbaik berpeluang memperoleh item berikut"
}

translations[chunk_2[10]] = {
    "tc": "每次參悟可獲得：%s",
    "en": "Each comprehension grants: %s",
    "id": "Setiap pemahaman dapat memperoleh: %s"
}

translations[chunk_2[11]] = {
    "tc": r"名稱：道場守衛\n修為：真仙一階\n修煉：1754年",
    "en": r"Name：Dojo Guard\nAttainment：Deity G.1\nPracticing：1754 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Dewa G.1\nLatihan：1754 tahun"
}

translations[chunk_2[12]] = {
    "tc": "靈級奇火神丹方",
    "en": "G.Spirit Strange Fire Orb Recipe",
    "id": "Resep G.Roh Strange Fire Orb"
}

translations[chunk_2[13]] = {
    "tc": "靈獸招式參悟未開啟",
    "en": "Pet Skill Comprehension not unlocked",
    "id": "Pemahaman Skill Peliharaan belum dibuka"
}

translations[chunk_2[14]] = {
    "tc": "不知何時被封存的秘寶，已經化為了仙珀一樣的礦石，小心打開後90%概率獲得隨機1至3個秘寶碎片，10%概率隨機獲得1個完整的秘寶。",
    "en": "A secret treasure sealed away long ago has turned into amber-like ore. Carefully opening it gives a 90% chance to randomly obtain 1-3 Secret Treasure Shards, and a 10% chance to randomly obtain 1 complete Secret Treasure.",
    "id": "Harta rahasia yang disegel entah sejak kapan telah berubah menjadi bijih seperti amber abadi. Membukanya dengan hati-hati memberikan 90% peluang untuk secara acak memperoleh 1 hingga 3 Fragmen Harta Rahasia, dan 10% peluang untuk secara acak memperoleh 1 Harta Rahasia utuh."
}

translations[chunk_2[15]] = {
    "tc": r"使用後習得靈級化血神丹的煉製之法。（天品煉丹師方可使用）\n化血神丹服用後提升真氣和木系傷害。",
    "en": r"Use to learn the refining method of G.Spirit Blood-Transforming Orb.(Usable by G.Heaven Alchemist)\nBlood-Transforming Orb could use to improve Qi and Wood DMG.",
    "id": r"Gunakan untuk mempelajari metode pemurnian G.Roh Blood-Transforming Orb.(Dapat digunakan oleh G.Surga Alkimis)\nBlood-Transforming Orb dapat digunakan untuk meningkatkan Qi dan DMG Kayu."
}

translations[chunk_2[16]] = {
    "tc": r"名稱：道場守衛\n修為：大乘一階\n修煉：1334年",
    "en": r"Name：Dojo Guard\nAttainment：Mahayana G.1\nPracticing：1334 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Mahayana G.1\nLatihan：1334 tahun"
}

translations[chunk_2[17]] = {
    "tc": "春潮天書",
    "en": "Spring Tide Tome",
    "id": "Kitab Suci Pasang Musim Semi"
}

translations[chunk_2[18]] = {
    "tc": "曾有一青雲妖靈佔據此山，為禍人界,不肯飛升。終觸怒上仙，滅其體魄而困其神魂。常有人於此山中聽到喟嘆：久在樊籠中，何時返自然。",
    "en": "Once a Qingyun Demon Spirit occupied this mountain, wreaking havoc in the mortal realm and refusing to ascend. It eventually angered a High Immortal, who destroyed its physical body and trapped its soul. People often hear sighs echoing in this mountain: \"Long trapped within a cage, when shall I return to nature.\"",
    "id": "Pernah ada Roh Iblis Qingyun yang menguasai gunung ini, mendatangkan malapetaka di dunia fana dan menolak untuk naik ke alam atas. Akhirnya memicu kemarahan Dewa Agung, yang menghancurkan tubuh fisiknya dan mengurung jiwanya. Orang-orang sering mendengar desah keluh di gunung ini: \"Terlalu lama di dalam sangkar, kapankah bisa kembali ke alam bebas.\""
}

translations[chunk_2[19]] = {
    "tc": r"名稱：道場守衛\n修為：仙帝九階\n修煉：1234年",
    "en": r"Name：Dojo Guard\nAttainment：Deity Emperor G.9\nPracticing：1234 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Kaisar Dewa G.9\nLatihan：1234 tahun"
}

translations[chunk_2[20]] = {
    "tc": "靈級朱果神丹方",
    "en": "G.Spirit Vermilion Fruit Orb Recipe",
    "id": "Resep G.Roh Vermilion Fruit Orb"
}

translations[chunk_2[21]] = {
    "tc": "背包空間不足，禮包以郵件形式發放，請注意查收",
    "en": "Insufficient backpack space. The pack has been sent via mail, please check your inbox",
    "id": "Ruang ransel tidak mencukupi, paket hadiah telah dikirim melalui surat, silakan periksa kotak masuk"
}

translations[chunk_2[22]] = {
    "tc": r"1.道友完成仙途任務，可領取獎勵\n2.仙途任務記錄了道友從人間到天外天的遊戲歷程",
    "en": r"1. Cultivators who complete Immortal Path Quests can claim rewards.\n2. Immortal Path Quests record your journey from the Mortal Realm to Beyond Heaven.",
    "id": r"1. Rekan Taois yang menyelesaikan Quest Jalan Abadi dapat mengklaim hadiah.\n2. Quest Jalan Abadi mencatat perjalanan Rekan Taois dari Dunia Fana hingga ke Luar Surga."
}

translations[chunk_2[23]] = {
    "tc": "魂力描述：%s",
    "en": "Soul Power Description: %s",
    "id": "Deskripsi Kekuatan Jiwa: %s"
}

translations[chunk_2[24]] = {
    "tc": r"使用後將“威震八方”頭像框加入衣閣。\n（<color=#458114>“論道大會”限時外觀，下個賽季前回收</color>）",
    "en": r'Use to add the "Awe the Eight Directions" profile frame to the Closet.\n(<color=#458114>Limited appearance of "Debate Assembly", reclaimed before the next season</color>)',
    "id": r'Gunakan untuk menambahkan bingkai avatar "Mengguncang Delapan Penjuru" ke Lemari.\n(<color=#458114>Tampilan terbatas "Konferensi Debat", akan ditarik sebelum musim berikutnya</color>)'
}

translations[chunk_2[25]] = {
    "tc": r"1.道友<color=#9e4444>種植誘妖草</color>，進入<color=#9e4444>誘捕陣</color>中誘捕妖獸（升級陣法還可以削弱妖獸的實力）。\n2.挑戰妖獸可獲得<color=#9e4444>妖獸殘血</color>和<color=#9e4444>妖獸精血</color>資源。\n3.積攢這兩種資源後前往靈獸功能去培養<color=#9e4444>靈獸血脈</color>，獲得屬性加成。",
    "en": r"1. Cultivators can <color=#9e4444>plant Fiend Tempter</color> and enter the <color=#9e4444>Trapping Array</color> to trap fiends (upgrading the array can also weaken fiends' power).\n2. Challenging fiends grants <color=#9e4444>Fiend Blood</color> and <color=#9e4444>Fiend Essence</color> resources.\n3. After collecting both resources, go to the Pet function to cultivate <color=#9e4444>Pet Veins</color> and gain attribute bonuses.",
    "id": r"1. Rekan Taois dapat <color=#9e4444>menanam Fiend Tempter</color> dan memasuki <color=#9e4444>Teknik Menjerat</color> untuk menjerat siluman (meningkatkan formasi juga dapat melemahkan kekuatan siluman).\n2. Menantang siluman memberikan sumber daya <color=#9e4444>Darah Iblis</color> dan <color=#9e4444>Esensi Iblis</color>.\n3. Kumpulkan kedua sumber daya ini lalu buka fitur Peliharaan untuk mengembangkan <color=#9e4444>Garis Keturunan Peliharaan</color> guna memperoleh bonus atribut."
}

translations[chunk_2[26]] = {
    "tc": "靈級金焰神丹",
    "en": "G.Spirit Golden Flame Orb",
    "id": "G.Roh Golden Flame Orb"
}

translations[chunk_2[27]] = {
    "tc": "收集[牧梅信箋]",
    "en": "Collect [Mu Mei Letter]",
    "id": "Kumpulkan [Surat Mu Mei]"
}

translations[chunk_2[28]] = {
    "tc": "靈級地鳴神丹方",
    "en": "G.Spirit Earth Roar Orb Recipe",
    "id": "Resep G.Roh Earth Roar Orb"
}

translations[chunk_2[29]] = {
    "tc": "挑戰已結束",
    "en": "Challenge has ended",
    "id": "Tantangan telah berakhir"
}

translations[chunk_2[30]] = {
    "tc": "靈級紫陽神丹",
    "en": "G.Spirit Purple Sun Orb",
    "id": "G.Roh Purple Sun Orb"
}

translations[chunk_2[31]] = {
    "tc": "晨息悟性丹",
    "en": "Morning Breath Savvy Pill",
    "id": "Pil Akal Napas Pagi"
}

translations[chunk_2[32]] = {
    "tc": "<color=#ad2228>%s</color>修為/秒 <color=#ad2228>%s</color>悟道經驗/次",
    "en": "<color=#ad2228>%s</color> Attainment/sec <color=#ad2228>%s</color> Enlightenment EXP/time",
    "id": "<color=#ad2228>%s</color> Capaian/detik <color=#ad2228>%s</color> EXP Pencerahan/kali"
}

translations[chunk_2[33]] = {
    "tc": "此道場由上古大能所佈置，為避免出現傷亡，讓修真界蒙受無謂的損失，特設禁制限制參與者修為和實力",
    "en": "This dojo was arranged by ancient almighty beings. To avoid casualties and unnecessary losses to the cultivation world, special restrictions are placed on participants' attainment and strength",
    "id": "Dojo ini ditata oleh tokoh perkasa kuno. Untuk menghindari korban dan kerugian yang tidak perlu di dunia kultivasi, pembatasan khusus diberlakukan untuk membatasi Capaian dan kekuatan peserta"
}

translations[chunk_2[34]] = {
    "tc": r"名稱：道場守衛\n修為：合體七階\n修煉：1045年",
    "en": r"Name：Dojo Guard\nAttainment：Embodiment G.7\nPracticing：1045 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Menjelma G.7\nLatihan：1045 tahun"
}

translations[chunk_2[35]] = {
    "tc": "相傳臥牛真人在此潛修五百載，點化植精妖怪不知凡幾，福澤鄉鄰，庇護一方。仙逝後，世人感懷真人，故稱此山為臥牛山。",
    "en": "Legend has it that Woniu Immortal meditated here for 500 years, enlightening countless plant spirits and demons, blessing neighbors, and protecting the region. After his ascension, mortals honored the master and named this mountain Mt.Woniu.",
    "id": "Konon Woniu Immortal berkultivasi di sini selama 500 tahun, mencerahkan roh tumbuhan dan siluman yang tak terhitung jumlahnya, memberkati tetangga, dan melindungi wilayah tersebut. Setelah wafat, masyarakat mengenang sang pertapa dan menamai gunung ini Gunung Woniu."
}

translations[chunk_2[36]] = {
    "tc": "<color=#4f9a12>%s</color>個%s碎片",
    "en": "<color=#4f9a12>%s</color> %s Shard(s)",
    "id": "<color=#4f9a12>%s</color> Fragmen %s"
}

translations[chunk_2[37]] = {
    "tc": r"名稱：道場守衛\n修為：太乙玉仙一階\n修煉：1754年",
    "en": r"Name：Dojo Guard\nAttainment：Taiyi G.1\nPracticing：1754 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Taiyi G.1\nLatihan：1754 tahun"
}

translations[chunk_2[38]] = {
    "tc": "龍鹿之靈可以領悟到尖牙、潛伏、凶神血裔、剛鬃、朱鬣、機警、長生、火咒、水咒、岩咒、氣刃、五行結界",
    "en": "Dragon Deer Spirit can comprehend Piercing Fang, Stealth, Savage Blood, Tough Mane, Red Mane, Vigilant, Longevity, Fire Curse, Water Curse, Stone Curse, Blade Wave, 5-Element Border",
    "id": "Dragon Deer Spirit dapat memahami Menusuk Fang, Diam-diam, Darah Liar, Surai yang tangguh, Surai Merah, Waspada, Umur panjang, Kutukan Api, Kutukan Air, Kutukan Batu, Gelombang Pedang, Perbatasan 5-Elemen"
}

translations[chunk_2[39]] = {
    "tc": r"地上和飛升後是分開的，<color=#9e4444>不能同時參加</color>。戰場任務每天<color=#9e4444>12:00點到14:59點，20:00點到22:59點</color>是雙倍獎勵，不要錯過。\n\n<color=#0c5a8b>吞天塔招式推薦</color>：\n<color=#9e4444>熾陽焚天訣</color>（真氣輸出招式）、 <color=#9e4444>魔獄玄胎經</color>（超強防禦招式）、 <color=#9e4444>撼昆侖</color>（高階命中吸血）",
    "en": r"Mortal realm and post-ascension are separated, and <color=#9e4444>cannot be joined simultaneously</color>. Battlefield tasks have double rewards daily from <color=#9e4444>12:00 to 14:59, 20:00 to 22:59</color>, don't miss out.\n\n<color=#0c5a8b>Celestial Tower Skill Recommendations</color>:\n<color=#9e4444>Firestorm Stifling Chant</color> (Qi output skill), <color=#9e4444>Demon Prison Scripture</color> (Super defense skill), <color=#9e4444>Shook Kunlun</color> (High-tier hit lifesteal)",
    "id": r"Dunia fana dan pasca-kenaikan dipisahkan, <color=#9e4444>tidak dapat diikuti bersamaan</color>. Quest medan perang berhadiah ganda setiap hari pukul <color=#9e4444>12:00 hingga 14:59, 20:00 hingga 22:59</color>, jangan sampai terlewat.\n\n<color=#0c5a8b>Rekomendasi Skill Menara Surgawi</color>:\n<color=#9e4444>Nyanyian Menahan Badai Api</color> (Skill output Qi), <color=#9e4444>Kitab Suci Penjara Setan</color> (Skill pertahanan super), <color=#9e4444>Mengguncang Kunlun</color> (Hit lifesteal tingkat tinggi)"
}

translations[chunk_2[40]] = {
    "tc": "1、每日機緣次數+%s",
    "en": "1. Daily Fortune attempts +%s",
    "id": "1. Jumlah Peluang Harian +%s"
}

translations[chunk_2[41]] = {
    "tc": r"“論道大會”第二名頭像框\n（下賽季開啟後回收）",
    "en": r'"Debate Assembly" 2nd Place Profile Frame\n(Reclaimed after the next season begins)',
    "id": r'Bingkai Profil Juara 2 "Konferensi Debat"\n(Ditarik setelah musim berikutnya dibuka)'
}

translations[chunk_2[42]] = {
    "tc": r"名稱：道場守衛\n修為：太乙玉仙四階\n修煉：1324年",
    "en": r"Name：Dojo Guard\nAttainment：Taiyi G.4\nPracticing：1324 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Taiyi G.4\nLatihan：1324 tahun"
}

translations[chunk_2[43]] = {
    "tc": "靈獸十四",
    "en": "Pet 14",
    "id": "Peliharaan 14"
}

translations[chunk_2[44]] = {
    "tc": "紅楓神術",
    "en": "Red Maple Divine Art",
    "id": "Seni Ilahi Maple Merah"
}

translations[chunk_2[45]] = {
    "tc": "福玉",
    "en": "Fortune Jade",
    "id": "Batu Giok Berkah"
}

translations[chunk_2[46]] = {
    "tc": "收集[姜楠信箋]",
    "en": "Collect [Jiang Nan Letter]",
    "id": "Kumpulkan [Surat Jiang Nan]"
}

translations[chunk_2[47]] = {
    "tc": "月宮",
    "en": "Moon Palace",
    "id": "Istana Bulan"
}

translations[chunk_2[48]] = {
    "tc": "參悟道具",
    "en": "Comprehension Item",
    "id": "Item Pemahaman"
}

translations[chunk_2[49]] = {
    "tc": "首次領悟可獲得：%s",
    "en": "First comprehension grants: %s",
    "id": "Pemahaman pertama dapat memperoleh: %s"
}

translations[chunk_2[50]] = {
    "tc": r"名稱：道場守衛\n修為：合體一階\n修煉：974年",
    "en": r"Name：Dojo Guard\nAttainment：Embodiment G.1\nPracticing：974 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Menjelma G.1\nLatihan：974 tahun"
}

translations[chunk_2[51]] = {
    "tc": r"名稱：道場守衛\n修為：煉虛五階\n修煉：1347年",
    "en": r"Name：Dojo Guard\nAttainment：Vainify G.5\nPracticing：1347 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Merusak G.5\nLatihan：1347 tahun"
}

translations[chunk_2[52]] = {
    "tc": r"使用後習得靈級金焰神丹的煉製之法。（天品煉丹師方可使用）\n金焰神丹服用後提升體魄和火系傷害。",
    "en": r"Use to learn the refining method of G.Spirit Golden Flame Orb.(Usable by G.Heaven Alchemist)\nGolden Flame Orb could use to improve Health and Fire DMG.",
    "id": r"Gunakan untuk mempelajari metode pemurnian G.Roh Golden Flame Orb.(Dapat digunakan oleh G.Surga Alkimis)\nGolden Flame Orb dapat digunakan untuk meningkatkan Kesehatan dan DMG Api."
}

translations[chunk_2[53]] = {
    "tc": r"使用後習得靈級地鳴神丹的煉製之法。（天品煉丹師方可使用）\n地鳴神丹服用後提升根骨和土系傷害。",
    "en": r"Use to learn the refining method of G.Spirit Earth Roar Orb.(Usable by G.Heaven Alchemist)\nEarth Roar Orb could use to improve Strength and Earth DMG.",
    "id": r"Gunakan untuk mempelajari metode pemurnian G.Roh Earth Roar Orb.(Dapat digunakan oleh G.Surga Alkimis)\nEarth Roar Orb dapat digunakan untuk meningkatkan Daya dan DMG Bumi."
}

translations[chunk_2[54]] = {
    "tc": r"修行界頂級功法需要<color=#458114>太乙玉仙</color>方可參悟\n效果：<color=#458114>生命提升</color>",
    "en": r"Top cultivation technique requires <color=#458114>Taiyi</color> to comprehend\nEffect: <color=#458114>HP Increase</color>",
    "id": r"Teknik tingkat atas dunia kultivasi membutuhkan <color=#458114>Taiyi</color> untuk dipahami\nEfek: <color=#458114>Peningkatan HP</color>"
}

translations[chunk_2[55]] = {
    "tc": "使用後將“氣吞山河”頭像框加入衣閣。",
    "en": 'Use to add the "Majestic Spirit" profile frame to the Closet.',
    "id": 'Gunakan untuk menambahkan bingkai avatar "Murka Penelan Buana" ke Lemari.'
}

translations[chunk_2[56]] = {
    "tc": "悲秋功法禮包",
    "en": "Autumn Grief Technique Pack",
    "id": "Paket Hadiah Teknik Duka Musim Gugur"
}

translations[chunk_2[57]] = {
    "tc": "春山如笑",
    "en": "Smiling Spring Hills",
    "id": "Bukit Musim Semi Berseri"
}

translations[chunk_2[58]] = {
    "tc": "悲秋靈本",
    "en": "Autumn Grief Spirit Manual",
    "id": "Buku Roh Duka Musim Gugur"
}

translations[chunk_2[59]] = {
    "tc": r"名稱：道場守衛\n修為：太乙玉仙九階\n修煉：1234年",
    "en": r"Name：Dojo Guard\nAttainment：Taiyi G.9\nPracticing：1234 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Taiyi G.9\nLatihan：1234 tahun"
}

translations[chunk_2[60]] = {
    "tc": r"名稱：道場守衛\n修為：遊仙六階\n修煉：1247年",
    "en": r"Name：Dojo Guard\nAttainment：Wanderer G.6\nPracticing：1247 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Tualang G.6\nLatihan：1247 tahun"
}

translations[chunk_2[61]] = {
    "tc": r"名稱：道場守衛\n修為：合體四階\n修煉：1345年",
    "en": r"Name：Dojo Guard\nAttainment：Embodiment G.4\nPracticing：1345 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Menjelma G.4\nLatihan：1345 tahun"
}

translations[chunk_2[62]] = {
    "tc": "收集[柳沐瑤信箋]",
    "en": "Collect [Liu Muyao Letter]",
    "id": "Kumpulkan [Surat Liu Muyao]"
}

translations[chunk_2[63]] = {
    "tc": "威震八方",
    "en": "Awe the Eight Directions",
    "id": "Mengguncang Delapan Penjuru"
}

translations[chunk_2[64]] = {
    "tc": "請按順序購買前置福袋",
    "en": "Please purchase prerequisite Lucky Bags in order",
    "id": "Silakan beli Tas Keberuntungan prasyarat secara berurutan"
}

translations[chunk_2[65]] = {
    "tc": r"1.<color=#9e4444>覺醒血脈</color>可獲得基礎屬性，不同品質的靈獸可覺醒血脈數量不同。\n2.消耗妖獸殘血和妖獸精血可強化血脈的基礎屬性。\n3.解鎖<color=#9e4444>血脈淬煉</color>功能後可消耗妖獸精血淬煉不同類型的屬性詞條，獲得大量屬性加成。",
    "en": r"1. <color=#9e4444>Awakening Veins</color> grants basic attributes. Pets of different qualities can awaken different numbers of veins.\n2. Consuming Fiend Blood and Fiend Essence can strengthen the basic attributes of veins.\n3. After unlocking the <color=#9e4444>Vein Tempering</color> function, Fiend Essence can be consumed to temper different types of attribute affixes, gaining massive attribute bonuses.",
    "id": r"1. <color=#9e4444>Membangkitkan Garis Keturunan</color> memberikan atribut dasar. Peliharaan dengan kualitas berbeda dapat membangkitkan jumlah garis keturunan yang berbeda.\n2. Mengonsumsi Darah Iblis dan Esensi Iblis dapat memperkuat atribut dasar garis keturunan.\n3. Setelah membuka fitur <color=#9e4444>Penempaan Garis Keturunan</color>, Esensi Iblis dapat digunakan untuk menempa berbagai jenis atribut, memberikan peningkatan atribut yang besar."
}

translations[chunk_2[66]] = {
    "tc": "悲秋心法",
    "en": "Autumn Grief Mental Method",
    "id": "Metode Mental Duka Musim Gugur"
}

translations[chunk_2[67]] = {
    "tc": r"名稱：道場守衛\n修為：仙尊十階\n修煉：1425年",
    "en": r"Name：Dojo Guard\nAttainment：Deity Lord G.10\nPracticing：1425 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Mahadewa Raja G.10\nLatihan：1425 tahun"
}

translations[chunk_2[68]] = {
    "tc": "祝賀道友本賽季論道大會榮譽上榜，位列榜首，威震寰宇，天下無敵。",
    "en": "Congratulations, fellow cultivator, on making the honor roll of this season's Debate Assembly, claiming the top spot, shaking the cosmos, and becoming invincible throughout the world.",
    "id": "Selamat kepada Rekan Taois yang masuk dalam daftar kehormatan Konferensi Debat musim ini, menduduki peringkat teratas, mengguncang jagat raya, dan tak terkalahkan di dunia."
}

translations[chunk_2[69]] = {
    "tc": "收集[居雲岫信箋]",
    "en": "Collect [Ju Yunxiu Letter]",
    "id": "Kumpulkan [Surat Ju Yunxiu]"
}

translations[chunk_2[70]] = {
    "tc": "本次更換將重新選擇獎池全部獎勵，當前獎池剩餘獎勵將不可再進行抽取，道具%s將消耗獎勵可選次數，是否確認？",
    "en": "This change will reselect all rewards in the prize pool. Remaining rewards in the current prize pool can no longer be drawn. Item %s will consume optional reward attempts. Confirm?",
    "id": "Penggantian ini akan memilih kembali semua hadiah di kumpulan hadiah, sisa hadiah di kumpulan saat ini tidak dapat diundi lagi, item %s akan menghabiskan kesempatan memilih hadiah, konfirmasi?"
}

translations[chunk_2[71]] = {
    "tc": r"玩法說明：\n1.論道大會為跨服比武論道玩法\n2.本次玩法為PVP測試玩法，若有設計不周敬請諒解\n參與條件：\n1.飛升後可參加\n開啟時間：\n1.論道大會為賽季形式，賽季之間間隔2周開啟一次\n2.每賽季持續1周，挑戰時間：周一至周五，結算時間周六晚上00:00點\n段位與積分：\n1.段位：共有9個段位，積分達到指定值之後可以晉升段位\n2.晉升段位後會獲得段位獎勵\n3.積分少於指定值之後，段位會降級（不影響已獲得的段位獎勵）\n4.積分：積分用於段位晉升和排名，賽季結束會根據當時排名發放一份獎勵\n5.上榜條件：段位達到玄階初級才可上榜參與排名匹配規則：\n1.所有玩家初始默認有100積分，段位為黃階初級\n2.匹配與自身積分、修煉年限、境界相近的玩家為對手\n戰鬥和獎勵：\n1.論道大會有相應禁制，限制玩家部分實力和規則，可在禁制中查看\n2.積分獎勵：挑戰勝利後有積分獎勵，積分多少根據對手的境界和修煉年限差值比例計算\n3.論道功勳：可在商鋪中兌換獎勵，挑戰勝利或失敗都會給，賽季不清空\n4.挑戰次數：剩餘挑戰次數，賽季結束時清空\n",
    "en": r"Gameplay Instructions:\n1. Debate Assembly is a cross-server martial debate gameplay\n2. This is a PVP test gameplay, please understand if there are imperfections in design\nParticipation Requirements:\n1. Available after ascension\nOpening Schedule:\n1. Debate Assembly is season-based, held once every 2 weeks\n2. Each season lasts 1 week, challenge time: Monday to Friday, settlement time: Saturday 00:00\nTier and Points:\n1. Tier: A total of 9 tiers, reaching specified points promotes you to a higher tier\n2. Tier rewards are granted upon promotion\n3. If points fall below specified value, tier will demote (does not affect claimed tier rewards)\n4. Points: Used for tier promotion and ranking. Rewards are issued based on ranking at season end\n5. Ranking Requirement: Reach G.Mythic Primary tier to qualify for ranking Matchmaking Rules:\n1. All players start with 100 points at G.Novice Primary tier\n2. Match with opponents with similar points, cultivation years, and realms\nBattle and Rewards:\n1. Debate Assembly has restrictions that limit certain player powers and rules, viewable in Restrictions\n2. Point Rewards: Points rewarded upon victory, amount calculated based on opponent realm and cultivation years difference ratio\n3. Debate Merits: Can be exchanged for rewards in Shop, granted win or lose, not reset between seasons\n4. Challenge Attempts: Remaining challenge attempts, cleared when season ends\n",
    "id": r"Petunjuk Gameplay:\n1. Konferensi Debat adalah gameplay debat bela diri lintas server\n2. Ini adalah gameplay uji coba PVP, mohon pengertiannya jika ada ketidaksempurnaan desain\nSyarat Partisipasi:\n1. Dapat diikuti setelah kenaikan\nWaktu Buka:\n1. Konferensi Debat dalam format musim, dibuka setiap jeda 2 minggu\n2. Setiap musim berlangsung 1 minggu, waktu tantangan: Senin hingga Jumat, penyelesaian: Sabtu pukul 00:00\nTingkat dan Poin:\n1. Tingkat: Ada 9 tingkat, mencapai poin tertentu dapat meningkatkan tingkat\n2. Hadiah tingkat diperoleh setelah naik tingkat\n3. Jika poin kurang dari nilai tertentu, tingkat akan turun (tidak mempengaruhi hadiah tingkat yang sudah diperoleh)\n4. Poin: Digunakan untuk kenaikan tingkat dan peringkat, hadiah dibagikan sesuai peringkat pada akhir musim\n5. Syarat Masuk Peringkat: Mencapai tingkat G.Mistik Pemula untuk masuk peringkat Aturan Pencocokan:\n1. Semua pemain awal memiliki 100 poin dengan tingkat G.Pemula Dasar\n2. Mencocokkan lawan dengan poin, tahun kultivasi, dan ranah yang sebanding\nPertempuran dan Hadiah:\n1. Konferensi Debat memiliki larangan khusus yang membatasi sebagian kekuatan dan aturan pemain, dapat dilihat di Larangan\n2. Hadiah Poin: Hadiah poin diberikan setelah menang tantangan, jumlah dihitung berdasarkan rasio selisih ranah dan tahun kultivasi lawan\n3. Prestasi Debat: Dapat ditukar hadiah di Toko, diberikan menang maupun kalah, tidak dihapus saat pergantian musim\n4. Jumlah Tantangan: Sisa kesempatan menantang, akan dikosongkan saat musim berakhir\n"
}

translations[chunk_2[72]] = {
    "tc": "獎勵已選擇完成，是否確認？",
    "en": "Reward selection complete. Confirm?",
    "id": "Hadiah telah selesai dipilih, apakah konfirmasi?"
}

translations[chunk_2[73]] = {
    "tc": "點擊誘捕陣按鈕",
    "en": "Click the Trapping Array button",
    "id": "Ketuk tombol Teknik Menjerat"
}

translations[chunk_2[74]] = {
    "tc": "積分：",
    "en": "Points:",
    "id": "Poin:"
}

translations[chunk_2[75]] = {
    "tc": r"名稱：道場守衛\n修為：大乘十階\n修煉：1456年",
    "en": r"Name：Dojo Guard\nAttainment：Mahayana G.10\nPracticing：1456 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Mahayana G.10\nLatihan：1456 tahun"
}

translations[chunk_2[76]] = {
    "tc": "靈級化血神丹方",
    "en": "G.Spirit Blood-Transforming Orb Recipe",
    "id": "Resep G.Roh Blood-Transforming Orb"
}

translations[chunk_2[77]] = {
    "tc": "神秘靈獸蛋-冬",
    "en": "Mysterious Pet Egg - Winter",
    "id": "Telur Peliharaan Misterius - Musim Dingin"
}

translations[chunk_2[78]] = {
    "tc": r"名稱：道場守衛\n修為：大羅金仙七階\n修煉：1456年",
    "en": r"Name：Dojo Guard\nAttainment：Daluo G.7\nPracticing：1456 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Daluo G.7\nLatihan：1456 tahun"
}

translations[chunk_2[79]] = {
    "tc": r"使用後習得靈級破浪神丹的煉製之法。（天品煉丹師方可使用）\n破浪神丹服用後提升身法和水系傷害。",
    "en": r"Use to learn the refining method of G.Spirit Wave-Breaking Orb.(Usable by G.Heaven Alchemist)\nWave-Breaking Orb could use to improve Agility and Water DMG.",
    "id": r"Gunakan untuk mempelajari metode pemurnian G.Roh Wave-Breaking Orb.(Dapat digunakan oleh G.Surga Alkimis)\nWave-Breaking Orb dapat digunakan untuk meningkatkan Kelincahan dan DMG Air."
}

translations[chunk_2[80]] = {
    "tc": "悲秋神術",
    "en": "Autumn Grief Divine Art",
    "id": "Seni Ilahi Duka Musim Gugur"
}

translations[chunk_2[81]] = {
    "tc": "服用後凝練修士修為，增加210體魄、700點土系傷害。（最多服用80個）",
    "en": "Able to condense the attainment, increase Health by 210, Earth DMG by 700.(Max 80 can be used)",
    "id": "Mampu memadatkan Capaian, meningkatkan Kesehatan sebesar 210, DMG Bumi sebesar 700.(Maks 80 dapat digunakan)"
}

translations[chunk_2[82]] = {
    "tc": "探路嘍囉·療",
    "en": "Scout Minion · Heal",
    "id": "Kroco Pengintai · Pulih"
}

translations[chunk_2[83]] = {
    "tc": "賽季獎勵預覽",
    "en": "Season Reward Preview",
    "id": "Pratinjau Hadiah Musim"
}

translations[chunk_2[84]] = {
    "tc": r"名稱：道場守衛\n修為：煉虛一階\n修煉：1754年",
    "en": r"Name：Dojo Guard\nAttainment：Vainify G.1\nPracticing：1754 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Merusak G.1\nLatihan：1754 tahun"
}

translations[chunk_2[85]] = {
    "tc": "仙界大能煉製，天帝特供，服用後能增加180點悟性。（最多服用100個）",
    "en": "Refined by almighty beings of the Immortal Realm, specially supplied for Heavenly Emperor, increases Savvy by 180 after use.(Max 100 can be used)",
    "id": "Dimurnikan oleh tokoh perkasa Alam Abadi, persembahan khusus Kaisar Langit, meningkatkan Akal sebesar 180 setelah digunakan.(Maks 100 dapat digunakan)"
}

translations[chunk_2[86]] = {
    "tc": "服用後凝練修士修為，增加210根骨、700點火系傷害。（最多服用80個）",
    "en": "Able to condense the attainment, increase Strength by 210, Fire DMG by 700.(Max 80 can be used)",
    "id": "Mampu memadatkan Capaian, meningkatkan Daya sebesar 210, DMG Api sebesar 700.(Maks 80 dapat digunakan)"
}

translations[chunk_2[87]] = {
    "tc": "靈級力透神丹方",
    "en": "G.Spirit Force-Penetrating Orb Recipe",
    "id": "Resep G.Roh Force-Penetrating Orb"
}

translations[chunk_2[88]] = {
    "tc": "使用後獲得靈獸：龍鹿之靈（同名靈獸只能擁有一個）",
    "en": "Use to obtain Pet: Dragon Deer Spirit (Can only possess one pet of the same name)",
    "id": "Gunakan untuk mendapatkan Peliharaan: Dragon Deer Spirit (Hanya dapat memiliki satu peliharaan dengan nama yang sama)"
}

translations[chunk_2[89]] = {
    "tc": "tap跳轉活動",
    "en": "Tap Redirect Event",
    "id": "Event Lompat Tap"
}

translations[chunk_2[90]] = {
    "tc": "<color=#ad2228>絕版招式</color>【四絕劍法】900仙玉搶購",
    "en": "<color=#ad2228>Out-of-Print Skill</color> [Four Absolutes Swordplay] Flash Sale for 900 Immortal Jade",
    "id": "<color=#ad2228>Skill Edisi Terbatas</color> [Ilmu Pedang Empat Mutlak] Beli Cepat seharga 900 Giok Abadi"
}

translations[chunk_2[91]] = {
    "tc": r"使用後可習得四絕劍法\n可在功法-招式絕學中查看已學習招式",
    "en": r"Use to learn Four Absolutes Swordplay\nView learned skills in Technique - Skill Secret",
    "id": r"Gunakan untuk mempelajari Ilmu Pedang Empat Mutlak\nDapat melihat skill yang dipelajari di Teknik - Jurus Pamungkas"
}

translations[chunk_2[92]] = {
    "tc": r"修行界初級功法需要<color=#458114>金丹</color>方可參悟\n停車坐愛楓林晚，霜葉紅於二月花。\n效果：<color=#458114>命中、閃避提升</color>",
    "en": r"Beginner cultivation technique requires <color=#458114>Gold Core</color> to comprehend\nStopping to admire the maple woods at dusk, frosty leaves are redder than spring flowers.\nEffect: <color=#458114>Hit, Dodge Increase</color>",
    "id": r"Teknik pemula dunia kultivasi membutuhkan <color=#458114>Gold Core</color> untuk dipahami\nBerhenti sejenak menikmati hutan maple di senja hari, daun berembun es lebih merah dari bunga musim semi.\nEfek: <color=#458114>Peningkatan Hit, Dodge</color>"
}

translations[chunk_2[93]] = {
    "tc": "上古大能所創造，通體晶瑩剔透，散發著柔和的光芒。修煉者只需將心神凝聚於玉盤之上，便能獲得指引和啟示，更加清晰地認識到自身修煉的現狀（無法通過尋寶獲得）",
    "en": "Created by ancient almighty beings, crystal clear throughout and emitting a gentle radiance. Cultivators need only focus their mind upon the jade plate to gain guidance and revelation, understanding their current cultivation status more clearly (Cannot be obtained via Treasure Hunt)",
    "id": "Diciptakan oleh tokoh perkasa kuno, berkilau jernih seutuhnya dan memancarkan cahaya lembut. Praktisi hanya perlu memusatkan pikiran pada piringan giok untuk memperoleh petunjuk dan pencerahan, memahami kondisi kultivasi saat ini dengan lebih jelas (Tidak dapat diperoleh melalui Berburu Harta Karun)"
}

translations[chunk_2[94]] = {
    "tc": "四季福地仙冊任務",
    "en": "Seasonal Domain Immortal Tome Quest",
    "id": "Quest Buku Abadi Seasonal Domain"
}

translations[chunk_2[95]] = {
    "tc": r"1.兩儀、三才和四象，3種祭煉方式用於提升飛舟等級，每天總共可祭煉2次\n2.祭煉方式不同，需要消耗的道具不同，獲取獎勵也有區分\n3.飛舟等級提升後，可駕馭飛舟進去更高階魔域副本\n4.飛舟達到一定等級可以領取等級獎勵，每個檔次終生只能領取一次，更換仙盟不會重置\n5.祭煉獲取道具，可用於提升仙盟技能，技能效果只在魔域生效.技能進度滿後，將會自動升級\n7.仙盟技能捐獻道具數量，達到每日上限後將不可再進行捐獻\n8.飛舟和技能養成綁定仙盟，解散後進度將會清空",
    "en": r"1. Liangyi, Sancai, and Sixiang: 3 refining methods are used to level up the Skyship, allowing 2 refines in total per day\n2. Different refining methods require different items and offer distinct rewards\n3. Increasing Skyship level allows piloting the Skyship into higher-tier Demondom dungeons\n4. Reaching certain Skyship levels unlocks level rewards, claimable only once per tier per lifetime, and not reset when changing Immortal Alliance\n5. Items gained from refining can be used to upgrade Immortal Alliance skills; skill effects are active only in Demondom. Skills auto-upgrade once progress is full\n7. Donating items for Immortal Alliance skills cannot continue once the daily limit is reached\n8. Skyship and skill growth are bound to the Immortal Alliance; progress will be cleared upon dissolution",
    "id": r"1. Liangyi, Sancai, dan Sixiang: 3 metode pemurnian digunakan untuk meningkatkan level Ark, total pemurnian 2 kali per hari\n2. Metode pemurnian yang berbeda membutuhkan item yang berbeda dan memberikan hadiah yang berbeda pula\n3. Setelah level Ark ditingkatkan, Ark dapat dikemudikan untuk memasuki dungeon Demondom tingkat lebih tinggi\n4. Mencapai level Ark tertentu dapat mengklaim hadiah level, setiap tingkatan hanya dapat diklaim sekali seumur hidup dan tidak akan direset saat berganti Klan\n5. Item yang diperoleh dari pemurnian dapat digunakan untuk meningkatkan skill Klan, efek skill hanya berlaku di Demondom. Skill akan otomatis naik level setelah progres penuh\n7. Jumlah donasi item skill Klan tidak dapat dilakukan lagi setelah mencapai batas harian\n8. Pengembangan Ark dan skill terikat dengan Klan, progres akan dihapus jika Klan dibubarkan"
}

translations[chunk_2[96]] = {
    "tc": "此身轉戰三千里，劍試天下無人敵",
    "en": "Battling across three thousand miles, testing the sword with no equal under heaven",
    "id": "Bertempur mengarungi tiga ribu li, menguji pedang tanpa tandingan di kolong langit"
}

translations[chunk_2[97]] = {
    "tc": "七夕今宵看碧霄，牽牛織女渡河橋 ",
    "en": "Gazing at the azure sky on Qixi night, Cowherd and Weaver Maid cross the bridge of stars ",
    "id": "Menatap langit biru di malam Qixi, Penggembala Sapi dan Gadis Penenun menyeberangi jembatan sungai "
}

translations[chunk_2[98]] = {
    "tc": "隨機秘寶碎片-藍色",
    "en": "Random Secret Treasure Shard - Blue",
    "id": "Fragmen Harta Rahasia Acak - Biru"
}

translations[chunk_2[99]] = {
    "tc": r"“論道大會”第三名頭像框\n（下賽季開啟後回收）",
    "en": r'"Debate Assembly" 3rd Place Profile Frame\n(Reclaimed after the next season begins)',
    "id": r'Bingkai Profil Juara 3 "Konferensi Debat"\n(Ditarik setelah musim berikutnya dibuka)'
}

translations[chunk_2[100]] = {
    "tc": r"“論道大會”第一名頭像框\n（下賽季開啟後回收）",
    "en": r'"Debate Assembly" 1st Place Profile Frame\n(Reclaimed after the next season begins)',
    "id": r'Bingkai Profil Juara 1 "Konferensi Debat"\n(Ditarik setelah musim berikutnya dibuka)'
}

translations[chunk_2[101]] = {
    "tc": "機緣怪物品質5",
    "en": "Fortune Monster Quality 5",
    "id": "Kualitas Monster Peluang 5"
}

translations[chunk_2[102]] = {
    "tc": r"名稱：道場守衛\n修為：玄仙八階\n修煉：1324年",
    "en": r"Name：Dojo Guard\nAttainment：Mythic Deity G.8\nPracticing：1324 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Dewa Mistikal G.8\nLatihan：1324 tahun"
}

translations[chunk_2[103]] = {
    "tc": "靈級水生神丹方",
    "en": "G.Spirit Water-Born Orb Recipe",
    "id": "Resep G.Roh Water-Born Orb"
}

translations[chunk_2[104]] = {
    "tc": "精英魔物·攻",
    "en": "Elite Demon · ATK",
    "id": "Monster Iblis Elit · ATK"
}

translations[chunk_2[105]] = {
    "tc": "使用後將“天人合一”稱號加入衣閣。",
    "en": 'Use to add the "Unity of Man and Nature" title to the Closet.',
    "id": 'Gunakan untuk menambahkan gelar "Kesatuan Manusia dan Alam" ke Lemari.'
}

translations[chunk_2[106]] = {
    "tc": r"名稱：道場守衛\n修為：天仙六階\n修煉：1247年",
    "en": r"Name：Dojo Guard\nAttainment：Heaven Deity G.6\nPracticing：1247 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Dewa Surgawi G.6\nLatihan：1247 tahun"
}

translations[chunk_2[107]] = {
    "tc": "否取消參悟",
    "en": "Cancel Comprehension",
    "id": "Batalkan Pemahaman"
}

translations[chunk_2[108]] = {
    "tc": r"名稱：道場守衛\n修為：煉虛六階\n修煉：1247年",
    "en": r"Name：Dojo Guard\nAttainment：Vainify G.6\nPracticing：1247 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Merusak G.6\nLatihan：1247 tahun"
}

translations[chunk_2[109]] = {
    "tc": "【四季福地】",
    "en": "[Seasonal Domain]",
    "id": "[Seasonal Domain]"
}

translations[chunk_2[110]] = {
    "tc": r"名稱：道場守衛\n修為：真仙五階\n修煉：1347年",
    "en": r"Name：Dojo Guard\nAttainment：Deity G.5\nPracticing：1347 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Dewa G.5\nLatihan：1347 tahun"
}

translations[chunk_2[111]] = {
    "tc": "距離下次：%s",
    "en": "Until next: %s",
    "id": "Menuju berikutnya: %s"
}

translations[chunk_2[112]] = {
    "tc": r"1、三階滿級招式開啟<color=#9e4444>招式參悟</color>\n2、道友可消耗參悟道具<color=#9e4444>刷新</color>出新的詞條、提升當前招式的屬性效果。\n3、刷新出紅色詞條後，相同位置下次刷新出紅色品質詞條的效果會更高（不會超過上限值）\n4、參悟需要消耗基礎道具和額外消耗道具，請道友仔細查看資源儲備情況～\n【參悟聖焰】刷新招式屬性詞條概率：\n綠色：<color=#008000>73.8%</color>        藍色：<color=#0000FF>20.5%</color>\n紫色：<color=#9400D3>4.2%</color>         橙色：<color=#FF8C00>1%</color>\n紅色：<color=#FF0000>0.5%</color>\n【參悟神焰】刷新招式屬性詞條概率：\n綠色：<color=#008000>44.6%</color>        藍色：<color=#0000FF>37.5%</color>\n紫色：<color=#9400D3>13.4%</color>         橙色：<color=#FF8C00>2.7%</color>\n紅色：<color=#FF0000>1.8%</color>\n4、使用<color=#9e4444>明悟砂可以鎖定</color>當前詞條不被刷新。（最多同時鎖定<color=#9e4444>4個</color>詞條，且鎖定詞條越多、明悟砂的消耗越多）\n5、詞條被替換時會有提示，默認勾選紫品質有提示，道友可自行更換或不選。\n6、若道友<color=#9e4444>遺忘三階招式，將不會返回參悟功能</color>的培養道具！請道友注意～",
    "en": r"1. Tier 3 max-level skills unlock <color=#9e4444>Skill Comprehension</color>\n2. Cultivators can consume comprehension items to <color=#9e4444>refresh</color> new affixes and enhance current skill attribute effects.\n3. After rolling a red affix, the effect of red-quality affixes rolled in the same slot next time will be higher (will not exceed max limit)\n4. Comprehension requires basic and extra consumable items, please check your resource reserves carefully~\n[Flame of Epiphany] Skill attribute affix refresh rates:\nGreen: <color=#008000>73.8%</color>        Blue: <color=#0000FF>20.5%</color>\nPurple: <color=#9400D3>4.2%</color>         Orange: <color=#FF8C00>1%</color>\nRed: <color=#FF0000>0.5%</color>\n[Flame of Inspiration] Skill attribute affix refresh rates:\nGreen: <color=#008000>44.6%</color>        Blue: <color=#0000FF>37.5%</color>\nPurple: <color=#9400D3>13.4%</color>         Orange: <color=#FF8C00>2.7%</color>\nRed: <color=#FF0000>1.8%</color>\n4. Using <color=#9e4444>Sand of Enlightenment can lock</color> current affixes from being refreshed. (Can lock up to <color=#9e4444>4</color> affixes simultaneously; locking more affixes increases Sand of Enlightenment cost)\n5. Prompts appear when replacing affixes; prompt on purple quality is enabled by default, which can be modified or disabled.\n6. If you <color=#9e4444>forget a Tier 3 skill, cultivation items from Comprehension will NOT be returned</color>! Please be careful~",
    "id": r"1. Skill Tingkat 3 level maksimal membuka <color=#9e4444>Pemahaman Skill</color>\n2. Rekan Taois dapat mengonsumsi item pemahaman untuk <color=#9e4444>menyegarkan</color> atribut baru dan meningkatkan efek atribut skill saat ini.\n3. Setelah menyegarkan atribut merah, efek atribut kualitas merah yang disegarkan berikutnya pada posisi yang sama akan lebih tinggi (tidak melebihi batas maksimal)\n4. Pemahaman membutuhkan item dasar dan item konsumsi tambahan, silakan periksa cadangan sumber daya dengan cermat~\n[Api Epiphany] Peluang menyegarkan atribut skill:\nHijau: <color=#008000>73.8%</color>        Biru: <color=#0000FF>20.5%</color>\nUngu: <color=#9400D3>4.2%</color>         Oranye: <color=#FF8C00>1%</color>\nMerah: <color=#FF0000>0.5%</color>\n[Api Inspirasi] Peluang menyegarkan atribut skill:\nHijau: <color=#008000>44.6%</color>        Biru: <color=#0000FF>37.5%</color>\nUngu: <color=#9400D3>13.4%</color>         Oranye: <color=#FF8C00>2.7%</color>\nMerah: <color=#FF0000>1.8%</color>\n4. Menggunakan <color=#9e4444>Pasir Pencerahan dapat mengunci</color> atribut saat ini agar tidak disegarkan. (Maksimal mengunci <color=#9e4444>4</color> atribut sekaligus; semakin banyak atribut terkunci, semakin banyak Pasir Pencerahan yang digunakan)\n5. Pengingat akan muncul saat atribut diganti; pengingat kualitas ungu dicentang secara default, Rekan Taois dapat mengubah atau tidak memilihnya.\n6. Jika Rekan Taois <color=#9e4444>melupakan skill Tingkat 3, item pelatihan fitur Pemahaman TIDAK akan dikembalikan</color>! Harap berhati-hati~"
}

translations[chunk_2[113]] = {
    "tc": r"名稱：道場守衛\n修為：大羅金仙一階\n修煉：1754年",
    "en": r"Name：Dojo Guard\nAttainment：Daluo G.1\nPracticing：1754 years",
    "id": r"Nama：Penjaga Dojo\nCapaian：Daluo G.1\nLatihan：1754 tahun"
}

translations[chunk_2[114]] = {
    "tc": "是否確認轉化",
    "en": "Confirm conversion?",
    "id": "Apakah konfirmasi konversi?"
}

print(f"Total keys translated: {len(translations)}")
assert len(translations) == len(chunk_2), f"Expected {len(chunk_2)}, got {len(translations)}"

# Validation logic
errors = []

for idx, orig in enumerate(chunk_2):
    if orig not in translations:
        errors.append(f"Missing key: {orig}")
        continue
    item = translations[orig]
    for lang in ['tc', 'en', 'id']:
        if lang not in item:
            errors.append(f"Missing lang {lang} in {orig}")
            continue
        text = item[lang]
        
        # 1. Placeholders
        orig_placeholders = re.findall(r'%[0-9]*[a-zA-Z%]', orig)
        text_placeholders = re.findall(r'%[0-9]*[a-zA-Z%]', text)
        if sorted(orig_placeholders) != sorted(text_placeholders):
            errors.append(f"[{lang}] Placeholder mismatch in #{idx}: orig={orig_placeholders}, trans={text_placeholders}")
            
        # 2. Color tags
        orig_colors_open = re.findall(r'<color=#[0-9a-fA-F]{6}>', orig)
        text_colors_open = re.findall(r'<color=#[0-9a-fA-F]{6}>', text)
        if orig_colors_open != text_colors_open:
            errors.append(f"[{lang}] Color open tag mismatch in #{idx}: orig={orig_colors_open}, trans={text_colors_open}")
            
        orig_colors_close = re.findall(r'</color>', orig)
        text_colors_close = re.findall(r'</color>', text)
        if len(orig_colors_close) != len(text_colors_close):
            errors.append(f"[{lang}] Color close tag count mismatch in #{idx}")
            
        # 3. Literal \n count
        orig_nl = orig.count(r'\n')
        text_nl = text.count(r'\n')
        if orig_nl != text_nl:
            errors.append(f"[{lang}] Literal \\n count mismatch in #{idx}: orig={orig_nl}, trans={text_nl}")

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for err in errors[:20]:
        print(" ", err)
else:
    print("ALL VALIDATION CHECKS PASSED PERFECTLY!")
    out_path = r'F:\项目\无极国际版\result_chunk_2.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)
    print(f"Saved successfully to {out_path}!")
