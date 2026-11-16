# -*- coding: utf-8 -*-
import json
import re

with open(r'F:\项目\无极国际版\chunk_4.json', 'r', encoding='utf-8') as f:
    chunk_items = json.load(f)

print(f"Total items in chunk_4.json: {len(chunk_items)}")

item_translations = [
    # 0: '精英魔物·盾'
    {
        "tc": "精英魔物·盾",
        "en": "Elite Monster · Shield",
        "id": "Monster Elit · Perisai"
    },
    # 1: '精英魔物·伐'
    {
        "tc": "精英魔物·伐",
        "en": "Elite Monster · Strike",
        "id": "Monster Elit · Serang"
    },
    # 2: '探路喽啰·攻'
    {
        "tc": "探路嘍囉·攻",
        "en": "Scout Minion · ATK",
        "id": "Kroco Pengintai · Serang"
    },
    # 3: '洞窟魔物·甲'
    {
        "tc": "洞窟魔物·甲",
        "en": "Cave Monster · Armor",
        "id": "Monster Gua · Zirah"
    },
    # 4: '洞窟魔物·伐'
    {
        "tc": "洞窟魔物·伐",
        "en": "Cave Monster · Strike",
        "id": "Monster Gua · Serang"
    },
    # 5: '1、四季福地开启时间为每月1号10点至最后一天24点，并且随季节开放不同的内容\\n2、击败凶兽和完成机缘都可以获得福地经验提高福地等级，等级越高出现的机缘等级也越高，奖励也越丰厚\\n3、每次活动开启，除福玉、仙册外其他相关数据都会重置\\n4、福地内包含每日刷新的机缘、凶兽，还有仙册和洞窟闯关内容，且福地内的全部战斗采用弟子战斗\\n5、可以通过仙玉和机缘令增加每日的机缘次数，额外的机缘次数会随着0点刷新一起刷新'
    {
        "tc": "1、四季福地開啟時間為每月1號10點至最後一天24點，並且隨季節開放不同的內容\\n2、擊敗兇獸和完成機緣都可以獲得福地經驗提高福地等級，等級越高出現的機緣等級也越高，獎勵也越豐厚\\n3、每次活動開啟，除福玉、仙冊外其他相關數據都會重置\\n4、福地內包含每日刷新的機緣、兇獸，還有仙冊和洞窟闖關內容，且福地內的全部戰鬥採用弟子戰鬥\\n5、可以通過仙玉和機緣令增加每日的機緣次數，額外的機緣次數會隨著0點刷新一起刷新",
        "en": "1. Seasonal Domain is open from 10:00 on the 1st of each month to 24:00 on the last day, with different content available according to the season.\\n2. Defeating fierce beasts and completing fortuities grant Domain EXP to raise Domain Level. The higher the level, the higher the fortuity tier and richer the rewards.\\n3. Each time the event opens, all related data except Seasonal Jade and Divine Book will be reset.\\n4. The Domain includes daily-refreshed fortuities and fierce beasts, as well as Divine Book and cave clearance content. All battles in the Domain are fought by disciples.\\n5. You can use Div.Jade and Fortuity Tokens to increase daily fortuity attempts. Extra attempts will reset along with the daily 0:00 refresh.",
        "id": "1. Domain Musiman dibuka dari tanggal 1 pukul 10:00 setiap bulan hingga hari terakhir pukul 24:00, dan konten yang berbeda dibuka sesuai musim.\\n2. Mengalahkan binatang ganas dan menyelesaikan kemujuran dapat memperoleh EXP domain untuk meningkatkan level domain. Semakin tinggi levelnya, semakin tinggi level kemujuran yang muncul, dan hadiahnya semakin melimpah.\\n3. Setiap kali event dibuka, data terkait lainnya akan direset kecuali Giok Musiman dan Buku Ilahi.\\n4. Domain ini mencakup kemujuran dan binatang ganas yang disegarkan setiap hari, serta Buku Ilahi dan konten penjelajahan gua, dan semua pertempuran di dalam domain menggunakan pertempuran murid.\\n5. Anda dapat menggunakan Batu Giok dan Token Kemujuran untuk meningkatkan jumlah kemujuran harian. Jumlah kemujuran tambahan akan disegarkan bersama dengan penyegaran pukul 0:00."
    },
    # 6: '论道功勋不足'
    {
        "tc": "論道功勳不足",
        "en": "Insufficient Theory Merits",
        "id": "Jasa Teori tidak cukup"
    },
    # 7: '打开后可获得试剑天下（男）*1和试剑天下（女）*1'
    {
        "tc": "打開後可獲得試劍天下（男）*1和試劍天下（女）*1",
        "en": "Open to obtain Sword of the Realm（Male）*1 and Sword of the Realm（Female）*1",
        "id": "Setelah dibuka, dapatkan Uji Pedang di Jagat Raya (Pria)*1 dan Uji Pedang di Jagat Raya (Wanita)*1"
    },
    # 8: '使用后可在聊天设置中选择“地阶”装扮。'
    {
        "tc": "使用後可在聊天設置中選擇「地階」裝扮。",
        "en": "Use to select \"G.Earth\" outfit in chat settings.",
        "id": "Gunakan untuk memilih pakaian \"G.Earth\" di pengaturan obrolan."
    },
    # 9: '青稚的男孩神情微微一怔，又很快掩饰了过去。单手接过油纸包，并用另外一只手将女孩冻得通红的小手揣入自己怀中。“夏夏，你怎么出门都不带个裹手，手都冻的通红。”'
    {
        "tc": "青稚的男孩神情微微一怔，又很快掩飾了過去。單手接過油紙包，並用另外一隻手將女孩凍得通紅的小手揣入自己懷中。「夏夏，你怎麼出門都不帶個裹手，手都凍的通紅。」",
        "en": "The young boy was slightly stunned, but quickly concealed it. He took the oiled paper package with one hand and tucked the girl's red-frozen little hand into his chest with the other. \"Xiaxia, why did you go out without hand wraps? Your hands are frozen red.\"",
        "id": "Bocah laki-laki muda itu tampak tertegun sejenak, namun segera menyembunyikannya. Dia menerima bungkusan kertas minyak dengan satu tangan, dan menyelipkan tangan kecil gadis yang merah membeku itu ke dalam dadanya dengan tangan yang lain. \"Xiaxia, kenapa kamu keluar tanpa sarung tangan? Tanganmu sampai merah membeku.\""
    },
    # 10: '论道大会礼包'
    {
        "tc": "論道大會禮包",
        "en": "Theory Assembly Gift Pack",
        "id": "Paket Hadiah Pertemuan Teori"
    },
    # 11: '修行界顶级功法需要<color=#458114>太乙玉仙</color>方可参悟\\n效果：<color=#458114>命中、闪避提升</color>'
    {
        "tc": "修行界頂級功法需要<color=#458114>太乙玉仙</color>方可參悟\\n效果：<color=#458114>命中、閃避提升</color>",
        "en": "Top Cultivation World Technique requires <color=#458114>Taiyi</color> to comprehend\\nEffect: <color=#458114>Hit, EVA Boost</color>",
        "id": "Teknik teratas Dunia Kultivasi memerlukan <color=#458114>Taiyi</color> untuk dipahami\\nEfek: <color=#458114>Peningkatan Hit, EVA</color>"
    },
    # 12: '灵级破元神丹方'
    {
        "tc": "靈級破元神丹方",
        "en": "G.Spirit Yuan-Breaking Divine Orb Recipe",
        "id": "G.Resep Orb Ilahi Pemecah Yuan"
    },
    # 13: '伏暑功法礼包'
    {
        "tc": "伏暑功法禮包",
        "en": "Summer Heat Technique Gift Pack",
        "id": "Paket Hadiah Teknik Panas Terik"
    },
    # 14: '是否花费%s仙玉购买礼包'
    {
        "tc": "是否花費%s仙玉購買禮包",
        "en": "Spend %s Div.Jade to buy the gift pack?",
        "id": "Apakah menghabiskan %s Batu Giok untuk membeli paket hadiah?"
    },
    # 15: '战神'
    {
        "tc": "戰神",
        "en": "War God",
        "id": "Dewa Perang"
    },
    # 16: '使用后将“水调歌头”服装加入衣阁。'
    {
        "tc": "使用後將「水調歌頭」服裝加入衣閣。",
        "en": "Use to add \"Melody of the Moon\" outfit to Closet.",
        "id": "Gunakan untuk menambahkan kostum \"Senandung Melodi Air\" ke Lemari."
    },
    # 17: '论道大会挑战次数增加%s'
    {
        "tc": "論道大會挑戰次數增加%s",
        "en": "Theory Assembly challenge attempts increased by %s",
        "id": "Jumlah tantangan Pertemuan Teori bertambah %s"
    },
    # 18: '1、灵兽招式可在游历-灵渊兽域中获取\\n2、可消耗战神图录·拓本和驭兽心得提升招式等级，最高10级\\n3、提升涅槃等级可开启更多招式格子\\n4、灵兽所有招式共享，可配置招式单独统计\\n5、遗忘招式将会返还70%升级消耗的资源，正在使用中技能无法遗忘\\n6、前缀相同的招式，只能同时装备一个\\n7、三阶满级招式开启<color=#9e4444>招式参悟</color>功能，道友可参悟出新的词条、提升当前技能的加成效果（若遗忘三阶招式，将不会返回参悟功能的培养道具！请道友注意～）'
    {
        "tc": "1、靈獸招式可在遊歷-靈淵獸域中獲取\\n2、可消耗戰神圖錄·拓本和馭獸心得提升招式等級，最高10級\\n3、提升涅槃等級可開啟更多招式格子\\n4、靈獸所有招式共享，可配置招式單獨統計\\n5、遺忘招式將會返還70%升級消耗的資源，正在使用中技能無法遺忘\\n6、前綴相同的招式，只能同時裝備一個\\n7、三階滿級招式開啟<color=#9e4444>招式參悟</color>功能，道友可參悟出新的詞條、提升當前技能的加成效果（若遺忘三階招式，將不會返回參悟功能的培養道具！請道友注意～）",
        "en": "1. Pet moves can be obtained in Roam - Spirit Abyss Beast Realm.\\n2. Mars Catalog and Beast Experience can be consumed to upgrade move level, up to Lv.10.\\n3. Raising Nirvana level can unlock more move slots.\\n4. All Pet moves are shared; configurable moves are counted separately.\\n5. Forgetting a move will refund 70% of the resources spent on upgrading. Moves currently in use cannot be forgotten.\\n6. Moves with the same prefix can only be equipped one at a time.\\n7. Tier-3 max-level moves unlock the <color=#9e4444>Move Comprehension</color> feature. Cultivators can comprehend new affixes and increase the bonus effect of the current skill (If a Tier-3 move is forgotten, cultivation items from the comprehension feature will NOT be refunded! Please be aware~)",
        "id": "1. Jurus Peliharaan dapat diperoleh di Kelana - Wilayah Binatang Jurang Roh.\\n2. Dapat mengonsumsi Katalog Mars dan Pengalaman Binatang untuk meningkatkan level jurus, hingga level 10.\\n3. Meningkatkan level Nirwana dapat membuka lebih banyak slot jurus.\\n4. Semua jurus Peliharaan dibagikan, jurus yang dapat dikonfigurasi dihitung secara terpisah.\\n5. Melupakan jurus akan mengembalikan 70% sumber daya yang dikonsumsi untuk peningkatan. Skill yang sedang digunakan tidak dapat dilupakan.\\n6. Jurus dengan awalan yang sama hanya dapat dipasang satu sekaligus.\\n7. Jurus Tier 3 level maks membuka fungsi <color=#9e4444>Pemahaman Jurus</color>. Rekan Taois dapat memahami atribut baru dan meningkatkan efek bonus skill saat ini (Jika Anda melupakan jurus Tier 3, item pelatihan fungsi pemahaman tidak akan dikembalikan! Harap perhatikan~)"
    },
    # 19: '四季福地-凶兽-夏'
    {
        "tc": "四季福地-兇獸-夏",
        "en": "Seasonal Domain - Fierce Beast - Summer",
        "id": "Domain Musiman - Binatang Ganas - Musim Panas"
    },
    # 20: '悲秋天书'
    {
        "tc": "悲秋天書",
        "en": "Sad Autumn Heaven Book",
        "id": "Buku Surga Musim Gugur Pilu"
    },
    # 21: '伏暑遁术'
    {
        "tc": "伏暑遁術",
        "en": "Summer Heat Escape Art",
        "id": "Seni Pelarian Panas Terik"
    },
    # 22: '服用后凝练修士修为，增加210根骨、700点金系伤害。（最多服用80个）'
    {
        "tc": "服用後凝練修士修為，增加210根骨、700點金系傷害。（最多服用80個）",
        "en": "Take to condense cultivator's Attainment, increasing 210 Strength and 700 Metal Damage. (Max 80 can be taken)",
        "id": "Konsumsi untuk memadatkan Capaian praktisi, meningkatkan 210 Daya dan 700 Kerusakan Logam. (Maks 80 dapat dikonsumsi)"
    },
    # 23: '论道大会玩法获取，可在对应玩法店铺中兑换道具。'
    {
        "tc": "論道大會玩法獲取，可在對應玩法店鋪中兌換道具。",
        "en": "Obtained from Theory Assembly gameplay, can be exchanged for items in the corresponding event shop.",
        "id": "Diperoleh dari gameplay Pertemuan Teori, dapat ditukarkan dengan item di toko gameplay terkait."
    },
    # 24: '剩余体力不足'
    {
        "tc": "剩餘體力不足",
        "en": "Insufficient Stamina remaining",
        "id": "Sisa Stamina tidak cukup"
    },
    # 25: '残冬灵本'
    {
        "tc": "殘冬靈本",
        "en": "Lingering Winter Codex",
        "id": "Codex Sisa Musim Dingin"
    },
    # 26: '拥有灵兽个数'
    {
        "tc": "擁有靈獸個數",
        "en": "Number of Pets Owned",
        "id": "Jumlah Peliharaan yang Dimiliki"
    },
    # 27: '紫霄妙法'
    {
        "tc": "紫霄妙法",
        "en": "Purplesky Sutra",
        "id": "Sutra Langit Ungu"
    },
    # 28: '灵级生息神丹方'
    {
        "tc": "靈級生息神丹方",
        "en": "G.Spirit Vitality Divine Orb Recipe",
        "id": "G.Resep Orb Ilahi Vitalitas Roh"
    },
    # 29: '机缘令'
    {
        "tc": "機緣令",
        "en": "Fortuity Token",
        "id": "Token Kemujuran"
    },
    # 30: '使用后习得灵级奇火神丹的炼制之法。（天品炼丹师方可使用）\\n奇火神丹服用后提升根骨和火系伤害。'
    {
        "tc": "使用後習得靈級奇火神丹的煉製之法。（天品煉丹師方可使用）\\n奇火神丹服用後提升根骨和火系傷害。",
        "en": "Use to learn G.Spirit Mystic Fire Divine Orb Refining. (Usable by G.Heaven Alchemist)\\nTaking Mystic Fire Divine Orb increases Strength and Fire Damage.",
        "id": "Gunakan untuk mempelajari metode pemurnian G.Spirit Api Mistik Divine Orb. (Dapat digunakan oleh Alkimis G.Surga)\\nKonsumsi Api Mistik Divine Orb meningkatkan Daya dan Kerusakan Api."
    },
    # 31: '名称：道场守卫\\n修为：元婴七阶\\n修炼：798年'
    {
        "tc": "名稱：道場守衛\\n修為：元嬰七階\\n修煉：798年",
        "en": "Name: Dojo Guard\\nAttainment: Nascence Tier 7\\nCultivation: 798 Years",
        "id": "Nama: Penjaga Dojo\\nCapaian: Nascence Tingkat 7\\nKultivasi: 798 Tahun"
    },
    # 32: '修行界初级功法需要<color=#458114>金丹</color>方可参悟\\n停车坐爱枫林晚，霜叶红于二月花。\\n效果：<color=#458114>灵气获取提升</color>'
    {
        "tc": "修行界初級功法需要<color=#458114>金丹</color>方可參悟\\n停車坐愛楓林晚，霜葉紅於二月花。\\n效果：<color=#458114>靈氣獲取提升</color>",
        "en": "Primary Cultivation World Technique requires <color=#458114>Formation</color> to comprehend\\nStopping the carriage, captivated by the maple grove at dusk; frosted leaves outshine the blossoms of early spring.\\nEffect: <color=#458114>Qi Gathering Boost</color>",
        "id": "Teknik dasar Dunia Kultivasi memerlukan <color=#458114>Formasi</color> untuk dipahami\\nBerhenti sejenak menikmati hutan maple di kala senja, daun beku lebih merah dari bunga musim semi.\\nEfek: <color=#458114>Peningkatan Perolehan Qi</color>"
    },
    # 33: '名称：道场守卫\\n修为：仙尊八阶\\n修炼：1324年'
    {
        "tc": "名稱：道場守衛\\n修為：仙尊八階\\n修煉：1324年",
        "en": "Name: Dojo Guard\\nAttainment: Deity Lord Tier 8\\nCultivation: 1324 Years",
        "id": "Nama: Penjaga Dojo\\nCapaian: Mahadewa Raja Tingkat 8\\nKultivasi: 1324 Tahun"
    },
    # 34: '固定消耗'
    {
        "tc": "固定消耗",
        "en": "Fixed Cost",
        "id": "Konsumsi Tetap"
    },
    # 35: '使用后将“烛小龙”头像框加入衣阁。'
    {
        "tc": "使用後將「燭小龍」頭像框加入衣閣。",
        "en": "Use to add \"Little Torch Dragon\" avatar frame to Closet.",
        "id": "Gunakan untuk menambahkan bingkai avatar \"Naga Lilin Cilik\" ke Lemari."
    },
    # 36: '修行界顶级功法需要<color=#458114>太乙玉仙</color>方可参悟\\n效果：<color=#458114>灵气获取提升</color>'
    {
        "tc": "修行界頂級功法需要<color=#458114>太乙玉仙</color>方可參悟\\n效果：<color=#458114>靈氣獲取提升</color>",
        "en": "Top Cultivation World Technique requires <color=#458114>Taiyi</color> to comprehend\\nEffect: <color=#458114>Qi Gathering Boost</color>",
        "id": "Teknik teratas Dunia Kultivasi memerlukan <color=#458114>Taiyi</color> untuk dipahami\\nEfek: <color=#458114>Peningkatan Perolehan Qi</color>"
    },
    # 37: '吾名%s'
    {
        "tc": "吾名%s",
        "en": "My name is %s",
        "id": "Namaku adalah %s"
    },
    # 38: '服用后凝练修士修为，增加210身法、700点木系伤害。（最多服用80个）'
    {
        "tc": "服用後凝練修士修為，增加210身法、700點木系傷害。（最多服用80個）",
        "en": "Take to condense cultivator's Attainment, increasing 210 Agility and 700 Wood Damage. (Max 80 can be taken)",
        "id": "Konsumsi untuk memadatkan Capaian praktisi, meningkatkan 210 Kelincahan dan 700 Kerusakan Kayu. (Maks 80 dapat dikonsumsi)"
    },
    # 39: '高级'
    {
        "tc": "高級",
        "en": "Advanced",
        "id": "Tingkat Lanjut"
    },
    # 40: '神秘灵兽蛋-夏'
    {
        "tc": "神秘靈獸蛋-夏",
        "en": "Mysterious Pet Egg - Summer",
        "id": "Telur Peliharaan Misterius - Musim Panas"
    },
    # 41: '服用后凝练修士修为，增加210根骨、700点水系伤害。（最多服用80个）'
    {
        "tc": "服用後凝練修士修為，增加210根骨、700點水系傷害。（最多服用80個）",
        "en": "Take to condense cultivator's Attainment, increasing 210 Strength and 700 Water Damage. (Max 80 can be taken)",
        "id": "Konsumsi untuk memadatkan Capaian praktisi, meningkatkan 210 Daya dan 700 Kerusakan Air. (Maks 80 dapat dikonsumsi)"
    },
    # 42: '不知何时被封存的至宝，已经化为了神珀一样的矿石，小心打开后90%概率获得随机1至3个至宝碎片，10%概率随机获得1个完整的至宝。'
    {
        "tc": "不知何時被封存的至寶，已經化為了神珀一樣的礦石，小心打開後90%概率獲得隨機1至3個至寶碎片，10%概率隨機獲得1個完整的至寶。",
        "en": "A supreme treasure sealed away at an unknown time, now turned into divine amber-like ore. Carefully open to have a 90% chance to obtain 1-3 random Supreme Treasure Shards, and a 10% chance to obtain 1 complete Supreme Treasure.",
        "id": "Harta karun tertinggi yang disegel pada waktu yang tidak diketahui, kini telah berubah menjadi bijih seperti ambar ilahi. Buka dengan hati-hati untuk mendapatkan 90% peluang memperoleh 1 hingga 3 Fragmen Harta Tertinggi acak, dan 10% peluang memperoleh 1 Harta Tertinggi utuh."
    },
    # 43: '名称：道场守卫\\n修为：大罗金仙六阶\\n修炼：1247年'
    {
        "tc": "名稱：道場守衛\\n修為：大羅金仙六階\\n修煉：1247年",
        "en": "Name: Dojo Guard\\nAttainment: Daluo Tier 6\\nCultivation: 1247 Years",
        "id": "Nama: Penjaga Dojo\\nCapaian: Daluo Tingkat 6\\nKultivasi: 1247 Tahun"
    },
    # 44: '晨息妙法'
    {
        "tc": "晨息妙法",
        "en": "Morning Breath Sutra",
        "id": "Sutra Napas Pagi"
    },
    # 45: '修炼年数：%s'
    {
        "tc": "修煉年數：%s",
        "en": "Cultivation Years: %s",
        "id": "Tahun Kultivasi: %s"
    },
    # 46: '珍宝灵珀'
    {
        "tc": "珍寶靈珀",
        "en": "Treasure Spirit Amber",
        "id": "Ambar Roh Harta"
    },
    # 47: '残冬天书'
    {
        "tc": "殘冬天書",
        "en": "Lingering Winter Heaven Book",
        "id": "Buku Surga Sisa Musim Dingin"
    },
    # 48: '服用后凝练修士修为，增加210身法、700点水系伤害。（最多服用80个）'
    {
        "tc": "服用後凝練修士修為，增加210身法、700點水系傷害。（最多服用80個）",
        "en": "Take to condense cultivator's Attainment, increasing 210 Agility and 700 Water Damage. (Max 80 can be taken)",
        "id": "Konsumsi untuk memadatkan Capaian praktisi, meningkatkan 210 Kelincahan dan 700 Kerusakan Air. (Maks 80 dapat dikonsumsi)"
    },
    # 49: '物品预览'
    {
        "tc": "物品預覽",
        "en": "Item Preview",
        "id": "Pratinjau Item"
    },
    # 50: '名称：道场守卫\\n修为：仙尊九阶\\n修炼：1234年'
    {
        "tc": "名稱：道場守衛\\n修為：仙尊九階\\n修煉：1234年",
        "en": "Name: Dojo Guard\\nAttainment: Deity Lord Tier 9\\nCultivation: 1234 Years",
        "id": "Nama: Penjaga Dojo\\nCapaian: Mahadewa Raja Tingkat 9\\nKultivasi: 1234 Tahun"
    },
    # 51: '活动道具，使用后论道大会挑战次数+1\\n获得后会自动使用\\n使用途径：论道大会'
    {
        "tc": "活動道具，使用後論道大會挑戰次數+1\\n獲得後會自動使用\\n使用途徑：論道大會",
        "en": "Event item. Use to increase Theory Assembly challenge attempts by 1.\\nAutomatically used upon acquisition.\\nHow to use: Theory Assembly",
        "id": "Item event, setelah digunakan jumlah tantangan Pertemuan Teori +1\\nAkan digunakan secara otomatis setelah diperoleh\\nCara penggunaan: Pertemuan Teori"
    },
    # 52: '1.诛仙阵为开服4天后的第1个周六开启，周五结束，九州商会为开服4天后第2个周六开启，周五结束，循环交替进行\\n2.诛仙阵内获得的兑换货币，可以积攒到下次活动开启使用（九州商会的商券会清空）\\n3.时光秘境每月1号开启，为赛季模式，赛季结束后秘境内招式、时之砂、标签和纳戒内道具会清空\\n4.地府判鬼每周二至周日开启，道友可在此兼任阎王之职，将鬼魂送入六道轮回\\n5.四季福地每月1号开启，为季度模式，每个季度将会获得不同的季节灵兽'
    {
        "tc": "1.誅仙陣為開服4天後的第1個週六開啟，週五結束，九州商會為開服4天後第2個週六開啟，週五結束，循環交替進行\\n2.誅仙陣內獲得的兌換貨幣，可以積攢到下次活動開啟使用（九州商會的商券會清空）\\n3.時光秘境每月1號開啟，為賽季模式，賽季結束後秘境內招式、時之砂、標籤和納戒內道具會清空\\n4.地府判鬼每週二至週日開啟，道友可在此兼任閻王之職，將鬼魂送入六道輪迴\\n5.四季福地每月1號開啟，為季度模式，每個季度將會獲得不同的季節靈獸",
        "en": "1. Deity Slain Array opens on the 1st Saturday 4 days after server launch and ends on Friday; Jiuzhou Commerce Chamber opens on the 2nd Saturday 4 days after server launch and ends on Friday, alternating in a cycle.\\n2. Exchange currency obtained in Deity Slain Array can be saved for the next event (Merchant Vouchers in Jiuzhou Commerce Chamber will be cleared).\\n3. Times Realm opens on the 1st of each month in season mode. After the season ends, moves, Sands of Time, tags, and items in the Ring in the realm will be cleared.\\n4. Nether Judge opens from Tuesday to Sunday. Cultivators can take on the role of King Yan here, sending ghosts into the Six Paths of Reincarnation.\\n5. Seasonal Domain opens on the 1st of each month in quarterly mode, granting different seasonal Pets each quarter.",
        "id": "1. Array Pengutuk Dewa dibuka pada hari Sabtu pertama 4 hari setelah server dibuka dan berakhir pada hari Jumat. Kamar Dagang Jiuzhou dibuka pada hari Sabtu ke-2 4 hari setelah server dibuka dan berakhir pada hari Jumat, bergantian secara berkala.\\n2. Mata uang penukaran yang diperoleh di Array Pengutuk Dewa dapat disimpan untuk digunakan pada event berikutnya (Kupon Dagang Kamar Dagang Jiuzhou akan dikosongkan).\\n3. Alam Alam Lain dibuka pada tanggal 1 setiap bulan dalam mode musim. Setelah musim berakhir, jurus, Pasir Waktu, label, dan item cincin penyimpanan di alam rahasia akan dikosongkan.\\n4. Hakim Nether dibuka setiap Selasa hingga Minggu. Rekan Taois dapat merangkap jabatan Raja Yan di sini untuk mengirim hantu ke Enam Alam Reinkarnasi.\\n5. Domain Musiman dibuka pada tanggal 1 setiap bulan dalam mode kuartal, dan Peliharaan musiman yang berbeda akan diperoleh setiap kuartal."
    },
    # 53: '飞翼霞凤'
    {
        "tc": "飛翼霞鳳",
        "en": "Winged Rosy Phoenix",
        "id": "Phoenix Sayap Fajar"
    },
    # 54: '使用后可获得随机植物种子。\\n包含：天青叶种子、血菩提种子、养魂花种子、七星花种子、金阳果种子、玉玄花种子、蕴道果种子、霓裳草种子、低级摇钱树、化龙草种子、忘忧果种子、高级摇钱树、低级仙玉树、高级仙元树、中级仙玉树'
    {
        "tc": "使用後可獲得隨機植物種子。\\n包含：天青葉種子、血菩提種子、養魂花種子、七星花種子、金陽果種子、玉玄花種子、蘊道果種子、霓裳草種子、低級搖錢樹、化龍草種子、忘憂果種子、高級搖錢樹、低級仙玉樹、高級仙元樹、中級仙玉樹",
        "en": "Use to obtain random plant seeds.\\nIncludes: Azure Leaf Seed, Blood Bodhi Seed, Soul Flower Seed, 7-Star Flower Seed, Golden Sun Fruit Seed, Jadeite Flower Seed, Tao Fruit Seed, Moon Grass Seed, Elementary Money Tree, Dragonify Grass Seed, Lotos Seed, Adv.Money Tree, Elementary Jade Tree, Adv.Divine Tree, Med.Jade Tree",
        "id": "Gunakan untuk mendapatkan benih tanaman acak.\\nTermasuk: Benih Daun Azure, Darah Bodhi Darah, Benih Bunga Jiwa, Benih Bunga Bintang 7, Benih Buah Golden, Benih Bunga Giok, Benih Buah Tao, Benih Rumput Bulan, Pohon Uang Dasar, Benih Rumput Dragonify, Benih Teratai, Adv.Pohon Uang, Pohon Giok Dasar, Adv.Pohon Ilahi, Kedokteran Batu Giok Giok"
    },
    # 55: '该玩家名帖已被屏蔽'
    {
        "tc": "該玩家名帖已被屏蔽",
        "en": "This player's name card has been blocked",
        "id": "Kartu nama pemain ini telah diblokir"
    },
    # 56: '使用后习得灵级破元神丹的炼制之法。（天品炼丹师方可使用）\\n破元神丹服用后提升真气和水系伤害。'
    {
        "tc": "使用後習得靈級破元神丹的煉製之法。（天品煉丹師方可使用）\\n破元神丹服用後提升真氣和水系傷害。",
        "en": "Use to learn G.Spirit Yuan-Breaking Divine Orb Refining. (Usable by G.Heaven Alchemist)\\nTaking Yuan-Breaking Divine Orb increases Qi and Water Damage.",
        "id": "Gunakan untuk mempelajari metode pemurnian G.Spirit Orb Ilahi Pemecah Yuan. (Dapat digunakan oleh Alkimis G.Surga)\\nKonsumsi Orb Ilahi Pemecah Yuan meningkatkan Qi dan Kerusakan Air."
    },
    # 57: '春潮心法'
    {
        "tc": "春潮心法",
        "en": "Spring Tide Mantra",
        "id": "Mantra Pasang Musim Semi"
    },
    # 58: '修行界初级功法需要<color=#458114>金丹</color>方可参悟\\n停车坐爱枫林晚，霜叶红于二月花。\\n效果：<color=#458114>修炼速度提升</color>'
    {
        "tc": "修行界初級功法需要<color=#458114>金丹</color>方可參悟\\n停車坐愛楓林晚，霜葉紅於二月花。\\n效果：<color=#458114>修煉速度提升</color>",
        "en": "Primary Cultivation World Technique requires <color=#458114>Formation</color> to comprehend\\nStopping the carriage, captivated by the maple grove at dusk; frosted leaves outshine the blossoms of early spring.\\nEffect: <color=#458114>Cultivation Speed Boost</color>",
        "id": "Teknik dasar Dunia Kultivasi memerlukan <color=#458114>Formasi</color> untuk dipahami\\nBerhenti sejenak menikmati hutan maple di kala senja, daun beku lebih merah dari bunga musim semi.\\nEfek: <color=#458114>Peningkatan Kecepatan Kultivasi</color>"
    },
    # 59: '灵级地藏神丹方'
    {
        "tc": "靈級地藏神丹方",
        "en": "G.Spirit Ksitigarbha Divine Orb Recipe",
        "id": "G.Resep Orb Ilahi Ksitigarbha"
    },
    # 60: '使用后将“蟾宫折桂”头像框加入衣阁。'
    {
        "tc": "使用後將「蟾宮折桂」頭像框加入衣閣。",
        "en": "Use to add \"Grasping the Laurel\" avatar frame to Closet.",
        "id": "Gunakan untuk menambahkan bingkai avatar \"Memetik Cabai di Istana Bulan\" ke Lemari."
    },
    # 61: '修行界顶级功法需要<color=#458114>太乙玉仙</color>方可参悟\\n效果：<color=#458114>防御提升</color>'
    {
        "tc": "修行界頂級功法需要<color=#458114>太乙玉仙</color>方可參悟\\n效果：<color=#458114>防禦提升</color>",
        "en": "Top Cultivation World Technique requires <color=#458114>Taiyi</color> to comprehend\\nEffect: <color=#458114>DEF Boost</color>",
        "id": "Teknik teratas Dunia Kultivasi memerlukan <color=#458114>Taiyi</color> untuk dipahami\\nEfek: <color=#458114>Peningkatan DEF</color>"
    },
    # 62: '秘宝仙珀'
    {
        "tc": "秘寶仙珀",
        "en": "Secret Treasure Immortal Amber",
        "id": "Ambar Abadi Harta Rahasia"
    },
    # 63: '1.商铺可用福玉兑换珍稀道具，剩余福玉永久保存。\\n2.商铺内商品无法加入购物车来快捷购买。'
    {
        "tc": "1.商鋪可用福玉兌換珍稀道具，剩餘福玉永久保存。\\n2.商鋪內商品無法加入購物車來快捷購買。",
        "en": "1. The shop allows exchanging Seasonal Jade for rare items; remaining Seasonal Jade is kept permanently.\\n2. Goods in the shop cannot be added to the shopping cart for quick purchase.",
        "id": "1. Toko dapat menggunakan Giok Musiman untuk menukar item langka, dan sisa Giok Musiman disimpan secara permanen.\\n2. Barang di toko tidak dapat ditambahkan ke keranjang belanja untuk pembelian cepat."
    },
    # 64: '拥有飞剑个数'
    {
        "tc": "擁有飛劍個數",
        "en": "Number of Flying Swords Owned",
        "id": "Jumlah Pedang Terbang yang Dimiliki"
    },
    # 65: '天下无敌'
    {
        "tc": "天下無敵",
        "en": "Invincible",
        "id": "Tak Terkalahkan"
    },
    # 66: '使用后习得灵级聚脉神丹的炼制之法。（天品炼丹师方可使用）\\n聚脉神丹服用后提升身法和金系伤害。'
    {
        "tc": "使用後習得靈級聚脈神丹的煉製之法。（天品煉丹師方可使用）\\n聚脈神丹服用後提升身法和金系傷害。",
        "en": "Use to learn G.Spirit Vein-Gathering Divine Orb Refining. (Usable by G.Heaven Alchemist)\\nTaking Vein-Gathering Divine Orb increases Agility and Metal Damage.",
        "id": "Gunakan untuk mempelajari metode pemurnian G.Spirit Orb Ilahi Pengumpul Urat. (Dapat digunakan oleh Alkimis G.Surga)\\nKonsumsi Orb Ilahi Pengumpul Urat meningkatkan Kelincahan dan Kerusakan Logam."
    },
    # 67: '打开后可从混沌鼎·碎片、聚宝盆·碎片、荒古破晓铃·碎片中任选一个'
    {
        "tc": "打開後可從混沌鼎·碎片、聚寶盆·碎片、荒古破曉鈴·碎片中任選一個",
        "en": "Open to select one from Cauldron of Chaos - Fragment, Treasure Basin - Fragment, or Bell of Dawn Shard",
        "id": "Buka untuk memilih salah satu dari Cauldron of Chaos -Fragmen, Harta Karun -Fragmen, atau Pecahan Lonceng Fajar"
    },
    # 68: '灵宝琥珀'
    {
        "tc": "靈寶琥珀",
        "en": "Spirit Treasure Amber",
        "id": "Ambar Harta Karun Roh"
    },
    # 69: '使用后获得灵兽：烛龙（同名灵兽只能拥有一个）'
    {
        "tc": "使用後獲得靈獸：燭龍（同名靈獸只能擁有一個）",
        "en": "Use to obtain Pet: Glint Dragon (You can only own one Pet of the same name)",
        "id": "Gunakan untuk memperoleh Peliharaan: Naga Kilauan (Hanya dapat memiliki satu Peliharaan dengan nama yang sama)"
    },
    # 70: '打开后可从归元宝树·主材，秘宝养成礼包和灵兽养成礼包众任选一个'
    {
        "tc": "打開後可從歸元寶樹·主材，秘寶養成禮包和靈獸養成禮包眾任選一個",
        "en": "Open to select one from Guiyuan Treasure Tree·Main Material, Secret Treasure Development Pack, or Pet Development Pack",
        "id": "Buka untuk memilih salah satu dari Pohon Harta Guiyuan·Material Utama, Paket Pengembangan Harta Rahasia, atau Paket Pengembangan Peliharaan"
    },
    # 71: '探路喽啰·盾'
    {
        "tc": "探路嘍囉·盾",
        "en": "Scout Minion · Shield",
        "id": "Kroco Pengintai · Perisai"
    },
    # 72: '灵级聚脉神丹'
    {
        "tc": "靈級聚脈神丹",
        "en": "G.Spirit Vein-Gathering Divine Orb",
        "id": "G.Spirit Orb Ilahi Pengumpul Urat"
    },
    # 73: '使用后可随机获得一本春潮功法。'
    {
        "tc": "使用後可隨機獲得一本春潮功法。",
        "en": "Use to randomly obtain a Spring Tide Technique book.",
        "id": "Gunakan untuk memperoleh buku Teknik Pasang Musim Semi secara acak."
    },
    # 74: '打开后，可获得灵兽口粮*500，涅槃丹*20'
    {
        "tc": "打開後，可獲得靈獸口糧*500，涅槃丹*20",
        "en": "Upon opening, you can obtain Pet Food*500, Nirvana Orb*20",
        "id": "Setelah dibuka, dapatkan Makanan Peliharaan*500, Orb Nirwana*20"
    },
    # 75: '打开后可从眠级明光神丹方、眠级三昧神丹方、眠级归源神丹方、眠级纯阳神丹方、眠级灵犀神丹方、眠级化元神丹方、眠级调和神丹方、眠级还真神丹方、眠级红莲神丹方、眠级定山神丹方中自选一个'
    {
        "tc": "打開後可從眠級明光神丹方、眠級三昧神丹方、眠級歸源神丹方、眠級純陽神丹方、眠級靈犀神丹方、眠級化元神丹方、眠級調和神丹方、眠級還真神丹方、眠級紅蓮神丹方、眠級定山神丹方中自選一個",
        "en": "Upon opening, you may select one from: G.Dormancy Bright Orb Recipe, G.Dormancy 3 Phase Divine Orb Recipe, G.Dormancy Origination Orb Recipe, G.Dormancy Pure Sun Orb Recipe, G.Dormancy Intimacy Orb Recipe, G.Dormancy Transform Orb Recipe, G.Dormancy Harmony Divine Orb Recipe, G.Dormancy Innocence Orb Recipe, G.Dormancy Red Lotus Divine Orb Recipe, G.Dormancy Mountain Orb Recipe.",
        "id": "Setelah dibuka, Anda dapat memilih salah satu dari: G.Resep Orb Cerah Dormansi, Resep Divine Orb G.Time 3 Fase, G.Resep Orb Asal Dormansi, G.Resep Orb Matahari Murni Dormansi, G.Resep Orb Keintiman Dormansi, G.Resep Orb Transformasi Dormansi, G.Resep Orb Ilahi Harmoni Dormansi, G.Resep Orb Dormancy Innocence, G.Resep Orb Ilahi Teratai Merah Dormansi, G.Resep Orb Gunung Dormansi."
    },
    # 76: '打开后，可获得灵石、食物、木材、陨铁各1000'
    {
        "tc": "打開後，可獲得靈石、食物、木材、隕鐵各1000",
        "en": "Upon opening, you can obtain 1000 each of Gem, Food, Wood, and Iron",
        "id": "Setelah dibuka, dapatkan masing-masing 1000 Permata, Makanan, Kayu, dan Besi"
    },
    # 77: '水调歌头礼包'
    {
        "tc": "水調歌頭禮包",
        "en": "Melody of the Moon Gift Pack",
        "id": "Paket Hadiah Senandung Melodi Air"
    },
    # 78: '残冬妙法'
    {
        "tc": "殘冬妙法",
        "en": "Lingering Winter Sutra",
        "id": "Sutra Sisa Musim Dingin"
    },
    # 79: '【三阶灵兽招式】参悟时，锁定词条不被刷新的专属道具，可通过四季福地玩法获取。'
    {
        "tc": "【三階靈獸招式】參悟時，鎖定詞條不被刷新的專屬道具，可通過四季福地玩法獲取。",
        "en": "Exclusive item to lock affixes from being refreshed during [Tier-3 Pet Move] comprehension. Can be obtained through Seasonal Domain gameplay.",
        "id": "Item eksklusif untuk mengunci atribut agar tidak disegarkan saat memahami [Jurus Peliharaan Tier 3], dapat diperoleh melalui gameplay Domain Musiman."
    },
    # 80: '名称：道场守卫\\n修为：合体五阶\\n修炼：1458年'
    {
        "tc": "名稱：道場守衛\\n修為：合體五階\\n修煉：1458年",
        "en": "Name: Dojo Guard\\nAttainment: Embodiment Tier 5\\nCultivation: 1458 Years",
        "id": "Nama: Penjaga Dojo\\nCapaian: Menjelma Tingkat 5\\nKultivasi: 1458 Tahun"
    },
    # 81: '红枫心法'
    {
        "tc": "紅楓心法",
        "en": "Red Maple Mantra",
        "id": "Mantra Maple Merah"
    },
    # 82: '今日刷新次数已达上限'
    {
        "tc": "今日刷新次數已達上限",
        "en": "Today's refresh attempts have reached the limit",
        "id": "Jumlah penyegaran hari ini telah mencapai batas"
    },
    # 83: '前往社区'
    {
        "tc": "前往社區",
        "en": "Go to Community",
        "id": "Buka Komunitas"
    },
    # 84: '福玉会在活动结束后清空，请尽快兑换'
    {
        "tc": "福玉會在活動結束後清空，請儘快兌換",
        "en": "Seasonal Jade will be cleared after the event ends, please exchange in time",
        "id": "Giok Musiman akan dikosongkan setelah event berakhir, harap tukarkan sesegera mungkin"
    },
    # 85: '灵级力透神丹'
    {
        "tc": "靈級力透神丹",
        "en": "G.Spirit Penetrating Divine Orb",
        "id": "G.Spirit Orb Ilahi Penembus Kekuatan"
    },
    # 86: '神秘的灵兽蛋，使用后有较大概率获得天级及以下灵兽蛋，较小概率获得稀有冬季灵兽-冰眸寒魄，小概率获得巽风鹫。'
    {
        "tc": "神秘的靈獸蛋，使用後有較大概率獲得天級及以下靈獸蛋，較小概率獲得稀有冬季靈獸-冰眸寒魄，小概率獲得巽風鷲。",
        "en": "A mysterious pet egg. Use to have a high chance of obtaining a G.Heaven or lower Pet Egg, a low chance of obtaining the rare winter Pet - Frost-Eye Cold Soul, and a very low chance of obtaining Xunfeng Vulture.",
        "id": "Telur peliharaan misterius, setelah digunakan memiliki peluang tinggi untuk mendapatkan Telur Peliharaan tingkat G.Surga atau lebih rendah, peluang kecil untuk mendapatkan Peliharaan musim dingin langka - Jiwa Dingin Mata Beku, dan peluang sangat kecil untuk mendapatkan Hering Xunfeng."
    },
    # 87: '名称：道场守卫\\n修为：元婴八阶\\n修炼：752年'
    {
        "tc": "名稱：道場守衛\\n修為：元嬰八階\\n修煉：752年",
        "en": "Name: Dojo Guard\\nAttainment: Nascence Tier 8\\nCultivation: 752 Years",
        "id": "Nama: Penjaga Dojo\\nCapaian: Nascence Tingkat 8\\nKultivasi: 752 Tahun"
    },
    # 88: '灵级奇火神丹'
    {
        "tc": "靈級奇火神丹",
        "en": "G.Spirit Mystic Fire Divine Orb",
        "id": "G.Spirit Api Mistik Divine Orb"
    },
    # 89: '服用后凝练修士修为，增加210体魄、700点木系伤害。（最多服用80个）'
    {
        "tc": "服用後凝練修士修為，增加210體魄、700點木系傷害。（最多服用80個）",
        "en": "Take to condense cultivator's Attainment, increasing 210 Health and 700 Wood Damage. (Max 80 can be taken)",
        "id": "Konsumsi untuk memadatkan Capaian praktisi, meningkatkan 210 Kesehatan dan 700 Kerusakan Kayu. (Maks 80 dapat dikonsumsi)"
    },
    # 90: '名称：道场守卫\\n修为：游仙八阶\\n修炼：1324年'
    {
        "tc": "名稱：道場守衛\\n修為：遊仙八階\\n修煉：1324年",
        "en": "Name: Dojo Guard\\nAttainment: Wanderer Tier 8\\nCultivation: 1324 Years",
        "id": "Nama: Penjaga Dojo\\nCapaian: Tualang Tingkat 8\\nKultivasi: 1324 Tahun"
    },
    # 91: '灵级御水神丹'
    {
        "tc": "靈級御水神丹",
        "en": "G.Spirit Water-Control Divine Orb",
        "id": "G.Spirit Orb Ilahi Pengendali Air"
    },
    # 92: '使用后将“冰封霜狼”法相加入衣阁。'
    {
        "tc": "使用後將「冰封霜狼」法相加入衣閣。",
        "en": "Use to add \"Frost-Bound Wolf\" Deity Form to Closet.",
        "id": "Gunakan untuk menambahkan Pendewaan \"Serigala Es Pembeku\" ke Lemari."
    },
    # 93: '清扫仙果核：<color=#458114>%s/%s</color>\\n领取王母馈赠：<color=#458114>%s/%s</color>'
    {
        "tc": "清掃仙果核：<color=#458114>%s/%s</color>\\n領取王母饋贈：<color=#458114>%s/%s</color>",
        "en": "Clean Immortal Fruit Cores: <color=#458114>%s/%s</color>\\nClaim Queen Mother's Gift: <color=#458114>%s/%s</color>",
        "id": "Membersihkan Inti Buah Abadi: <color=#458114>%s/%s</color>\\nKlaim Hadiah Ibu Suri: <color=#458114>%s/%s</color>"
    },
    # 94: '锁定消耗'
    {
        "tc": "鎖定消耗",
        "en": "Lock Cost",
        "id": "Konsumsi Kunci"
    },
    # 95: '名称：道场守卫\\n修为：游仙九阶\\n修炼：1234年'
    {
        "tc": "名稱：道場守衛\\n修為：遊仙九階\\n修煉：1234年",
        "en": "Name: Dojo Guard\\nAttainment: Wanderer Tier 9\\nCultivation: 1234 Years",
        "id": "Nama: Penjaga Dojo\\nCapaian: Tualang Tingkat 9\\nKultivasi: 1234 Tahun"
    },
    # 96: '使用后习得灵级紫阳神丹的炼制之法。（天品炼丹师方可使用）\\n紫阳神丹服用后提升根骨和金系伤害。'
    {
        "tc": "使用後習得靈級紫陽神丹的煉製之法。（天品煉丹師方可使用）\\n紫陽神丹服用後提升根骨和金系傷害。",
        "en": "Use to learn G.Spirit Purple Sun Divine Orb Refining. (Usable by G.Heaven Alchemist)\\nTaking Purple Sun Divine Orb increases Strength and Metal Damage.",
        "id": "Gunakan untuk mempelajari metode pemurnian G.Spirit Matahari Ungu Divine Orb. (Dapat digunakan oleh Alkimis G.Surga)\\nKonsumsi Matahari Ungu Divine Orb meningkatkan Daya dan Kerusakan Logam."
    },
    # 97: '道场禁制'
    {
        "tc": "道場禁制",
        "en": "Dojo Restriction",
        "id": "Larangan Dojo"
    },
    # 98: '云梦大泽之畔，水灵根修炼者的圣地。后为妖魔所忌惮，在异族联手的阴谋围剿中，战乱不休，尸骸枯骨不计其数，仿若炼狱。'
    {
        "tc": "雲夢大澤之畔，水靈根修煉者的聖地。後為妖魔所忌憚，在異族聯手的陰謀圍剿中，戰亂不休，屍骸枯骨不計其數，仿若煉獄。",
        "en": "By the shores of the Great Yunmeng Marsh lies a sacred land for Water Spirit Root cultivators. Later feared by demons and besieged in a conspiracy by allied foreign races, endless warfare ensued, leaving countless corpses and bones behind, like a living purgatory.",
        "id": "Di tepi Rawa Besar Yunmeng, merupakan tempat suci bagi para praktisi Akar Roh Air. Kemudian ditakuti oleh monster dan iblis, dalam pengepungan konspirasi bersama oleh ras asing, perang berkecamuk tanpa henti, mayat dan tulang tak terhitung jumlahnya, layaknya api penyucian."
    },
    # 99: '名称：道场守卫\\n修为：大罗金仙四阶\\n修炼：1324年'
    {
        "tc": "名稱：道場守衛\\n修為：大羅金仙四階\\n修煉：1324年",
        "en": "Name: Dojo Guard\\nAttainment: Daluo Tier 4\\nCultivation: 1324 Years",
        "id": "Nama: Penjaga Dojo\\nCapaian: Daluo Tingkat 4\\nKultivasi: 1324 Tahun"
    },
    # 100: '货币资源'
    {
        "tc": "貨幣資源",
        "en": "Currency Resources",
        "id": "Sumber Daya Mata Uang"
    },
    # 101: '草药矿石'
    {
        "tc": "草藥礦石",
        "en": "Herbs & Minerals",
        "id": "Herba & Bijih"
    },
    # 102: '养成材料'
    {
        "tc": "養成材料",
        "en": "Development Materials",
        "id": "Material Pengembangan"
    },
    # 103: '天地五行五灵之力，在特殊条件下聚合而成，使用后金、木、水、火、土五行伤害各增加1000点'
    {
        "tc": "天地五行五靈之力，在特殊條件下聚合而成，使用後金、木、水、火、土五行傷害各增加1000點",
        "en": "Power of heaven and earth's five elements and five spirits, aggregated under special conditions. Upon use, Metal, Wood, Water, Fire, and Earth 5-Element Damage are each increased by 1000.",
        "id": "Kekuatan lima elemen dan lima roh langit dan bumi, terkumpul dalam kondisi khusus. Setelah digunakan, kerusakan 5 elemen Logam, Kayu, Air, Api, dan Tanah masing-masing meningkat 1000 poin."
    },
    # 104: '红枫遁术'
    {
        "tc": "紅楓遁術",
        "en": "Red Maple Escape Art",
        "id": "Seni Pelarian Maple Merah"
    },
    # 105: '挑战令'
    {
        "tc": "挑戰令",
        "en": "Challenge Token",
        "id": "Token Tantangan"
    },
    # 106: '积分保护中'
    {
        "tc": "積分保護中",
        "en": "Point Protection Active",
        "id": "Perlindungan Poin Aktif"
    },
    # 107: '使用后将“天下无敌”称号加入衣阁。\\n（<color=#458114>“论道大会”限时外观，下个赛季前回收</color>）'
    {
        "tc": "使用後將「天下無敵」稱號加入衣閣。\\n（<color=#458114>「論道大會」限時外觀，下個賽季前回收</color>）",
        "en": "Use to add \"Invincible\" title to Closet.\\n(<color=#458114>\"Theory Assembly\" time-limited cosmetic, will be recycled before next season</color>)",
        "id": "Gunakan untuk menambahkan gelar \"Tak Terkalahkan\" ke Lemari.\\n(<color=#458114>Tampilan berbatas waktu \"Pertemuan Teori\", akan ditarik kembali sebelum musim berikutnya</color>)"
    },
    # 108: '【获取途径】'
    {
        "tc": "【獲取途徑】",
        "en": "[How to Obtain]",
        "id": "[Cara Memperoleh]"
    },
    # 109: '传说中神秘、敏捷和灵性的化身，拥有龙族的锐利牙齿和火焰般炽热的气息，可以喷吐出强大而毁灭性的火焰。同时具备神鹿般优雅迅捷的奔跑能力，在林间跳跃时仿佛飘逸舞动。'
    {
        "tc": "傳說中神秘、敏捷和靈性的化身，擁有龍族的銳利牙齒和火焰般熾熱的氣息，可以噴吐出強大而毀滅性的火焰。同時具備神鹿般優雅迅捷的奔跑能力，在林間跳躍時彷彿飄逸舞動。",
        "en": "The incarnation of mystery, agility, and spirituality in legend, possessing the sharp teeth and flaming breath of dragons, capable of exhaling powerful and destructive flames. It also possesses the graceful and swift running ability of a divine deer, leaping through forests as if dancing with elegance.",
        "id": "Inkarnasi misteri, kelincahan, dan spiritualitas dalam legenda, memiliki gigi tajam naga dan nafas sehangat api, mampu menghembuskan api yang kuat dan menghancurkan. Pada saat yang sama, ia memiliki kemampuan berlari yang anggun dan cepat seperti rusa dewa, melompat di antara pepohonan seolah menari dengan anggun."
    },
    # 110: '凶兽来袭'
    {
        "tc": "兇獸來襲",
        "en": "Beasts Strike",
        "id": "Binatang Buas Menyerang"
    },
    # 111: '次数：'
    {
        "tc": "次數：",
        "en": "Attempts: ",
        "id": "Jumlah: "
    },
    # 112: '红枫灵本'
    {
        "tc": "紅楓靈本",
        "en": "Red Maple Codex",
        "id": "Codex Maple Merah"
    },
    # 113: '使用后可在聊天设置中选择“战神”装扮。'
    {
        "tc": "使用後可在聊天設置中選擇「戰神」裝扮。",
        "en": "Use to select \"War God\" outfit in chat settings.",
        "id": "Gunakan untuk memilih pakaian \"Dewa Perang\" di pengaturan obrolan."
    },
    # 114: '轮回之境已扫荡'
    {
        "tc": "輪迴之境已掃蕩",
        "en": "Realm of Circles swept",
        "id": "Alam Lingkaran telah disapu"
    }
]

assert len(item_translations) == len(chunk_items), f"Mismatch count: {len(item_translations)} vs {len(chunk_items)}"

result = {}
for i, key in enumerate(chunk_items):
    result[key] = item_translations[i]

# --- VALIDATION SUITE ---
errors = []

# 1. Check count
if len(result) != len(chunk_items):
    errors.append(f"Count mismatch: result has {len(result)}, chunk_items has {len(chunk_items)}")

# 2. Check keys
for idx, key in enumerate(chunk_items):
    if key not in result:
        errors.append(f"Missing key #{idx}: {repr(key)}")

# 3. Check subkeys & tags/placeholders/newlines
ph_pattern = re.compile(r'%[0-9]*\.?[0-9]*[sdf]|%s/%s|%%')
color_pattern = re.compile(r'<color=#[0-9a-fA-F]{6}>|</color>')

for orig, trans in result.items():
    for lang in ['tc', 'en', 'id']:
        if lang not in trans or not trans[lang]:
            errors.append(f"Empty or missing '{lang}' in {repr(orig)}")
            continue
        
        val = trans[lang]
        
        # Newline count (check literal '\\n' count)
        orig_nl = orig.count('\\n')
        val_nl = val.count('\\n')
        if orig_nl != val_nl:
            errors.append(f"Literal \\n mismatch in {lang} for {repr(orig)}: orig has {orig_nl}, got {val_nl}")
        
        # Check no raw ascii newline introduced
        if '\n' in val:
            errors.append(f"Raw ascii newline found in {lang} for {repr(orig)}")
        
        # Color tags
        orig_colors = color_pattern.findall(orig)
        val_colors = color_pattern.findall(val)
        if orig_colors != val_colors:
            errors.append(f"Color tag mismatch in {lang} for {repr(orig)}: orig {orig_colors} vs val {val_colors}")
        
        # Placeholders
        orig_phs = ph_pattern.findall(orig)
        val_phs = ph_pattern.findall(val)
        if orig_phs != val_phs:
            errors.append(f"Placeholder mismatch in {lang} for {repr(orig)}: orig {orig_phs} vs val {val_phs}")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for e in errors[:20]:
        print("  -", e)
else:
    print("ALL VALIDATION CHECKS PASSED PERFECTLY!")
    out_path = r'F:\项目\无极国际版\result_chunk_4.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(result)} items to {out_path}")
