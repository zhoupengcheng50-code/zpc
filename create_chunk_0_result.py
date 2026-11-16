# -*- coding: utf-8 -*-
import json
import re

# Load source chunk_0.json
with open('chunk_0.json', 'r', encoding='utf-8') as f:
    chunk_0 = json.load(f)

# Define translations for all 115 items
# Structure: index -> (tc, en, id)
translations = {}

# 0
translations[0] = {
    "tc": "使用後習得靈級焚天神丹的煉製之法。（天品煉丹師方可使用）\\n焚天神丹服用後提升身法和火系傷害。",
    "en": "Use to learn the refining method of G.Spirit Burning Heaven Orb.(Usable by G.Heaven Alchemist)\\nBurning Heaven Orb could use to improve Agility and Fire DMG.",
    "id": "Gunakan untuk mempelajari metode pemurnian G.Roh Burning Heaven Orb.(Dapat digunakan oleh G.Surga Alkimis)\\nBurning Heaven Orb dapat digunakan untuk meningkatkan Kelincahan dan DMG Api."
}

# 1
translations[1] = {
    "tc": "使用後可隨機獲得一本殘冬功法。",
    "en": "Use to randomly obtain a Waning Winter Technique.",
    "id": "Gunakan untuk memperoleh satu Teknik Waning Winter secara acak."
}

# 2
translations[2] = {
    "tc": "名稱：道場守衛\\n修為：仙帝一階\\n修煉：1754年",
    "en": "Name: Dojo Guard\\nAttainment: Deity Emperor G.1\\nPracticing: 1754 years",
    "id": "Nama: Penjaga Dojo\\nCapaian: Kaisar Dewa G.1\\nLatihan: 1754 tahun"
}

# 3
translations[3] = {
    "tc": "飛泉鳴玉",
    "en": "Spring Singing Jade",
    "id": "Mata Air Bernyanyi Giok"
}

# 4
translations[4] = {
    "tc": "<color=#ad2228>本次領悟可獲得：%s</color>",
    "en": "<color=#ad2228>Current comprehension can obtain: %s</color>",
    "id": "<color=#ad2228>Pemahaman saat ini dapat memperoleh: %s</color>"
}

# 5
translations[5] = {
    "tc": "三階靈獸招式參悟專屬道具之一，使用該道具參悟",
    "en": "One of the exclusive items for G.3 Pet Skill comprehension, use this item to comprehend",
    "id": "Salah satu item eksklusif untuk pemahaman Jurus Peliharaan G.3, gunakan item ini untuk memahami"
}

# 6
translations[6] = {
    "tc": "3、立即獲取200",
    "en": "3. Instantly obtain 200",
    "id": "3. Dapatkan 200 secara instan"
}

# 7
translations[7] = {
    "tc": "1、獲得裝備、學習功法、獲取衣閣裝飾、結識道侶、煉製法寶、使用寵物蛋、收集宗門秘寶等遊戲行為，均可激活對應圖鑒\\n2、特定圖鑒組合可激活羈絆屬性，羈絆屬性永久生效。\\n3、並不是所有上述類型內的所有物品都被收納進圖鑒。\\n4、法寶的屬性有隨機波動成分，所以並不會和圖鑒內顯示的完全一致。",
    "en": "1. In-game actions such as obtaining equipment, learning Techniques, acquiring Closet decorations, meeting Companions, refining Artifacts, using pet eggs, and collecting Sect secret treasures can activate corresponding Codices.\\n2. Specific Codex combinations can activate Bond attributes, which take effect permanently.\\n3. Not all items within the aforementioned types are included in the Codex.\\n4. Artifact attributes contain random variations, so they will not be entirely identical to those displayed in the Codex.",
    "id": "1. Tindakan dalam game seperti memperoleh perlengkapan, mempelajari Teknik, mendapatkan dekorasi Lemari Pakaian, mengenal Pendamping, memurnikan Artefak, menggunakan telur peliharaan, dan mengumpulkan harta rahasia Sekte dapat mengaktifkan Kodeks terkait.\\n2. Kombinasi Kodeks tertentu dapat mengaktifkan atribut Ikatan, yang berlaku secara permanen.\\n3. Tidak semua item dalam jenis-jenis di atas dimasukkan ke dalam Kodeks.\\n4. Atribut Artefak memiliki komponen fluktuasi acak, sehingga tidak akan sepenuhnya sama dengan yang ditampilkan di Kodeks."
}

# 8
translations[8] = {
    "tc": "靈獸功法等級未滿",
    "en": "Pet Technique level is not maxed",
    "id": "Level Teknik Peliharaan belum penuh"
}

# 9
translations[9] = {
    "tc": "該道友沒有配備招式",
    "en": "This Taoist friend has no skills equipped",
    "id": "Rekan kultivator ini belum melengkapi jurus"
}

# 10
translations[10] = {
    "tc": "龍鹿之靈",
    "en": "Dragon Deer Spirit",
    "id": "Roh Rusa Naga"
}

# 11
translations[11] = {
    "tc": "伏暑妙法",
    "en": "Summer Quell Secret Technique",
    "id": "Teknik Rahasia Meredam Musim Panas"
}

# 12
translations[12] = {
    "tc": "隨機靈獸蛋-秋",
    "en": "Random Pet Egg - Autumn",
    "id": "Telur Peliharaan Acak - Musim Gugur"
}

# 13
translations[13] = {
    "tc": "名稱：道場守衛\\n修為：大乘九階\\n修煉：1746年",
    "en": "Name: Dojo Guard\\nAttainment: Mahayana G.9\\nPracticing: 1746 years",
    "id": "Nama: Penjaga Dojo\\nCapaian: Mahayana G.9\\nLatihan: 1746 tahun"
}

# 14
translations[14] = {
    "tc": "使用後習得靈級樹魄神丹的煉製之法。（天品煉丹師方可使用）\\n樹魄神丹服用後提升體魄和木系傷害。",
    "en": "Use to learn the refining method of G.Spirit Tree Soul Orb.(Usable by G.Heaven Alchemist)\\nTree Soul Orb could use to improve Health and Wood DMG.",
    "id": "Gunakan untuk mempelajari metode pemurnian G.Roh Tree Soul Orb.(Dapat digunakan oleh G.Surga Alkimis)\\nTree Soul Orb dapat digunakan untuk meningkatkan Kesehatan dan DMG Kayu."
}

# 15
translations[15] = {
    "tc": "領取成功",
    "en": "Claimed successfully",
    "id": "Berhasil diklaim"
}

# 16
translations[16] = {
    "tc": "游仙限時禮包",
    "en": "Wanderer Limited Giftpack",
    "id": "Paket Hadiah Terbatas Tualang"
}

# 17
translations[17] = {
    "tc": "收集[東橋姑娘信箋]",
    "en": "Collect [Miss Dong Qiao's Letter]",
    "id": "Kumpulkan [Surat Nona Dong Qiao]"
}

# 18
translations[18] = {
    "tc": "青城鎮派絕學，內含春夏秋冬，威力係數：%s，傷害加成：真氣*%s、根骨*%s、體魄*%s、身法*%s",
    "en": "Qingcheng ultimate sect technique, containing Spring, Summer, Autumn and Winter. Power level: %s, DMG buff: Qi*%s, Strength*%s, Health*%s, Agility*%s",
    "id": "Jurus sekte pamungkas Qingcheng, memuat musim semi, panas, gugur, dan dingin. Level kekuatan: %s, DMG buff: Qi*%s, Daya*%s, Kesehatan*%s, Kelincahan*%s"
}

# 19
translations[19] = {
    "tc": "是否遺忘%s，遺忘後將返還70%%升級消耗材料。（遺忘技能不返還三階招式參悟的消耗材料，請道友謹慎操作～）",
    "en": "Whether to forget %s? 70%% of upgrade materials will be refunded after forgetting. (Forgetting skills will not refund materials consumed for G.3 Skill comprehension, please operate with caution~)",
    "id": "Apakah ingin melupakan %s? 70%% material konsumsi peningkatan akan dikembalikan setelah dilupakan. (Melupakan skill tidak mengembalikan material konsumsi pemahaman Jurus G.3, harap berhati-hati dalam beroperasi~)"
}

# 20
translations[20] = {
    "tc": "受到傷害後，恢復五行傷害總值%s生命值，持續31回合",
    "en": "After taking DMG, restore HP equal to %s of total Five Elements DMG, lasting 31 rounds",
    "id": "Setelah menerima DMG, pulihkan HP sebesar %s dari total DMG Lima Elemen, berlangsung selama 31 ronde"
}

# 21
translations[21] = {
    "tc": "隨機靈獸蛋-夏",
    "en": "Random Pet Egg - Summer",
    "id": "Telur Peliharaan Acak - Musim Panas"
}

# 22
translations[22] = {
    "tc": "名稱：道場守衛\\n修為：大乘三階\\n修煉：1754年",
    "en": "Name: Dojo Guard\\nAttainment: Mahayana G.3\\nPracticing: 1754 years",
    "id": "Nama: Penjaga Dojo\\nCapaian: Mahayana G.3\\nLatihan: 1754 tahun"
}

# 23
translations[23] = {
    "tc": "洞窟魔物·療",
    "en": "Cave Monster · Heal",
    "id": "Monster Gua · Pulih"
}

# 24
translations[24] = {
    "tc": "防守：%m/%d %X",
    "en": "Defense: %m/%d %X",
    "id": "Pertahanan: %m/%d %X"
}

# 25
translations[25] = {
    "tc": "服用後凝練修士修為，增加210身法、700點土系傷害。（最多服用80個）",
    "en": "Able to condense cultivator's Attainment, increase Agility by 210 and Earth DMG by 700.(Max 80 can be used)",
    "id": "Dapat memadatkan Capaian kultivator, meningkatkan Kelincahan sebesar 210 dan DMG Bumi sebesar 700.(Maksimal 80 dapat digunakan)"
}

# 26
translations[26] = {
    "tc": "名稱：道場守衛\\n修為：大乘七階\\n修煉：1964年",
    "en": "Name: Dojo Guard\\nAttainment: Mahayana G.7\\nPracticing: 1964 years",
    "id": "Nama: Penjaga Dojo\\nCapaian: Mahayana G.7\\nLatihan: 1964 tahun"
}

# 27
translations[27] = {
    "tc": "本次更換將重新選擇獎池全部獎勵，已選擇的限定次數獎勵將返還次數，是否確認？",
    "en": "This replacement will reselect all rewards in the prize pool, and selected limited-time rewards will have their attempts refunded. Confirm?",
    "id": "Penggantian ini akan memilih ulang semua hadiah di kumpulan hadiah, dan hadiah batas frekuensi yang telah dipilih akan mengembalikan jumlahnya. Konfirmasi?"
}

# 28
translations[28] = {
    "tc": "靈級紫陽神丹方",
    "en": "G.Spirit Ziyang Orb Recipe",
    "id": "Resep G.Roh Ziyang Orb"
}

# 29
translations[29] = {
    "tc": "使用後將“天下無敵”頭像框加入衣閣。\\n（<color=#458114>“論道大會”限時外觀，下個賽季前回收</color>）",
    "en": "Use to add \"Invincible\" Profile Photo into Closet.\\n(<color=#458114>\"Theory Assembly\" limited appearance, reclaimed before next season</color>)",
    "id": "Gunakan untuk menambahkan Bingkai Avatar \"Tak Terkalahkan\" ke Lemari Pakaian.\\n(<color=#458114>Tampilan terbatas \"Pertemuan Teori\", ditarik kembali sebelum musim berikutnya</color>)"
}

# 30
translations[30] = {
    "tc": "論道大會",
    "en": "Theory Assembly",
    "id": "Pertemuan Teori"
}

# 31
translations[31] = {
    "tc": "靈獸蛋·龍鹿之靈",
    "en": "Pet Egg · Dragon Deer Spirit",
    "id": "Telur Peliharaan · Roh Rusa Naga"
}

# 32
translations[32] = {
    "tc": "使用後習得靈級明悟神丹的煉製之法。（天品煉丹師方可使用）\\n明悟神丹服用後提升體魄和金系傷害。",
    "en": "Use to learn the refining method of G.Spirit Enlightenment Orb.(Usable by G.Heaven Alchemist)\\nEnlightenment Orb could use to improve Health and Metal DMG.",
    "id": "Gunakan untuk mempelajari metode pemurnian G.Roh Enlightenment Orb.(Dapat digunakan oleh G.Surga Alkimis)\\nEnlightenment Orb dapat digunakan untuk meningkatkan Kesehatan dan DMG Logam."
}

# 33
translations[33] = {
    "tc": "收集[蕭雲信箋]",
    "en": "Collect [Xiao Yun's Letter]",
    "id": "Kumpulkan [Surat Xiao Yun]"
}

# 34
translations[34] = {
    "tc": "真仙限時禮包",
    "en": "Deity Limited Giftpack",
    "id": "Paket Hadiah Terbatas Dewa"
}

# 35
translations[35] = {
    "tc": "靈級凝土神丹方",
    "en": "G.Spirit Soil-Focusing Orb Recipe",
    "id": "Resep G.Roh Soil-Focusing Orb"
}

# 36
translations[36] = {
    "tc": "我在年紀尚幼時就加入了黃風谷，一切都是家裏安排妥當的，水到渠成的。我所發揮的作用，不過是讓師長知道有我這麼個人存在罷了，至於其他的，都不是我能做主的……原本以為自己的修行生活會在平淡無奇中渡過，但卻沒想到，宗門卻安排我與一名陸姓師兄互相結識。師長們是希望我答應這一樁姻緣，促成美談。我從小個性溫馴，只知道聽從師長們的安排，不敢做任何違逆。也許我本質上就是這樣一個……木偶般孑然的人吧。",
    "en": "I joined Yellow Wind Valley when I was still very young. Everything was well arranged by my family, naturally falling into place. My role was merely to let my masters and elders know that someone like me existed; as for anything else, none of it was mine to decide... I originally thought my cultivation life would pass in quiet obscurity, but unexpectedly, the Sect arranged for me to meet a senior brother surnamed Lu. The masters hoped I would agree to this marriage and create a delightful tale. Since childhood, I was meek by nature, knowing only to obey the arrangements of my elders, never daring to disobey in the slightest. Perhaps in essence, I am just such a solitary, puppet-like person.",
    "id": "Saya bergabung dengan Lembah Angin Kuning ketika masih sangat muda. Semuanya telah diatur rapi oleh keluarga saya, berjalan begitu saja tanpa hambatan. Peran saya hanyalah membuat para guru dan tetua tahu bahwa sosok seperti saya ada; selebihnya, tidak ada yang bisa saya putuskan sendiri... Semula saya mengira kehidupan kultivasi saya akan berlalu dengan tenang tanpa riak, namun tak disangka, Sekte mengatur agar saya berkenalan dengan seorang kakak seperguruan bermarga Lu. Para tetua berharap saya menyetujui perjodohan ini demi menciptakan kisah yang indah. Sejak kecil watak saya penurut, hanya tahu menuruti pengaturan tetua, tak berani membantah sedikit pun. Mungkin pada hakikatnya, saya hanyalah orang yang kesepian... layaknya boneka kayu."
}

# 37
translations[37] = {
    "tc": "不在可挑戰時間內",
    "en": "Not within challenge time",
    "id": "Bukan dalam waktu tantangan"
}

# 38
translations[38] = {
    "tc": "活動道具，使用後可以增加1次機緣次數，額外機緣次數會隨著每日刷新清空，請即時使用。\\n使用途徑：四季福地",
    "en": "Event item. Use to increase Fortuity attempts by 1. Extra Fortuity attempts will be cleared upon daily refresh, please use promptly.\\nUsage Method: Seasonal Domain",
    "id": "Item event. Gunakan untuk menambah 1 kali kesempatan Keberuntungan. Kesempatan Keberuntungan ekstra akan dikosongkan bersama pembaruan harian, harap gunakan segera.\\nCara Penggunaan: Domain Musiman"
}

# 39
translations[39] = {
    "tc": "背包空間不足，獎勵以郵件形式發放，請注意查收",
    "en": "Insufficient backpack space, rewards are sent via mail, please check",
    "id": "Ruang ransel tidak cukup, hadiah dikirim melalui surat, silakan periksa"
}

# 40
translations[40] = {
    "tc": "靈獸蛋·冰眸寒魄",
    "en": "Pet Egg · Glacial Frostsoul",
    "id": "Telur Peliharaan · Glacial Frostsoul"
}

# 41
translations[41] = {
    "tc": "最近5位通關的道友：",
    "en": "Recent 5 Taoist friends who cleared:",
    "id": "5 rekan kultivator terakhir yang lolos:"
}

# 42
translations[42] = {
    "tc": "不知何時被封存的靈寶，已經化為了琥珀一樣的礦石，小心打開後90%概率獲得隨機1至3個靈寶碎片，10%概率隨機獲得1個完整的靈寶。",
    "en": "A treasure sealed at an unknown time, already turned into an amber-like ore. Carefully opening it grants a 90% chance to randomly obtain 1 to 3 Treasure Shards, and a 10% chance to randomly obtain 1 complete Treasure.",
    "id": "Harta pusaka yang disegel entah sejak kapan, telah berubah menjadi bijih seperti batu ambar. Membukanya dengan hati-hati memberikan peluang 90% untuk memperoleh 1 hingga 3 Pecahan Pusaka secara acak, dan peluang 10% untuk memperoleh 1 Pusaka utuh secara acak."
}

# 43
translations[43] = {
    "tc": "鎮派法寶：%s",
    "en": "Zhenpai Artifact: %s",
    "id": "Artefak Zhenpai: %s"
}

# 44
translations[44] = {
    "tc": "上古龍神，又名燭九陰，神通廣大，開眼為晝、閉眼為夜，呼吸之間可致天時變換，冬夏交替。",
    "en": "Ancient dragon god, also known as Zhu Jiuyin, possesses boundless divine powers. Opening eyes brings day and closing eyes brings night; in a breath, it causes weather changes and alters winter and summer.",
    "id": "Dewa naga kuno, juga dikenal sebagai Zhu Jiuyin, memiliki kekuatan ilahi yang sangat dahsyat. Membuka mata menjadi siang dan menutup mata menjadi malam; dalam hembusan napasnya dapat mengubah cuaca dan pergantian musim dingin serta panas."
}

# 45
translations[45] = {
    "tc": "靈級地藏神丹",
    "en": "G.Spirit Ksitigarbha Orb",
    "id": "G.Roh Ksitigarbha Orb"
}

# 46
translations[46] = {
    "tc": "洞窟魔物·攻",
    "en": "Cave Monster · ATK",
    "id": "Monster Gua · Serang"
}

# 47
translations[47] = {
    "tc": "<color=#ad2228>本次參悟可獲得：%s</color>",
    "en": "<color=#ad2228>Current comprehension can obtain: %s</color>",
    "id": "<color=#ad2228>Pemahaman saat ini dapat memperoleh: %s</color>"
}

# 48
translations[48] = {
    "tc": "靈獸養成禮包",
    "en": "Pet Training Giftpack",
    "id": "Paket Hadiah Pelatihan Peliharaan"
}

# 49
translations[49] = {
    "tc": "名稱：道場守衛\\n修為：玄仙二階\\n修煉：1124年",
    "en": "Name: Dojo Guard\\nAttainment: Mythic Deity G.2\\nPracticing: 1124 years",
    "id": "Nama: Penjaga Dojo\\nCapaian: Dewa Mistikal G.2\\nLatihan: 1124 tahun"
}

# 50
translations[50] = {
    "tc": "機緣怪物品質4",
    "en": "Fortuity Monster Quality 4",
    "id": "Kualitas Monster Keberuntungan 4"
}

# 51
translations[51] = {
    "tc": "服用後凝練修士修為，增加210體魄、700點火系傷害。（最多服用80個）",
    "en": "Able to condense cultivator's Attainment, increase Health by 210 and Fire DMG by 700.(Max 80 can be used)",
    "id": "Dapat memadatkan Capaian kultivator, meningkatkan Kesehatan sebesar 210 dan DMG Api sebesar 700.(Maksimal 80 dapat digunakan)"
}

# 52
translations[52] = {
    "tc": "隨機秘寶碎片-紫色",
    "en": "Random Secret Treasure Shard - Purple",
    "id": "Pecahan Harta Karun Rahasia Acak - Ungu"
}

# 53
translations[53] = {
    "tc": "稀有寶物",
    "en": "Rare Treasure",
    "id": "Harta Langka"
}

# 54
translations[54] = {
    "tc": "名稱：道場守衛\\n修為：分神一階\\n修煉：750年",
    "en": "Name: Dojo Guard\\nAttainment: Severance G.1\\nPracticing: 750 years",
    "id": "Nama: Penjaga Dojo\\nCapaian: Sengsara G.1\\nLatihan: 750 tahun"
}

# 55
translations[55] = {
    "tc": "是否取消替換",
    "en": "Cancel replacement?",
    "id": "Batalkan penggantian?"
}

# 56
translations[56] = {
    "tc": "每日訪問論壇，領取超值福利",
    "en": "Visit forum daily to claim great benefits",
    "id": "Kunjungi forum setiap hari untuk mengklaim keuntungan bernilai tinggi"
}

# 57
translations[57] = {
    "tc": "是否花費<color=#9e4444>%s</color>仙玉增加<color=#9e4444>%s</color>洞窟體力?",
    "en": "Spend <color=#9e4444>%s</color> Immortal Jade to increase <color=#9e4444>%s</color> Cave Stamina?",
    "id": "Apakah ingin menghabiskan <color=#9e4444>%s</color> Giok Abadi untuk menambah <color=#9e4444>%s</color> Stamina Gua?"
}

# 58
translations[58] = {
    "tc": "鎖定數量已達上限",
    "en": "Locked quantity has reached the limit",
    "id": "Jumlah yang dikunci telah mencapai batas maksimal"
}

# 59
translations[59] = {
    "tc": "祝賀道友本賽季論道大會榮譽上榜，位列第三，名傳三界，威名赫赫。",
    "en": "Congratulations to fellow Taoist for earning an honorable place in this season's Theory Assembly, ranking 3rd, renowned throughout the Three Realms with illustrious prestige!",
    "id": "Selamat kepada rekan kultivator atas kehormatan masuk peringkat Pertemuan Teori musim ini, menempati posisi ke-3, tersohor di Tiga Alam dengan reputasi termasyhur!"
}

# 60
translations[60] = {
    "tc": "名稱：道場守衛\\n修為：天仙八階\\n修煉：1324年",
    "en": "Name: Dojo Guard\\nAttainment: Heaven Deity G.8\\nPracticing: 1324 years",
    "id": "Nama: Penjaga Dojo\\nCapaian: Dewa Surgawi G.8\\nLatihan: 1324 tahun"
}

# 61
translations[61] = {
    "tc": "紅楓天書",
    "en": "Red Maple Heavenly Tome",
    "id": "Kitab Surgawi Red Maple"
}

# 62
translations[62] = {
    "tc": "探路嘍囉·甲",
    "en": "Pathfinding Minion · First",
    "id": "Kroco Penjelajah · Satu"
}

# 63
translations[63] = {
    "tc": "2、機緣獲取經驗提升+%s%%",
    "en": "2. Fortuity EXP gain increased +%s%%",
    "id": "2. Perolehan EXP Keberuntungan meningkat +%s%%"
}

# 64
translations[64] = {
    "tc": "隨機魂力",
    "en": "Random Soul Energy",
    "id": "Energi Jiwa Acak"
}

# 65
translations[65] = {
    "tc": "四季福玉不足",
    "en": "Insufficient Seasonal Jade",
    "id": "Giok Musiman tidak cukup"
}

# 66
translations[66] = {
    "tc": "重選血脈",
    "en": "Reselect Bloodline",
    "id": "Pilih Ulang Garis Keturunan"
}

# 67
translations[67] = {
    "tc": "1、福地洞窟每個季度棲息著不同的怪物，擊敗一定數量的怪物可以領取豐厚獎勵\\n2、擊敗怪物不消耗體力，未擊敗時消耗體力，可通過仙玉購買體力\\n3、每隔一定層數會隨機刷新相同的一條後天魂力，怪物和弟子均獲得加成效果",
    "en": "1. Different monsters inhabit the Blessed Land Cave each season, and defeating a certain number of monsters allows claiming generous rewards.\\n2. Defeating monsters does not consume Stamina; Stamina is only consumed when failing to defeat them, and Stamina can be purchased with Immortal Jade.\\n3. Every few floors, the same Postnatal Primary Power will randomly refresh, granting bonus effects to both monsters and disciples.",
    "id": "1. Monster yang berbeda menghuni Gua Tanah Berkah setiap musim, dan mengalahkan sejumlah monster dapat mengklaim hadiah berlimpah.\\n2. Mengalahkan monster tidak menghabiskan Stamina; Stamina hanya dihabiskan jika gagal mengalahkan, dan Stamina dapat dibeli menggunakan Giok Abadi.\\n3. Setiap beberapa lantai, Atribut Tambahan Energi Jiwa yang sama akan diperbarui secara acak, memberikan efek bonus kepada monster dan murid."
}

# 68
translations[68] = {
    "tc": "風情月意",
    "en": "Breeze and Moon Charm",
    "id": "Pesona Angin dan Bulan"
}

# 69
translations[69] = {
    "tc": "伏暑神術",
    "en": "Summer Quell Divine Spell",
    "id": "Mantra Ilahi Meredam Musim Panas"
}

# 70
translations[70] = {
    "tc": "1.天命法則彙總顯示各功能提供的戰鬥觸發被動效果\\n2.彙總功能包含：心魔命格、元神劍胎、無極宮、以力證道、聖軀套裝、藏寶閣",
    "en": "1. The Destined Rules summary displays combat-triggered passive effects provided by each function.\\n2. Summary functions include: Inner Demon Fate, Essence Soul Sword Fetus, Infinite Palace, Power Saint, Sage Trunk Suit, Treasure Pavilion.",
    "id": "1. Rangkuman Aturan yang Ditakdirkan menampilkan efek pasif pemicu pertempuran yang diberikan oleh setiap fungsi.\\n2. Fungsi ringkasan mencakup: Titik Takdir Batin Iblis, Janin Pedang Jiwa Esensi, Istana Maha, Power Saint, Setelan Batang Sage, Paviliun Harta."
}

# 71
translations[71] = {
    "tc": "名稱：道場守衛\\n修為：煉虛四階\\n修煉：1324年",
    "en": "Name: Dojo Guard\\nAttainment: Vainify G.4\\nPracticing: 1324 years",
    "id": "Nama: Penjaga Dojo\\nCapaian: Merusak G.4\\nLatihan: 1324 tahun"
}

# 72
translations[72] = {
    "tc": "是否確定解鎖四季福地超值福利？\\n（解鎖可立即領取<color=#9e4444>680仙玉</color>）",
    "en": "Are you sure to unlock Seasonal Domain great benefits?\\n(Unlocking allows claiming <color=#9e4444>680 Immortal Jade</color> immediately)",
    "id": "Apakah yakin untuk membuka keuntungan bernilai tinggi Domain Musiman?\\n(Membuka dapat langsung mengklaim <color=#9e4444>680 Giok Abadi</color>)"
}

# 73
translations[73] = {
    "tc": "論道大會段位獎",
    "en": "Theory Assembly Tier Rewards",
    "id": "Hadiah Tingkat Pertemuan Teori"
}

# 74
translations[74] = {
    "tc": "使用後習得靈級禦水神丹的煉製之法。（天品煉丹師方可使用）\\n禦水神丹服用後提升根骨和水系傷害。",
    "en": "Use to learn the refining method of G.Spirit Water-Control Orb.(Usable by G.Heaven Alchemist)\\nWater-Control Orb could use to improve Strength and Water DMG.",
    "id": "Gunakan untuk mempelajari metode pemurnian G.Roh Water-Control Orb.(Dapat digunakan oleh G.Surga Alkimis)\\nWater-Control Orb dapat digunakan untuk meningkatkan Daya dan DMG Air."
}

# 75
translations[75] = {
    "tc": "名稱：道場守衛\\n修為：分神四階\\n修煉：752年",
    "en": "Name: Dojo Guard\\nAttainment: Severance G.4\\nPracticing: 752 years",
    "id": "Nama: Penjaga Dojo\\nCapaian: Sengsara G.4\\nLatihan: 752 tahun"
}

# 76
translations[76] = {
    "tc": "春潮妙法",
    "en": "Spring Tide Secret Technique",
    "id": "Teknik Rahasia Pasang Musim Semi"
}

# 77
translations[77] = {
    "tc": "服用後凝練修士修為，增加210真氣、700點水系傷害。（最多服用80個）",
    "en": "Able to condense cultivator's Attainment, increase Qi by 210 and Water DMG by 700.(Max 80 can be used)",
    "id": "Dapat memadatkan Capaian kultivator, meningkatkan Qi sebesar 210 dan DMG Air sebesar 700.(Maksimal 80 dapat digunakan)"
}

# 78
translations[78] = {
    "tc": "祝賀道友本賽季論道大會榮譽上榜，小有薄名，略備薄禮，助您早日榮登榜首，威震寰宇。",
    "en": "Congratulations to fellow Taoist for making the honorable rank in this season's Theory Assembly! To honor your modest fame, a humble gift is prepared to help you ascend to the top of the leaderboard and awe the universe soon!",
    "id": "Selamat kepada rekan kultivator atas kehormatan masuk peringkat Pertemuan Teori musim ini! Merayakan ketenaran Anda, hadiah sederhana telah disiapkan untuk membantu Anda segera menduduki puncak peringkat dan mengguncang alam semesta!"
}

# 79
translations[79] = {
    "tc": "使用後獲得靈獸：冰眸寒魄（同名靈獸只能擁有一個）",
    "en": "Use to obtain Pet: Glacial Frostsoul (Only one Pet of the same name can be owned)",
    "id": "Gunakan untuk memperoleh Peliharaan: Glacial Frostsoul (Hanya dapat memiliki satu Peliharaan dengan nama yang sama)"
}

# 80
translations[80] = {
    "tc": "新屬性存在【%s及以上】品質詞條，確定要再次參悟嗎？",
    "en": "The new attributes contain affixes at [%s or better quality]. Are you sure to comprehend again?",
    "id": "Atribut baru memiliki entri dengan kualitas [%s atau lebih tinggi], apakah yakin ingin memahami lagi?"
}

# 81
translations[81] = {
    "tc": "福地仙冊",
    "en": "Blessed Land Immortal Book",
    "id": "Buku Abadi Tanah Berkah"
}

# 82
translations[82] = {
    "tc": "名稱：道場守衛\\n修為：太乙玉仙七階\\n修煉：1456年",
    "en": "Name: Dojo Guard\\nAttainment: Taiyi G.7\\nPracticing: 1456 years",
    "id": "Nama: Penjaga Dojo\\nCapaian: Taiyi G.7\\nLatihan: 1456 tahun"
}

# 83
translations[83] = {
    "tc": "探路嘍囉·戮",
    "en": "Pathfinding Minion · Slay",
    "id": "Kroco Penjelajah · Bantai"
}

# 84
translations[84] = {
    "tc": "悲秋遁術",
    "en": "Autumn Sorrow Escape Art",
    "id": "Jurus Kabur Ratapan Musim Gugur"
}

# 85
translations[85] = {
    "tc": "使用後將“無極仙途”稱號加入衣閣。",
    "en": "Use to add \"Infinite Cultivation\" Title into Closet.",
    "id": "Gunakan untuk menambahkan Gelar \"Kultivasi Tanpa Batas\" ke Lemari Pakaian."
}

# 86
translations[86] = {
    "tc": "收集[蕭淩萱信箋]",
    "en": "Collect [Xiao Lingxuan's Letter]",
    "id": "Kumpulkan [Surat Xiao Lingxuan]"
}

# 87
translations[87] = {
    "tc": "使用後將“山河圖”法相加入衣閣。",
    "en": "Use to add \"Vast Realm Scroll\" Deity Form into Closet.",
    "id": "Gunakan untuk menambahkan Wujud Dewa \"Lukisan Gunung dan Sungai\" ke Lemari Pakaian."
}

# 88
translations[88] = {
    "tc": "暫無道友通關",
    "en": "No Taoist friend has cleared yet",
    "id": "Belum ada rekan kultivator yang lolos"
}

# 89
translations[89] = {
    "tc": "名稱：道場守衛\\n修為：分神五階\\n修煉：841年",
    "en": "Name: Dojo Guard\\nAttainment: Severance G.5\\nPracticing: 841 years",
    "id": "Nama: Penjaga Dojo\\nCapaian: Sengsara G.5\\nLatihan: 841 tahun"
}

# 90
translations[90] = {
    "tc": "名稱：道場守衛\\n修為：大乘五階\\n修煉：1746年",
    "en": "Name: Dojo Guard\\nAttainment: Mahayana G.5\\nPracticing: 1746 years",
    "id": "Nama: Penjaga Dojo\\nCapaian: Mahayana G.5\\nLatihan: 1746 tahun"
}

# 91
translations[91] = {
    "tc": "晨息機緣丹",
    "en": "Morning Breath Fortuity Orb",
    "id": "Orb Keberuntungan Nafas Pagi"
}

# 92
translations[92] = {
    "tc": "名稱：道場守衛\\n修為：太乙玉仙五階\\n修煉：1347年",
    "en": "Name: Dojo Guard\\nAttainment: Taiyi G.5\\nPracticing: 1347 years",
    "id": "Nama: Penjaga Dojo\\nCapaian: Taiyi G.5\\nLatihan: 1347 tahun"
}

# 93
translations[93] = {
    "tc": "名稱：道場守衛\\n修為：仙帝六階\\n修煉：1247年",
    "en": "Name: Dojo Guard\\nAttainment: Deity Emperor G.6\\nPracticing: 1247 years",
    "id": "Nama: Penjaga Dojo\\nCapaian: Kaisar Dewa G.6\\nLatihan: 1247 tahun"
}

# 94
translations[94] = {
    "tc": "打開後可從：魏十八介紹信、杜靈菲介紹信、東雅介紹信中任選一個",
    "en": "Open to choose one from: Wei Shiba Recommendation Letter, Du Lingfei Recommendation Letter, Dongya Recommendation Letter",
    "id": "Buka untuk memilih salah satu dari: Surat Rekomendasi Wei Shiba, Surat Rekomendasi Du Lingfei, Surat Rekomendasi Dongya"
}

# 95
translations[95] = {
    "tc": "傳說中寒冷和冰雪世界的守護者，以獨眼注視著周圍環境，並有類似順風耳一般的極強聽力。",
    "en": "The legendary guardian of the cold and snowy realm, watching over the surroundings with a single eye, possessing extraordinary hearing akin to clairaudience.",
    "id": "Penjaga legendaris dunia dingin dan salju, mengawasi lingkungan sekitar dengan satu mata, dan memiliki pendengaran luar biasa tajam seperti telinga dewa angin."
}

# 96
translations[96] = {
    "tc": "鎮魔地圖進度",
    "en": "Demon Suppressing Map Progress",
    "id": "Kemajuan Peta Penindas Setan"
}

# 97
translations[97] = {
    "tc": "當前隨機魂力【%s層-%s層】",
    "en": "Current random Soul Energy [Floor %s - Floor %s]",
    "id": "Energi Jiwa acak saat ini [Lantai %s - Lantai %s]"
}

# 98
translations[98] = {
    "tc": "使用後可在聊天設置中選擇“月上枝頭”裝扮。",
    "en": "Use to select the \"Moon on willow head\" decoration in chat settings.",
    "id": "Gunakan untuk memilih dekorasi \"Bulan di kepala pohon willow\" dalam pengaturan obrolan."
}

# 99
translations[99] = {
    "tc": "收集[孟輕影信箋]",
    "en": "Collect [Meng Qingying's Letter]",
    "id": "Kumpulkan [Surat Meng Qingying]"
}

# 100
translations[100] = {
    "tc": "舞衫歌扇",
    "en": "Dancing Robe and Singing Fan",
    "id": "Gaun Tarian dan Kipas Nyanyian"
}

# 101
translations[101] = {
    "tc": "傳說中的神獸，龍頭、馬身、麟腳，形似獅子，會飛。貔貅兇猛威武，它在天上負責巡視工作，阻止妖魔鬼怪、瘟疫疾病擾亂天庭。",
    "en": "A legendary divine beast with dragon head, horse body, qilin feet, resembling a lion, capable of flight. Pixiu is fierce and majestic; patrolling the heavens, it prevents demons, ghosts, plagues, and diseases from disturbing the Heavenly Court.",
    "id": "Binatang suci legendaris berkepala naga, berbadan kuda, berkaki qilin, mirip singa, dan dapat terbang. Pixiu ganas dan perkasa; berpatroli di surga, ia mencegah siluman, hantu, wabah, dan penyakit mengacaukan Istana Surgawi."
}

# 102
translations[102] = {
    "tc": "洞窟魔物·盾",
    "en": "Cave Monster · Shield",
    "id": "Monster Gua · Perisai"
}

# 103
translations[103] = {
    "tc": "使用後可在聊天設置中選擇“天階”裝扮。",
    "en": "Use to select the \"G.Heaven\" decoration in chat settings.",
    "id": "Gunakan untuk memilih dekorasi \"G.Surga\" dalam pengaturan obrolan."
}

# 104
translations[104] = {
    "tc": "修行界初級功法需要<color=#458114>金丹</color>方可參悟\\n停車坐愛楓林晚，霜葉紅於二月花。\\n效果：<color=#458114>防禦提升</color>",
    "en": "Reach <color=#458114>Formation</color> to comprehend the Pri.Technique of Practice\\nStopping the carriage to admire the maple woods at dusk; frost-bitten leaves are redder than spring flowers in February.\\nEffect: <color=#458114>DEF increased</color>",
    "id": "Mencapai <color=#458114>Formasi</color> untuk memahami Teknik Dasar Kultivasi\\nMenghentikan kereta menikmati senja di hutan mapel, daun berembun es lebih merah dari bunga musim semi.\\nEfek: <color=#458114>Peningkatan Pertahanan</color>"
}

# 105
translations[105] = {
    "tc": "1.每個靈獸都可以覺醒血脈，品質越高的靈獸可覺醒血脈個數越多\\n2.靈獸有<color=#9e4444>血脈強化</color>和<color=#9e4444>血脈淬煉</color>兩種養成\\n3.血脈強化\\n（1）每條血脈都有2種基礎強化屬性，消耗<color=#9e4444>【妖獸殘血】【妖獸精血】</color>來強化提升血脈屬性\\n（2）品質越高的靈獸強化等級上限越高\\n<color=#FF0000>天品靈獸40級（玄武50級 ）</color> \\n<color=#FF8C00>地品靈獸30級 </color> \\n<color=#9400D3>玄品靈獸20級</color>\\n<color=#0000FF>黃品靈獸10級</color>\\n（3）血脈強化等級受靈獸涅槃轉數影響\\n靈獸1轉50級，血脈強化限制為10級\\n靈獸2轉1級，血脈強化限制為20級\\n靈獸2轉50級，血脈可強化至最高等級\\n4.重選血脈\\n（1）道友可以<color=#9e4444>重新選擇血脈</color>替換上陣（已覺醒的血脈不再扣除精血道具）。\\n（2）替換血脈的<color=#9e4444>等級培養進度保留！</color>只更換基礎屬性、和被基礎屬性影響的淬煉加成屬性\\n5.血脈淬煉\\n（1）每個靈獸最高可擁有4條淬煉屬性！\\n<color=#FF0000>天品靈獸</color>4個血脈=4個淬煉屬性\\n<color=#FF8C00>地品靈獸</color>3個血脈=3個淬煉屬性\\n<color=#9400D3>玄品靈獸</color>2個血脈=2個淬煉屬性\\n<color=#0000FF>黃品靈獸</color>1個血脈=1個淬煉屬性\\n（2）消耗<color=#9e4444>【妖獸精血】</color>可淬煉出不同品質的屬性詞條\\n（3）連續淬煉<color=#9e4444>20次</color>，下次淬煉必出一條紫色品質的屬性\\n（4）靈獸涅槃達到4轉之前，轉數越高，詞條淬煉出的屬性越好\\n（5）出現高品質淬煉屬性時，可消耗<color=#9e4444>【鎮脈石】</color>將其鎖定；被鎖定的屬性在下次淬煉中將不會被刷新！\\n鎖定1個詞條消耗1個鎮脈石\\n同時鎖定2個詞條消耗3個鎮脈石\\n當少於等於2個詞條時不能鎖定\\n當大於3個詞條時最多同時鎖定2個詞條\\n每次淬煉後保留上次鎖定選擇，仔細查看及時更換選擇\\n（6）淬煉屬性品質概率：\\n<color=#008000>綠色品質：60.5%</color>\\n<color=#0000FF>藍色品質：24%</color>\\n<color=#9400D3>紫色品質：10%</color>\\n<color=#FF8C00>橙色品質：5%</color>\\n<color=#FF0000>紅色品質：0.5%</color>",
    "en": "1. Every Pet can awaken Bloodlines. The higher the Pet's quality, the more Bloodlines can be awakened.\\n2. Pets have two development paths: <color=#9e4444>Bloodline Enhancement</color> and <color=#9e4444>Bloodline Quenching</color>.\\n3. Bloodline Enhancement\\n(1) Each Bloodline has 2 basic enhancement attributes. Consume <color=#9e4444>[Fiend Blood] [Fiend Essence]</color> to enhance and upgrade Bloodline attributes.\\n(2) Pets of higher quality have higher enhancement level caps:\\n<color=#FF0000>G.Heaven Pet Lv.40 (Xuanwu Lv.50)</color> \\n<color=#FF8C00>G.Earth Pet Lv.30</color> \\n<color=#9400D3>G.Mythic Pet Lv.20</color>\\n<color=#0000FF>G.Novice Pet Lv.10</color>\\n(3) Bloodline enhancement level is affected by Pet Nirvana Reincarnations:\\nPet 1st Reincarnation Lv.50, Bloodline enhancement capped at Lv.10\\nPet 2nd Reincarnation Lv.1, Bloodline enhancement capped at Lv.20\\nPet 2nd Reincarnation Lv.50, Bloodline can be enhanced to max level\\n4. Reselect Bloodline\\n(1) Fellow Taoists can <color=#9e4444>reselect Bloodline</color> to deploy in battle (already awakened Bloodlines will no longer deduct Fiend Essence items).\\n(2) <color=#9e4444>Level training progress is retained</color> when replacing Bloodline! Only basic attributes and quenching bonus attributes affected by basic attributes will be changed.\\n5. Bloodline Quenching\\n(1) Each Pet can possess up to 4 quenching attributes!\\n<color=#FF0000>G.Heaven Pet</color> 4 Bloodlines = 4 quenching attributes\\n<color=#FF8C00>G.Earth Pet</color> 3 Bloodlines = 3 quenching attributes\\n<color=#9400D3>G.Mythic Pet</color> 2 Bloodlines = 2 quenching attributes\\n<color=#0000FF>G.Novice Pet</color> 1 Bloodline = 1 quenching attribute\\n(2) Consume <color=#9e4444>[Fiend Essence]</color> to quench attribute affixes of different qualities.\\n(3) Quenching <color=#9e4444>20 times</color> consecutively guarantees a purple quality attribute on the next quenching.\\n(4) Before Pet Nirvana reaches 4th Reincarnation, the higher the Reincarnation, the better the attributes quenched from affixes.\\n(5) When high-quality quenching attributes appear, consume <color=#9e4444>[Gem of Veins]</color> to lock them; locked attributes will not be refreshed in the next quenching!\\nLocking 1 affix consumes 1 Gem of Veins\\nLocking 2 affixes simultaneously consumes 3 Gems of Veins\\nCannot lock when there are 2 or fewer affixes\\nCan lock up to 2 affixes simultaneously when there are more than 3 affixes\\nPrevious lock choices are retained after each quenching, please check carefully and update selections in time\\n(6) Quenching attribute quality probability:\\n<color=#008000>Green Quality: 60.5%</color>\\n<color=#0000FF>Blue Quality: 24%</color>\\n<color=#9400D3>Purple Quality: 10%</color>\\n<color=#FF8C00>Orange Quality: 5%</color>\\n<color=#FF0000>Red Quality: 0.5%</color>",
    "id": "1. Setiap Peliharaan dapat membangkitkan Garis Keturunan. Semakin tinggi kualitas Peliharaan, semakin banyak Garis Keturunan yang dapat dibangkitkan.\\n2. Peliharaan memiliki 2 jalur pembinaan: <color=#9e4444>Peningkatan Garis Keturunan</color> dan <color=#9e4444>Pendinginan Garis Keturunan</color>.\\n3. Peningkatan Garis Keturunan\\n(1) Setiap Garis Keturunan memiliki 2 jenis atribut peningkatan dasar. Konsumsi <color=#9e4444>[Darah Iblis] [Esensi Iblis]</color> untuk meningkatkan atribut Garis Keturunan.\\n(2) Semakin tinggi kualitas Peliharaan, semakin tinggi batas level peningkatan:\\n<color=#FF0000>Peliharaan G.Surga Lv.40 (Xuanwu Lv.50)</color> \\n<color=#FF8C00>Peliharaan G.Earth Lv.30</color> \\n<color=#9400D3>Peliharaan G.Mistik Lv.20</color>\\n<color=#0000FF>Peliharaan G.Pemula Lv.10</color>\\n(3) Level peningkatan Garis Keturunan dipengaruhi oleh Reinkarnasi Nirwana Peliharaan:\\nPeliharaan Reinkarnasi 1 Lv.50, batas peningkatan Garis Keturunan adalah Lv.10\\nPeliharaan Reinkarnasi 2 Lv.1, batas peningkatan Garis Keturunan adalah Lv.20\\nPeliharaan Reinkarnasi 2 Lv.50, Garis Keturunan dapat ditingkatkan hingga level tertinggi\\n4. Pilih Ulang Garis Keturunan\\n(1) Rekan kultivator dapat <color=#9e4444>memilih ulang Garis Keturunan</color> untuk bertempur (Garis Keturunan yang telah dibangkitkan tidak akan memotong item Esensi Iblis lagi).\\n(2) <color=#9e4444>Kemajuan pelatihan level dipertahankan</color> saat mengganti Garis Keturunan! Hanya atribut dasar dan atribut bonus pendinginan yang dipengaruhi atribut dasar yang akan diganti.\\n5. Pendinginan Garis Keturunan\\n(1) Setiap Peliharaan dapat memiliki hingga 4 atribut pendinginan!\\n<color=#FF0000>Peliharaan G.Surga</color> 4 Garis Keturunan = 4 atribut pendinginan\\n<color=#FF8C00>Peliharaan G.Earth</color> 3 Garis Keturunan = 3 atribut pendinginan\\n<color=#9400D3>Peliharaan G.Mistik</color> 2 Garis Keturunan = 2 atribut pendinginan\\n<color=#0000FF>Peliharaan G.Pemula</color> 1 Garis Keturunan = 1 atribut pendinginan\\n(2) Konsumsi <color=#9e4444>[Esensi Iblis]</color> untuk mendinginkan entri atribut dengan berbagai kualitas.\\n(3) Pendinginan berturut-turut <color=#9e4444>20 kali</color> menjamin atribut kualitas ungu pada pendinginan berikutnya.\\n(4) Sebelum Nirwana Peliharaan mencapai Reinkarnasi 4, semakin tinggi Reinkarnasi, semakin baik atribut yang dihasilkan dari pendinginan entri.\\n(5) Saat muncul atribut pendinginan berkualitas tinggi, dapat mengonsumsi <color=#9e4444>[Permata Vena]</color> untuk menguncinya; atribut yang dikunci tidak akan diperbarui pada pendinginan berikutnya!\\nMengunci 1 entri mengonsumsi 1 Permata Vena\\nMengunci 2 entri sekaligus mengonsumsi 3 Permata Vena\\nTidak dapat mengunci jika terdapat 2 atau lebih sedikit entri\\nDapat mengunci maksimal 2 entri sekaligus jika terdapat lebih dari 3 entri\\nSetelah setiap pendinginan, pilihan kunci sebelumnya dipertahankan, harap periksa dengan cermat dan perbarui pilihan tepat waktu\\n(6) Peluang kualitas atribut pendinginan:\\n<color=#008000>Kualitas Hijau: 60.5%</color>\\n<color=#0000FF>Kualitas Biru: 24%</color>\\n<color=#9400D3>Kualitas Ungu: 10%</color>\\n<color=#FF8C00>Kualitas Oranye: 5%</color>\\n<color=#FF0000>Kualitas Merah: 0.5%</color>"
}

# 106
translations[106] = {
    "tc": "收集[桃夭信箋]",
    "en": "Collect [Tao Yao's Letter]",
    "id": "Kumpulkan [Surat Tao Yao]"
}

# 107
translations[107] = {
    "tc": "論道功勳",
    "en": "Theory Merits",
    "id": "Jasa Teori"
}

# 108
translations[108] = {
    "tc": "使用後可獲得隨機秘寶材料。\\n包含：日月精粹、洪荒精魄",
    "en": "Use to obtain random Secret Treasure materials.\\nContains: Essense of Sun and Moon, Chaos Essense",
    "id": "Gunakan untuk mendapatkan material Harta Karun Rahasia acak.\\nBerisi: Inti dari Matahari dan Bulan, Esensi Kekacauan"
}

# 109
translations[109] = {
    "tc": "參悟該道書需要：<color=#ad2228>%s</color>",
    "en": "Comprehending this book requires: <color=#ad2228>%s</color>",
    "id": "Memahami kitab Tao ini memerlukan: <color=#ad2228>%s</color>"
}

# 110
translations[110] = {
    "tc": "章節任務完成進度",
    "en": "Chapter Quest Completion Progress",
    "id": "Kemajuan Penyelesaian Misi Bab"
}

# 111
translations[111] = {
    "tc": "修行界頂級功法需要<color=#458114>太乙玉仙</color>方可參悟\\n效果：<color=#458114>修煉速度提升</color>",
    "en": "Reach <color=#458114>Taiyi</color> to comprehend the Top Technique of Practice\\nEffect: <color=#458114>Cultivation Speed increased</color>",
    "id": "Mencapai <color=#458114>Taiyi</color> untuk memahami Teknik Teratas Kultivasi\\nEfek: <color=#458114>Peningkatan Kecepatan Latihan</color>"
}

# 112
translations[112] = {
    "tc": "修行界高級功法，但寫的通俗易懂<color=#458114>合體期</color>便可參悟\\n據說，高坐紫霄那位成道前曾親自審閱過。\\n效果：<color=#458114>修煉速度提升</color>",
    "en": "An Adv.Technique of Practice, written plainly so one can comprehend at <color=#458114>Embodiment</color> stage.\\nLegend has it that the venerable one who sits high in Zixiao personally reviewed it before attaining Tao.\\nEffect: <color=#458114>Cultivation Speed increased</color>",
    "id": "Teknik lanjutan kultivasi yang ditulis sederhana sehingga dapat dipahami di tahap <color=#458114>Menjelma</color>.\\nKonon Yang Mulia yang bertahta tinggi di Zixiao sempat memeriksanya sendiri sebelum mencapai Tao.\\nEfek: <color=#458114>Peningkatan Kecepatan Latihan</color>"
}

# 113
translations[113] = {
    "tc": "使用後將“試劍天下”服裝加入衣閣。",
    "en": "Use to add \"Sword of the Realm\" costume into Closet.",
    "id": "Gunakan untuk menambahkan Busana \"Pedang Alam Semesta\" ke Lemari Pakaian."
}

# 114
translations[114] = {
    "tc": "祝賀道友本賽季論道大會榮譽上榜，位列第二，名傳三界，威名赫赫。",
    "en": "Congratulations to fellow Taoist for earning an honorable place in this season's Theory Assembly, ranking 2nd, renowned throughout the Three Realms with illustrious prestige!",
    "id": "Selamat kepada rekan kultivator atas kehormatan masuk peringkat Pertemuan Teori musim ini, menempati posisi ke-2, tersohor di Tiga Alam dengan reputasi termasyhur!"
}

# Verification & Building Result
result = {}
errors = []

for i, src in enumerate(chunk_0):
    if i not in translations:
        errors.append(f"Missing translation for index {i}: {src}")
        continue
    tr = translations[i]
    for lang in ['tc', 'en', 'id']:
        if lang not in tr:
            errors.append(f"Index {i} missing lang {lang}")
            continue
        val = tr[lang]
        
        # 1. Placeholder protection check
        src_phs = re.findall(r'%[0-9]*\.?[0-9]*[sdfmX%]', src)
        val_phs = re.findall(r'%[0-9]*\.?[0-9]*[sdfmX%]', val)
        if sorted(src_phs) != sorted(val_phs):
            errors.append(f"Index {i} ({lang}) placeholder mismatch: src={src_phs}, val={val_phs}")
            
        # 2. Color tag check
        src_tags = re.findall(r'<color=[^>]+>|</color>', src)
        val_tags = re.findall(r'<color=[^>]+>|</color>', val)
        if src_tags != val_tags:
            errors.append(f"Index {i} ({lang}) tag mismatch: src={src_tags}, val={val_tags}")
            
        # 3. Newline check
        src_nl = src.count('\\n')
        val_nl = val.count('\\n')
        if src_nl != val_nl:
            errors.append(f"Index {i} ({lang}) newline count mismatch: src={src_nl}, val={val_nl}")

    result[src] = tr

print(f"Total processed: {len(result)}/115")
if errors:
    print(f"ERRORS FOUND ({len(errors)}):")
    for e in errors:
        print("  -", e)
else:
    print("ALL CHECKS PASSED PERFECTLY!")
    out_path = 'result_chunk_0.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"Saved successfully to {out_path}!")
