# -*- coding: utf-8 -*-
import json
import re

# Load source chunk_5.json
with open(r'F:\项目\无极国际版\chunk_5.json', 'r', encoding='utf-8') as f:
    source_list = json.load(f)

print(f"Total source items: {len(source_list)}")

translations = {
    "至宝神珀": {
        "tc": "至寶神珀",
        "en": "Ultimate Treasure Divine Amber",
        "id": "Harta Karun Tertinggi Amber Ilahi"
    },
    "灵级灼日神丹": {
        "tc": "靈級灼日神丹",
        "en": "Spirit Grade Scorching Sun Divine Orb",
        "id": "Spirit Grade Orb Ilahi Matahari Terik"
    },
    "洞窟魔物·恒": {
        "tc": "洞窟魔物·恆",
        "en": "Cave Monster · Eternal",
        "id": "Monster Gua · Abadi"
    },
    "冰眸寒魄可以领悟到尖牙、矫健、潜伏、凶神血裔、朱鬣、机警、烟水、火咒、岩咒、木咒、气刃、五行结界": {
        "tc": "冰眸寒魄可以領悟到尖牙、矯健、潛伏、凶神血裔、朱鬣、機警、煙水、火咒、岩咒、木咒、氣刃、五行結界",
        "en": "Ice Eye Frost Soul is able to learn Piercing Fang, Agile, Stealth, Savage Blood, Red Mane, Vigilant, Smoke Water, Fire Curse, Stone Curse, Wood Curse, Blade Wave, 5-Element Border.",
        "id": "Ice Eye Frost Soul dapat mempelajari Piercing Fang, Agile, Stealth, Savage Blood, Red Mane, Vigilant, Smoke Water, Fire Curse, Stone Curse, Wood Curse, Blade Wave, 5-Element Border."
    },
    "貔貅可以领悟到尖牙、潜伏、兽血沸腾、凶神血裔、朱鬣、机警、雷界、火咒、水咒、岩咒、木咒、五行结界": {
        "tc": "貔貅可以領悟到尖牙、潛伏、獸血沸騰、凶神血裔、朱鬣、機警、雷界、火咒、水咒、岩咒、木咒、五行結界",
        "en": "Pixiu is able to learn Piercing Fang, Stealth, Bloodlust, Savage Blood, Red Mane, Vigilant, Thunder Bound, Fire Curse, Water Curse, Stone Curse, Wood Curse, 5-Element Border.",
        "id": "Pixiu dapat mempelajari Piercing Fang, Stealth, Bloodlust, Savage Blood, Red Mane, Vigilant, Thunder Bound, Fire Curse, Water Curse, Stone Curse, Wood Curse, 5-Element Border."
    },
    "传说中神秘而华丽的怪物，它拥有雄伟而壮观的双翼，头部呈现出凤凰般高贵和威严之态，眼神中透着智慧和灵性。凤善于飞行，在天空中翱翔时展现出无与伦比的优雅和自由。它能够自如地穿梭于云雾之间，将阳光映射在羽毛上形成美丽夺目的色彩。": {
        "tc": "傳說中神秘而華麗的怪物，牠擁有雄偉而壯觀的雙翼，頭部呈現出鳳凰般高貴和威嚴之態，眼神中透著智慧和靈性。鳳善於飛行，在天空中翱翔時展現出無與倫比的優雅和自由。牠能夠自如地穿梭於雲霧之間，將陽光映射在羽毛上形成美麗奪目的色彩。",
        "en": "A legendary mysterious and gorgeous creature, it possesses magnificent and spectacular wings, with a head displaying the noble and majestic demeanor of a phoenix, and eyes brimming with wisdom and spirituality. The Phoenix excels at flying, displaying unparalleled elegance and freedom as it soars across the sky. It can freely shuttle among clouds and mist, reflecting sunlight upon its feathers to create stunning, dazzling colors.",
        "id": "Makhluk misterius dan anggun dalam legenda, memiliki sayap yang megah dan spektakuler, kepalanya menunjukkan keagungan dan wibawa bagaikan burung phoenix, dan tatapan matanya memancarkan kebijaksanaan dan kecerdasan spiritual. Feng pandai terbang, menunjukkan keanggunan dan kebebasan yang tiada tara saat melayang di angkasa. Ia mampu meluncur bebas di antara kabut dan awan, memantulkan sinar matahari pada bulunya untuk membentuk warna-warni yang indah dan memukau."
    },
    "神秘的灵兽蛋，使用后有较大概率获得天级及以下灵兽蛋，较小概率获得稀有秋季灵兽-貔貅，小概率获得巽风鹫。": {
        "tc": "神秘的靈獸蛋，使用後有較大概率獲得天級及以下靈獸蛋，較小概率獲得稀有秋季靈獸-貔貅，小概率獲得巽風鷲。",
        "en": "Mysterious Pet Egg. Use to have a high chance to obtain a G.Heaven or below Pet Egg, a smaller chance to obtain rare Autumn Pet - Pixiu, and a slight chance to obtain Xunfeng Vulture.",
        "id": "Telur Peliharaan Misterius. Gunakan untuk memiliki peluang besar memperoleh Telur Peliharaan G.Surga atau ke bawah, peluang lebih kecil memperoleh Peliharaan Musim Gugur Langka - Pixiu, dan peluang kecil memperoleh Hering Xunfeng."
    },
    "四季福地-凶兽-冬": {
        "tc": "四季福地-兇獸-冬",
        "en": "Seasonal Domain - Ferocious Beast - Winter",
        "id": "Domain Musiman - Binatang Buas - Musim Dingin"
    },
    "冰眸寒魄": {
        "tc": "冰眸寒魄",
        "en": "Ice Eye Frost Soul",
        "id": "Ice Eye Frost Soul"
    },
    "使用后习得灵级地藏神丹的炼制之法。（天品炼丹师方可使用）\\n地藏神丹服用后提升身法和土系伤害。": {
        "tc": "使用後習得靈級地藏神丹的煉製之法。（天品煉丹師方可使用）\\n地藏神丹服用後提升身法和土系傷害。",
        "en": "Use to learn Spirit Grade Ksitigarbha Divine Orb Refining.(Usable by G.Heaven Alchemist)\\nTaking Ksitigarbha Divine Orb increases Agility and Earth DMG.",
        "id": "Gunakan untuk mempelajari metode pemurnian Spirit Grade Orb Ilahi Ksitigarbha.(Dapat digunakan oleh Alkemis G.Surga)\\nMengonsumsi Orb Ilahi Ksitigarbha meningkatkan Kelincahan dan DMG Bumi."
    },
    "使用后习得灵级力透神丹的炼制之法。（天品炼丹师方可使用）\\n力透神丹服用后提升真气和金系伤害。": {
        "tc": "使用後習得靈級力透神丹的煉製之法。（天品煉丹師方可使用）\\n力透神丹服用後提升真氣和金系傷害。",
        "en": "Use to learn Spirit Grade Piercing Force Divine Orb Refining.(Usable by G.Heaven Alchemist)\\nTaking Piercing Force Divine Orb increases Qi and Metal DMG.",
        "id": "Gunakan untuk mempelajari metode pemurnian Spirit Grade Orb Ilahi Penembus Kekuatan.(Dapat digunakan oleh Alkemis G.Surga)\\nMengonsumsi Orb Ilahi Penembus Kekuatan meningkatkan Qi dan DMG Logam."
    },
    "随机秘宝碎片-红色": {
        "tc": "隨機秘寶碎片-紅色",
        "en": "Random Secret Treasure Shard - Red",
        "id": "Serpihan Harta Rahasia Acak - Merah"
    },
    "凶兽礼盒-冬": {
        "tc": "兇獸禮盒-冬",
        "en": "Ferocious Beast Gift Box - Winter",
        "id": "Kotak Hadiah Binatang Buas - Musim Dingin"
    },
    "伏暑灵本": {
        "tc": "伏暑靈本",
        "en": "Midsummer Spirit Tome",
        "id": "Kitab Roh Penahan Panas"
    },
    "内务物资礼包（大）": {
        "tc": "內務物資禮包（大）",
        "en": "Internal Affairs Supplies Gift Pack (Large)",
        "id": "Paket Hadiah Pasokan Urusan Internal (Besar)"
    },
    "每日：%s": {
        "tc": "每日：%s",
        "en": "Daily: %s",
        "id": "Harian: %s"
    },
    "打开后，可获得日月精粹*300，洪荒精魄*30": {
        "tc": "打開後，可獲得日月精粹*300，洪荒精魄*30",
        "en": "Open to obtain Sun and Moon Essence*300, Chaos Essence*30",
        "id": "Buka untuk memperoleh Inti dari Matahari dan Bulan*300, Esensi Kekacauan*30"
    },
    "通关详情": {
        "tc": "通關詳情",
        "en": "Clear Details",
        "id": "Detail Penyelesaian"
    },
    "【修正效果】：%s": {
        "tc": "【修正效果】：%s",
        "en": "[Correction Effect]: %s",
        "id": "[Efek Koreksi]: %s"
    },
    "祝贺道友本赛季论道大会荣誉上榜，位列前10名，名传三界，威名赫赫。": {
        "tc": "祝賀道友本賽季論道大會榮譽上榜，位列前10名，名傳三界，威名赫赫。",
        "en": "Congratulations Fellow Taoist on being honorably ranked in this season's Theory Assembly, placing in the top 10, renowned across the Three Realms with illustrious fame.",
        "id": "Selamat kepada Rekan Tao telah terdaftar secara terhormat di Pertemuan Teori musim ini, menempati peringkat 10 besar, terkenal di Tiga Alam dengan ketenaran yang termasyhur."
    },
    "平心叶": {
        "tc": "平心葉",
        "en": "Serenity Leaf",
        "id": "Daun Penenang Hati"
    },
    "仙塾悟道说明：\\n1.灵童境界达到<炼虚一阶后>开启仙塾悟道功能\\n2.悟道时间为：每周一至周五，周六日休息\\n3.周一至周五设置不同的悟道类型，所增加的属性类型也不一样\\n4.每个灵童每天选择仙帝或者道祖班进行悟道（每天只有一次选择机会，不能更改）\\n5.仙塾悟道属性会根据灵童资质转化为人物属性\\n6.辅导—赠送<color=#ad2228>悟道法球</color>可缩短悟道时间。注：悟道加速次数<color=#ad2228>次日重置，不做保留</color>。（如悟道持续跨天，次日使用悟道法球，则消耗<color=#ad2228>当天使用次数</color>。悟道开启当天次数<color=#ad2228>不会保留跨天</color>。）\\n7灵童每次悟道会获得1学分，学分用于学分榜排名，学分每周日22点清空\\n8.学分榜罗列本周所有悟道灵童的排名（根据学分高低排名，相同学分按达成时间先后排序）\\n9.学分榜每周日22点重置，学分榜奖励每周六24点发放（每个上榜灵童都可获得一份奖励）\\n10.悟道事件跟随本次悟道，本次悟道结束后会清除\\n11.灵童继承时：仙塾属性也会继承": {
        "tc": "仙塾悟道說明：\\n1.靈童境界達到<煉虛一階後>開啟仙塾悟道功能\\n2.悟道時間為：每週一至週五，週六日休息\\n3.週一至週五設置不同的悟道類型，所增加的屬性類型也不一樣\\n4.每個靈童每天選擇仙帝或者道祖班進行悟道（每天只有一次選擇機會，不能更改）\\n5.仙塾悟道屬性會根據靈童資質轉化為人物屬性\\n6.輔導—贈送<color=#ad2228>悟道法球</color>可縮短悟道時間。注：悟道加速次數<color=#ad2228>次日重置，不做保留</color>。（如悟道持續跨天，次日使用悟道法球，則消耗<color=#ad2228>當天使用次數</color>。悟道開啟當天次數<color=#ad2228>不會保留跨天</color>。）\\n7.靈童每次悟道會獲得1學分，學分用於學分榜排名，學分每週日22點清空\\n8.學分榜羅列本周所有悟道靈童的排名（根據學分高低排名，相同學分按達成時間先後排序）\\n9.學分榜每週日22點重置，學分榜獎勵每週六24點發放（每個上榜靈童都可獲得一份獎勵）\\n10.悟道事件跟隨本次悟道，本次悟道結束後會清除\\n11.靈童繼承時：仙塾屬性也會繼承",
        "en": "Instructions for Enlightenment in Fairy School:\\n1.Open the function of Enlightenment of Fairy School after reaching <Vainify G.1>\\n2.Enlightenment Time: Monday to Friday, rest on Saturday and Sunday\\n3.Set different enlightenment types from Monday to Friday, and the added attribute types will also be different\\n4.Each Fairchild chooses Deity Emperor Class or Tao Ancestor Class for enlightenment every day (there is only one chance to choose every day and can't be changed)\\n5.Fairy School enlightenment attributes will be converted into character attributes according to the Fairchild's quality\\n6.Tutoring—Gifting <color=#ad2228>Enlightenment Orb</color> can shorten Enlightenment time. Note: Enlightenment speed-up attempts <color=#ad2228>reset next day and are not retained</color>. (If Enlightenment spans across days and an Enlightenment Orb is used the next day, it will consume <color=#ad2228>the attempts of that day</color>. The attempts on the day Enlightenment starts <color=#ad2228>will not be retained across days</color>.)\\n7.Fairchild will get 1 credit for each enlightenment, which will be used for Credit Ranking. The credits will be cleared at 22:00 every Sunday\\n8.The Credit Ranking lists the rankings of all enlightenment Fairchild this week (ranked by credits, the same credits are ranked according to the time of achievement)\\n9.The Credit Ranking is reset at 22:00 every Sunday, and rewards of Credit Ranking are issued at 24:00 every Saturday (each Fairchild on the list can get a reward)\\n10.Enlightenment events follow this enlightenment and will be cleared when enlightenment ends\\n11.When the Fairchild inherits: Fairy School attributes will also be inherited",
        "id": "Petunjuk Pencerahan di Sekolah Peri:\\n1.Buka fungsi Pencerahan Sekolah Peri setelah mencapai <Vainify G.1>\\n2.Waktu Pencerahan: Senin sampai Jumat, istirahat pada hari Sabtu dan Minggu\\n3.Tetapkan jenis pencerahan yang berbeda dari Senin hingga Jumat, dan jenis atribut yang ditambahkan juga akan berbeda\\n4.Setiap Bocahan memilih Kelas Kaisar Dewa atau Kelas Leluhur Tao untuk pencerahan setiap hari (hanya ada satu kesempatan untuk memilih setiap hari dan tidak dapat diubah)\\n5.Atribut pencerahan Sekolah Peri akan diubah menjadi atribut karakter sesuai dengan kualitas Bocahan\\n6.Bimbingan—Memberikan <color=#ad2228>Bola Pencerahan</color> dapat mempersingkat waktu Pencerahan. Catatan: Jumlah percepatan Pencerahan <color=#ad2228>direset keesokan harinya dan tidak disimpan</color>. (Jika Pencerahan berlanjut melintasi hari dan Bola Pencerahan digunakan pada hari berikutnya, maka akan menghabiskan <color=#ad2228>jumlah penggunaan hari itu</color>. Jumlah pada hari dimulainya Pencerahan <color=#ad2228>tidak akan disimpan melintasi hari</color>.)\\n7.Bocahan akan mendapatkan 1 kredit untuk setiap pencerahan, yang akan digunakan untuk Peringkat Kredit. Kredit akan dihapus pada pukul 22:00 setiap hari Minggu\\n8.Peringkat Kredit mencantumkan peringkat semua pencerahan Bocahan minggu ini (berdasarkan kredit, kredit yang sama diberi peringkat berdasarkan waktu pencapaian)\\n9.Peringkat Kredit disetel ulang pada pukul 22:00 setiap hari Minggu, dan hadiah Peringkat Kredit diberikan pada pukul 24:00 setiap hari Sabtu (setiap Bocahan dalam daftar dapat memperoleh hadiah)\\n10.Peristiwa Pencerahan mengikuti pencerahan ini dan akan dihapus saat pencerahan berakhir\\n11.Saat Bocahan mewarisi: atribut Sekolah Peri juga akan diwariskan"
    },
    "获得<color=#4f9a12>%s</color>个%s\\n": {
        "tc": "獲得<color=#4f9a12>%s</color>個%s\\n",
        "en": "Obtained <color=#4f9a12>%s</color> %s\\n",
        "id": "Mendapatkan <color=#4f9a12>%s</color> %s\\n"
    },
    "扫荡次数已达上限": {
        "tc": "掃蕩次數已達上限",
        "en": "Sweep attempts have reached the limit",
        "id": "Jumlah sapuan telah mencapai batas maksimum"
    },
    "四季福地福玉": {
        "tc": "四季福地福玉",
        "en": "Seasonal Domain Fortune Jade",
        "id": "Giok Berkah Domain Musiman"
    },
    "福地等级：%s": {
        "tc": "福地等級：%s",
        "en": "Blessed Land Level: %s",
        "id": "Tingkat Tanah Berkah: %s"
    },
    "名称：道场守卫\\n修为：合体三阶\\n修炼：1012年": {
        "tc": "名稱：道場守衛\\n修為：合體三階\\n修煉：1012年",
        "en": "Name: Dojo Guard\\nAttainment: Embodiment G.3\\nPractice: 1012 years",
        "id": "Nama: Penjaga Dojo\\nCapaian: Menjelma G.3\\nLatihan: 1012 tahun"
    },
    "名称：道场守卫\\n修为：天仙一阶\\n修炼：1754年": {
        "tc": "名稱：道場守衛\\n修為：天仙一階\\n修煉：1754年",
        "en": "Name: Dojo Guard\\nAttainment: Heaven Deity G.1\\nPractice: 1754 years",
        "id": "Nama: Penjaga Dojo\\nCapaian: Dewa Surgawi G.1\\nLatihan: 1754 tahun"
    },
    "本赛季": {
        "tc": "本賽季",
        "en": "Current Season",
        "id": "Musim Ini"
    },
    "龙血果": {
        "tc": "龍血果",
        "en": "Dragon Blood Fruit",
        "id": "Buah Darah Naga"
    },
    "启灵+%s %s": {
        "tc": "啟靈+%s %s",
        "en": "Enlighten +%s %s",
        "id": "Pencerahan +%s %s"
    },
    "残冬神术": {
        "tc": "殘冬神術",
        "en": "Lingering Winter Divine Art",
        "id": "Seni Ilahi Sisa Musim Dingin"
    },
    "五行五灵丹": {
        "tc": "五行五靈丹",
        "en": "Five Elements Five Spirits Orb",
        "id": "Orb Lima Roh 5-Elemen"
    },
    "祝贺道友本赛季论道大会荣誉上榜，位列前500名，名传三界，威名赫赫。": {
        "tc": "祝賀道友本賽季論道大會榮譽上榜，位列前500名，名傳三界，威名赫赫。",
        "en": "Congratulations Fellow Taoist on being honorably ranked in this season's Theory Assembly, placing in the top 500, renowned across the Three Realms with illustrious fame.",
        "id": "Selamat kepada Rekan Tao telah terdaftar secara terhormat di Pertemuan Teori musim ini, menempati peringkat 500 besar, terkenal di Tiga Alam dengan ketenaran yang termasyhur."
    },
    "祝贺道友本赛季论道大会荣誉上榜，位列前300名，名传三界，威名赫赫。": {
        "tc": "祝賀道友本賽季論道大會榮譽上榜，位列前300名，名傳三界，威名赫赫。",
        "en": "Congratulations Fellow Taoist on being honorably ranked in this season's Theory Assembly, placing in the top 300, renowned across the Three Realms with illustrious fame.",
        "id": "Selamat kepada Rekan Tao telah terdaftar secara terhormat di Pertemuan Teori musim ini, menempati peringkat 300 besar, terkenal di Tiga Alam dengan ketenaran yang termasyhur."
    },
    "每日限购：%s": {
        "tc": "每日限購：%s",
        "en": "Daily Purchase Limit: %s",
        "id": "Batas Beli Harian: %s"
    },
    "排名：%s": {
        "tc": "排名：%s",
        "en": "Rank: %s",
        "id": "Peringkat: %s"
    },
    "段位奖励：首次达到对应段位后发放": {
        "tc": "段位獎勵：首次達到對應段位後發放",
        "en": "Tier Reward: Issued after reaching the corresponding tier for the first time",
        "id": "Hadiah Tingkat: Diberikan setelah mencapai tingkat yang sesuai untuk pertama kali"
    },
    "我的积分：%s": {
        "tc": "我的積分：%s",
        "en": "My Points: %s",
        "id": "Poin Saya: %s"
    },
    "已达最大锁定数量": {
        "tc": "已達最大鎖定數量",
        "en": "Maximum locked count reached",
        "id": "Telah mencapai jumlah kunci maksimum"
    },
    "1. 建议仔细对比属性效果，再替换\\n2. 想保留的原属性，可用明悟砂锁定\\n3. 最多同时锁定三个词条不被替换\\n4. 锁定词条个数越多，消耗明悟砂越多": {
        "tc": "1. 建議仔細對比屬性效果，再替換\\n2. 想保留的原屬性，可用明悟砂鎖定\\n3. 最多同時鎖定三個詞條不被替換\\n4. 鎖定詞條個數越多，消耗明悟砂越多",
        "en": "1. It is recommended to carefully compare attribute effects before replacing\\n2. Use Sand of Enlightenment to lock original attributes you wish to keep\\n3. Up to three affixes can be locked at the same time to avoid being replaced\\n4. The more affixes locked, the more Sand of Enlightenment is consumed",
        "id": "1. Disarankan membandingkan efek atribut dengan cermat sebelum mengganti\\n2. Gunakan Pasir Pencerahan untuk mengunci atribut asli yang ingin dipertahankan\\n3. Maksimal mengunci tiga entri sekaligus agar tidak tergantikan\\n4. Semakin banyak entri yang dikunci, semakin banyak Pasir Pencerahan yang dikonsumsi"
    },
    "待参悟": {
        "tc": "待參悟",
        "en": "To Be Comprehended",
        "id": "Menunggu Pemahaman"
    },
    "无属性": {
        "tc": "無屬性",
        "en": "None Attribute",
        "id": "Tanpa Atribut"
    },
    "参悟技能": {
        "tc": "參悟技能",
        "en": "Comprehend Skill",
        "id": "Pahami Keterampilan"
    },
    "%s月福地": {
        "tc": "%s月福地",
        "en": "%s Month Blessed Land",
        "id": "Tanah Berkah Bulan %s"
    },
    "【三阶灵兽招式】参悟专属道具之一，可通过四季福地玩法获取。\\n【参悟神焰】刷新招式属性词条概率：\\n绿色：<color=#008000>44.6%</color>        蓝色：<color=#0000FF>37.5%</color>\\n紫色：<color=#9400D3>13.4%</color>        橙色：<color=#FF8C00>2.7%</color>\\n红色：<color=#FF0000>1.8%</color>": {
        "tc": "【三階靈獸招式】參悟專屬道具之一，可通過四季福地玩法獲取。\\n【參悟神焰】刷新招式屬性詞條概率：\\n綠色：<color=#008000>44.6%</color>        藍色：<color=#0000FF>37.5%</color>\\n紫色：<color=#9400D3>13.4%</color>        橙色：<color=#FF8C00>2.7%</color>\\n紅色：<color=#FF0000>1.8%</color>",
        "en": "[G.3 Pet Skill] One of the exclusive comprehension items, obtainable from Seasonal Domain gameplay.\\n[Comprehension Divine Flame] Chance to refresh skill attribute affixes:\\nGreen: <color=#008000>44.6%</color>        Blue: <color=#0000FF>37.5%</color>\\nPurple: <color=#9400D3>13.4%</color>        Orange: <color=#FF8C00>2.7%</color>\\nRed: <color=#FF0000>1.8%</color>",
        "id": "[Jurus Peliharaan G.3] Salah satu item eksklusif pemahaman, dapat diperoleh dari gameplay Domain Musiman.\\n[Api Ilahi Pemahaman] Peluang memperbarui entri atribut jurus:\\nHijau: <color=#008000>44.6%</color>        Biru: <color=#0000FF>37.5%</color>\\nUngu: <color=#9400D3>13.4%</color>        Oranye: <color=#FF8C00>2.7%</color>\\nMerah: <color=#FF0000>1.8%</color>"
    },
    "一身墨绿长袍，腰佩长刀，干净利落，显得她英气勃发": {
        "tc": "一身墨綠長袍，腰佩長刀，乾淨俐落，顯得她英氣勃發",
        "en": "Dressed in a dark green robe with a saber at her waist, neat and brisk, she radiates heroic spirit.",
        "id": "Mengenakan jubah hijau tua dengan pedang panjang di pinggang, rapi dan cekatan, memancarkan aura kepahlawanan yang gagah berani."
    },
    "使用后习得灵级灼日神丹的炼制之法。（天品炼丹师方可使用）\\n灼日神丹服用后提升真气和火系伤害。": {
        "tc": "使用後習得靈級灼日神丹的煉製之法。（天品煉丹師方可使用）\\n灼日神丹服用後提升真氣和火系傷害。",
        "en": "Use to learn Spirit Grade Scorching Sun Divine Orb Refining.(Usable by G.Heaven Alchemist)\\nTaking Scorching Sun Divine Orb increases Qi and Fire DMG.",
        "id": "Gunakan untuk mempelajari metode pemurnian Spirit Grade Orb Ilahi Matahari Terik.(Dapat digunakan oleh Alkemis G.Surga)\\nMengonsumsi Orb Ilahi Matahari Terik meningkatkan Qi dan DMG Api."
    },
    "使用后将“声名远扬”称号加入衣阁。": {
        "tc": "使用後將“聲名遠揚”稱號加入衣閣。",
        "en": "Use to add \"Renowned\" title into closet.",
        "id": "Gunakan untuk menambahkan gelar \"Reputasi yang luas\" ke dalam lemari."
    },
    "春潮功法礼包": {
        "tc": "春潮功法禮包",
        "en": "Spring Tide Technique Gift Pack",
        "id": "Paket Hadiah Teknik Pasang Musim Semi"
    },
    "随机灵兽蛋-冬": {
        "tc": "隨機靈獸蛋-冬",
        "en": "Random Pet Egg - Winter",
        "id": "Telur Peliharaan Acak - Musim Dingin"
    },
    "灵兽蛋·飞翼霞凤": {
        "tc": "靈獸蛋·飛翼霞鳳",
        "en": "Pet Egg · Winged Dawn Phoenix",
        "id": "Telur Peliharaan · Phoenix Cahaya Bersayap"
    },
    "仙界大能炼制，天帝特供，服用后能增加180点机缘。（最多服用100个）": {
        "tc": "仙界大能煉製，天帝特供，服用後能增加180點機緣。（最多服用100個）",
        "en": "Refined by mighty beings of Celestial Realm, specially supplied for Heavenly Emperor. Increases Opportunity by 180 upon taking.(Max 100 uses)",
        "id": "Dimurnikan oleh tokoh hebat Alam Abadi, pasokan khusus untuk Kaisar Langit. Mengonsumsi dapat meningkatkan 180 Peluang.(Maksimal 100 kali)"
    },
    "灵级焚天神丹方": {
        "tc": "靈級焚天神丹方",
        "en": "Spirit Grade Burning Sky Divine Orb Recipe",
        "id": "Resep Orb Ilahi Pembakar Langit Spirit Grade"
    },
    "灵级破浪神丹方": {
        "tc": "靈級破浪神丹方",
        "en": "Spirit Grade Wave Breaking Divine Orb Recipe",
        "id": "Resep Orb Ilahi Pemecah Gelombang Spirit Grade"
    },
    "使用后习得灵级水生神丹的炼制之法。（天品炼丹师方可使用）\\n水生神丹服用后提升体魄和水系伤害。": {
        "tc": "使用後習得靈級水生神丹的煉製之法。（天品煉丹師方可使用）\\n水生神丹服用後提升體魄和水系傷害。",
        "en": "Use to learn Spirit Grade Water Born Divine Orb Refining.(Usable by G.Heaven Alchemist)\\nTaking Water Born Divine Orb increases Health and Water DMG.",
        "id": "Gunakan untuk mempelajari metode pemurnian Spirit Grade Orb Ilahi Kelahiran Air.(Dapat digunakan oleh Alkemis G.Surga)\\nMengonsumsi Orb Ilahi Kelahiran Air meningkatkan Kesehatan dan DMG Air."
    },
    "打开后，可获得灵石、食物、木材、陨铁各5000": {
        "tc": "打開後，可獲得靈石、食物、木材、隕鐵各5000",
        "en": "Open to obtain 5,000 Gems, Food, Wood, and Iron each",
        "id": "Buka untuk memperoleh masing-masing 5.000 Permata, Makanan, Kayu, dan Besi"
    },
    "灵级水生神丹": {
        "tc": "靈級水生神丹",
        "en": "Spirit Grade Water Born Divine Orb",
        "id": "Spirit Grade Orb Ilahi Kelahiran Air"
    },
    "服用后凝练修士修为，增加210体魄、700点水系伤害。（最多服用80个）": {
        "tc": "服用後凝練修士修為，增加210體魄、700點水系傷害。（最多服用80個）",
        "en": "Able to condense the attainment, increase Health by 210 and Water DMG by 700.(Max 80 can be used)",
        "id": "Mampu memadatkan Capaian, meningkatkan Kesehatan sebesar 210 dan DMG Air sebesar 700.(Maks 80 dapat digunakan)"
    },
    "服用后凝练修士修为，增加210根骨、700点土系伤害。（最多服用80个）": {
        "tc": "服用後凝練修士修為，增加210根骨、700點土系傷害。（最多服用80個）",
        "en": "Able to condense the attainment, increase Strength by 210 and Earth DMG by 700.(Max 80 can be used)",
        "id": "Mampu memadatkan Capaian, meningkatkan Daya sebesar 210 dan DMG Bumi sebesar 700.(Maks 80 dapat digunakan)"
    },
    "服用后凝练修士修为，增加210真气、700点土系伤害。（最多服用80个）": {
        "tc": "服用後凝練修士修為，增加210真氣、700點土系傷害。（最多服用80個）",
        "en": "Able to condense the attainment, increase Qi by 210 and Earth DMG by 700.(Max 80 can be used)",
        "id": "Mampu memadatkan Capaian, meningkatkan Qi sebesar 210 dan DMG Bumi sebesar 700.(Maks 80 dapat digunakan)"
    },
    "服用后凝练修士修为，增加210真气、700点火系伤害。（最多服用80个）": {
        "tc": "服用後凝練修士修為，增加210真氣、700點火系傷害。（最多服用80個）",
        "en": "Able to condense the attainment, increase Qi by 210 and Fire DMG by 700.(Max 80 can be used)",
        "id": "Mampu memadatkan Capaian, meningkatkan Qi sebesar 210 dan DMG Api sebesar 700.(Maks 80 dapat digunakan)"
    },
    "春潮神术": {
        "tc": "春潮神術",
        "en": "Spring Tide Divine Art",
        "id": "Seni Ilahi Pasang Musim Semi"
    },
    "春潮": {
        "tc": "春潮",
        "en": "Spring Tide",
        "id": "Pasang Musim Semi"
    },
    "灵级化血神丹": {
        "tc": "靈級化血神丹",
        "en": "Spirit Grade Blood Transforming Divine Orb",
        "id": "Spirit Grade Orb Ilahi Pengubah Darah"
    },
    "服用后凝练修士修为，增加210身法、700点火系伤害。（最多服用80个）": {
        "tc": "服用後凝練修士修為，增加210身法、700點火系傷害。（最多服用80個）",
        "en": "Able to condense the attainment, increase Agility by 210 and Fire DMG by 700.(Max 80 can be used)",
        "id": "Mampu memadatkan Capaian, meningkatkan Kelincahan sebesar 210 dan DMG Api sebesar 700.(Maks 80 dapat digunakan)"
    },
    "1、每次叛教后再选择，会推荐3个门派供道友选择\\n2、道友可消耗威望刷新，每天有3次刷新次数\\n3、每次刷新会再推荐3个门派（没有新门派会出现重复的推荐）": {
        "tc": "1、每次叛教後再選擇，會推薦3個門派供道友選擇\\n2、道友可消耗威望刷新，每天有3次刷新次數\\n3、每次刷新會再推薦3個門派（沒有新門派會出現重複的推薦）",
        "en": "1. Each time after betraying sect to choose again, 3 sects will be recommended for Fellow Taoist to choose\\n2. Fellow Taoist can spend Prestige to refresh, with 3 refresh attempts daily\\n3. Each refresh will recommend 3 sects again (if there are no new sects, duplicate recommendations will appear)",
        "id": "1. Setiap kali setelah berkhianat sekte untuk memilih lagi, 3 sekte akan direkomendasikan untuk dipilih Rekan Tao\\n2. Rekan Tao dapat menggunakan Prestise untuk menyegarkan, dengan 3 kali kesempatan penyegaran setiap hari\\n3. Setiap penyegaran akan merekomendasikan 3 sekte lagi (jika tidak ada sekte baru, rekomendasi berulang akan muncul)"
    },
    "使用后将“妙笔生花”头像框加入衣阁。": {
        "tc": "使用後將“妙筆生花”頭像框加入衣閣。",
        "en": "Use to add \"Gifted Brush\" Avatar Frame into closet.",
        "id": "Gunakan untuk menambahkan bingkai avatar \"Kuas Ajaib\" ke dalam lemari."
    },
    "已通关": {
        "tc": "已通關",
        "en": "Cleared",
        "id": "Selesai"
    },
    "地阶初级": {
        "tc": "地階初級",
        "en": "G.Earth Primary",
        "id": "G.Earth Pemula"
    },
    "地阶高级": {
        "tc": "地階高級",
        "en": "G.Earth Adv.",
        "id": "G.Earth Lanjutan"
    },
    "黄阶初级": {
        "tc": "黃階初級",
        "en": "G.Novice Primary",
        "id": "G.Pemula Dasar"
    },
    "黄阶高级": {
        "tc": "黃階高級",
        "en": "G.Novice Adv.",
        "id": "G.Pemula Lanjutan"
    },
    "天阶初级": {
        "tc": "天階初級",
        "en": "G.Heaven Primary",
        "id": "G.Surga Pemula"
    },
    "天阶高级": {
        "tc": "天階高級",
        "en": "G.Heaven Adv.",
        "id": "G.Surga Lanjutan"
    },
    "玄阶初级": {
        "tc": "玄階初級",
        "en": "G.Mythic Primary",
        "id": "G.Mistik Pemula"
    },
    "玄阶高级": {
        "tc": "玄階高級",
        "en": "G.Mythic Adv.",
        "id": "G.Mistik Lanjutan"
    },
    "武神": {
        "tc": "武神",
        "en": "War God",
        "id": "Dewa Perang"
    },
    "禁制": {
        "tc": "禁制",
        "en": "Restriction",
        "id": "Larangan"
    },
    "礼包": {
        "tc": "禮包",
        "en": "Gift Pack",
        "id": "Paket Hadiah"
    },
    "胜利": {
        "tc": "勝利",
        "en": "Victory",
        "id": "Kemenangan"
    },
    "败": {
        "tc": "敗",
        "en": "Defeat",
        "id": "Kekalahan"
    },
    "段位提升": {
        "tc": "段位提升",
        "en": "Tier Up",
        "id": "Tingkat Naik"
    },
    "赛季冠军": {
        "tc": "賽季冠軍",
        "en": "Season Champion",
        "id": "Juara Musim"
    },
    "论道榜": {
        "tc": "論道榜",
        "en": "Theory Rankings",
        "id": "Peringkat Teori"
    },
    "灵运": {
        "tc": "靈運",
        "en": "Spirit Fortune",
        "id": "Keberuntungan Roh"
    },
    "仙册·春": {
        "tc": "仙冊·春",
        "en": "Immortal Book · Spring",
        "id": "Buku Abadi · Musim Semi"
    },
    "仙册·夏": {
        "tc": "仙冊·夏",
        "en": "Immortal Book · Summer",
        "id": "Buku Abadi · Musim Panas"
    },
    "仙册·秋": {
        "tc": "仙冊·秋",
        "en": "Immortal Book · Autumn",
        "id": "Buku Abadi · Musim Gugur"
    },
    "仙册·冬": {
        "tc": "仙冊·冬",
        "en": "Immortal Book · Winter",
        "id": "Buku Abadi · Musim Dingin"
    },
    "完成福地挑战任务领取丰厚奖励！": {
        "tc": "完成福地挑戰任務領取豐厚獎勵！",
        "en": "Complete Blessed Land challenge quests to claim rich rewards!",
        "id": "Selesaikan misi tantangan tanah berkah untuk mengklaim hadiah berlimpah!"
    },
    "新功能开启": {
        "tc": "新功能開啟",
        "en": "New Function Unlocked",
        "id": "Fungsi Baru Dibuka"
    },
    "便捷分解": {
        "tc": "便捷分解",
        "en": "Quick Disassemble",
        "id": "Bongkar Cepat"
    }
}

# Validation checks
missing_keys = [k for k in source_list if k not in translations]
if missing_keys:
    print(f"ERROR: Missing keys ({len(missing_keys)}): {missing_keys}")
else:
    print("SUCCESS: All 93 source keys are present in translations!")

extra_keys = [k for k in translations if k not in source_list]
if extra_keys:
    print(f"ERROR: Extra keys ({len(extra_keys)}): {extra_keys}")
else:
    print("SUCCESS: No extra keys in translations!")

# Check placeholders (%s, %d, etc.), tags (<color=...>, </color>), and newlines (\\n)
errors = []
for k in source_list:
    item = translations[k]
    # Check placeholders in original
    phs = re.findall(r'%[0-9]*\.?[0-9]*[sdf]', k)
    # Check tags in original
    color_tags = re.findall(r'<color=#[0-9a-fA-F]+>', k)
    close_tags = re.findall(r'</color>', k)
    # Check newlines in original
    nl_count = k.count('\\n')

    for lang in ['tc', 'en', 'id']:
        val = item[lang]
        # Check placeholders
        val_phs = re.findall(r'%[0-9]*\.?[0-9]*[sdf]', val)
        if val_phs != phs:
            errors.append(f"[{lang}] Placeholder mismatch in {repr(k)}: expected {phs}, got {val_phs}")
        # Check color tags
        val_ctags = re.findall(r'<color=#[0-9a-fA-F]+>', val)
        val_closes = re.findall(r'</color>', val)
        if val_ctags != color_tags:
            errors.append(f"[{lang}] Color tags mismatch in {repr(k)}: expected {color_tags}, got {val_ctags}")
        if len(val_closes) != len(close_tags):
            errors.append(f"[{lang}] Close tags count mismatch in {repr(k)}: expected {len(close_tags)}, got {len(val_closes)}")
        # Check newline counts
        val_nl_count = val.count('\\n')
        if val_nl_count != nl_count:
            errors.append(f"[{lang}] Newline count mismatch in {repr(k)}: expected {nl_count}, got {val_nl_count}")

if errors:
    print(f"VALIDATION ERRORS ({len(errors)}):")
    for e in errors:
        print("  -", e)
else:
    print("SUCCESS: All placeholders, tags, and newlines strictly match!")

# Write out result_chunk_5.json
out_path = r'F:\项目\无极国际版\result_chunk_5.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"Saved result_chunk_5.json to {out_path} with {len(translations)} entries.")
