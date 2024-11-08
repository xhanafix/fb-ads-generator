import random

class FacebookAdGenerator:
    def __init__(self):
        self.headlines = [
            "𝗠𝗘𝗝𝗔 𝗟𝗜𝗣𝗔𝗧 𝗣𝗢𝗥𝗧𝗔𝗕𝗟𝗘 𝗬𝗔𝗡𝗚 𝗦𝗘𝗥𝗕𝗔𝗚𝗨𝗡𝗔! 🔥",
            "𝗠𝗘𝗝𝗔 𝗦𝗘𝗥𝗕𝗔𝗚𝗨𝗡𝗔 𝗨𝗡𝗧𝗨𝗞 𝗥𝗨𝗠𝗔𝗛 𝗔𝗡𝗗𝗔! 👍",
            "𝗠𝗘𝗝𝗔 𝗣𝗢𝗥𝗧𝗔𝗕𝗟𝗘 𝗬𝗔𝗡𝗚 𝗠𝗨𝗗𝗔𝗛 𝗗𝗜𝗕𝗔𝗪𝗔! 💪",
            "𝗠𝗘𝗝𝗔 𝗟𝗜𝗣𝗔𝗧 𝗬𝗔𝗡𝗚 𝗦𝗧𝗬𝗟𝗜𝗦𝗛 & 𝗣𝗥𝗔𝗞𝗧𝗜𝗞𝗔𝗟! ✨",
            "𝗠𝗘𝗝𝗔 𝗦𝗔𝗠𝗣𝗜𝗡𝗚 𝗬𝗔𝗡𝗚 𝗠𝗘𝗡𝗝𝗜𝗠𝗔𝗧𝗞𝗔𝗡 𝗥𝗨𝗔𝗡𝗚! 🎯",
            "𝗠𝗘𝗝𝗔 𝗣𝗢𝗥𝗧𝗔𝗕𝗟𝗘 𝗠𝗨𝗟𝗧𝗜𝗙𝗨𝗡𝗚𝗦𝗜! 🌟",
            "𝗠𝗘𝗝𝗔 𝗟𝗜𝗣𝗔𝗧 𝗬𝗔𝗡𝗚 𝗠𝗢𝗗𝗘𝗥𝗡 & 𝗞𝗨𝗔𝗧! 💯",
            "𝗠𝗘𝗝𝗔 𝗦𝗔𝗠𝗣𝗜𝗡𝗚 𝗬𝗔𝗡𝗚 𝗠𝗨𝗗𝗔𝗛 𝗗𝗜𝗦𝗜𝗠𝗣𝗔𝗡! 📦",
            "𝗠𝗘𝗝𝗔 𝗣𝗢𝗥𝗧𝗔𝗕𝗟𝗘 𝗨𝗡𝗧𝗨𝗞 𝗦𝗘𝗠𝗨𝗔 𝗞𝗘𝗚𝗨𝗡𝗔𝗔𝗡! 🎊",
            "𝗠𝗘𝗝𝗔 𝗟𝗜𝗣𝗔𝗧 𝗬𝗔𝗡𝗚 𝗕𝗘𝗥𝗞𝗨𝗔𝗟𝗜𝗧𝗜! ⭐"
        ]
        
        self.testimonials = [
            '"Sangat berguna untuk WFH! Mudah lipat dan simpan bila tak guna" ENCIK ADAM - SHAH ALAM',
            '"Best sangat meja ni, ringan tapi kukuh. Boleh bawa kemana-mana!" PUAN SARAH - KL',
            '"Design simple tapi cantik, sesuai dengan ruang rumah moden" KAK LISA - PUTRAJAYA',
            '"Memang berbaloi dengan harga. Kualiti terjamin!" ENCIK RAHMAN - JOHOR',
            '"Perfect untuk laptop dan kerja. Ketinggian pun sesuai" PUAN AMINAH - SELANGOR',
            '"Senang nak bawa masa travel, ringan je!" ENCIK FAIZ - MELAKA',
            '"Material premium, tak mudah rosak. Highly recommended!" KAK WAN - PERAK',
            '"Sesuai untuk semua kegunaan, value for money!" ENCIK SYAFIQ - PENANG',
            '"Design minimalis, sesuai dengan rumah moden" PUAN LINDA - SABAH',
            '"Memang puas hati dengan kualiti meja ni!" ENCIK ZACK - SARAWAK'
        ]
        
        self.benefits = [
            "👉 Material Premium & Tahan Lasak",
            "👉 Mudah Dilipat & Disimpan",
            "👉 Ringan & Senang Dibawa",
            "👉 Design Minimalis & Moden",
            "👉 Sesuai Untuk Pelbagai Kegunaan",
            "👉 Ketinggian Yang Ergonomik",
            "👉 Jimat Ruang Penyimpanan",
            "👉 Pemasangan Tanpa Alat",
            "👉 Permukaan Anti Calar",
            "👉 Kaki Anti Gelincir"
        ]
        
        self.bonuses = [
            "🎁 Percuma Beg Pembawa Eksklusif",
            "🎁 Percuma Penghantaran Ke Seluruh Malaysia",
            "🎁 Percuma Pad Anti Gelincir",
            "🎁 Percuma Warranty 1 Tahun",
            "🎁 Percuma Panduan Penjagaan",
            "🎁 Percuma Gift Misteri",
            "🎁 Percuma Cloth Pembersih Premium",
            "🎁 Percuma Sticker Hiasan",
            "🎁 Percuma Adjustment Pad",
            "🎁 Percuma After Sales Support"
        ]

        self.closings = [
            "P/S : Stok Terhad! Dapatkan Sekarang Dengan Harga Promosi 🔥",
            "P/S : Lebih 1000+ Unit Terjual Dengan Review 5 Bintang ⭐",
            "P/S : Jaminan Kepuasan Atau Wang Dikembalikan 💯",
            "P/S : Promosi Terhad Untuk 50 Unit Pertama Sahaja!",
            "P/S : Free Shipping Ke Seluruh Malaysia 🚚",
            "P/S : Harga Promosi Untuk Masa Terhad Sahaja!",
            "P/S : Stok Terhad Untuk Bulan Ini! Grab It Fast 🏃",
            "P/S : Dapatkan Bonus Bernilai RM99 Secara Percuma!",
            "P/S : Ready Stock! Same Day Delivery Available 📦",
            "P/S : COD Available Untuk Sekitar Klang Valley 🚗"
        ]

    def generate_ad_copy(self, business_name, whatsapp_link):
        headline = random.choice(self.headlines)
        testimonial = random.choice(self.testimonials)
        closing = random.choice(self.closings)
        
        # Randomly select 5-7 benefits
        selected_benefits = random.sample(self.benefits, random.randint(5, 7))
        # Randomly select 3-4 bonuses
        selected_bonuses = random.sample(self.bonuses, random.randint(3, 4))
        
        ad_copy = f"{headline} {business_name}? 😍\n\n"
        ad_copy += ".\n.\n.\n\n"
        ad_copy += f"{testimonial}\n\n"
        ad_copy += "𝗞𝗘𝗡𝗔𝗣𝗔 𝗔𝗡𝗗𝗔 𝗣𝗘𝗥𝗟𝗨 𝗠𝗜𝗟𝗜𝗞𝗜 𝗠𝗘𝗝𝗔 𝗣𝗢𝗥𝗧𝗔𝗕𝗟𝗘 𝗜𝗡𝗜? 🤔\n\n"
        
        for benefit in selected_benefits:
            ad_copy += f"{benefit}\n"
            
        ad_copy += "\n𝗕𝗢𝗡𝗨𝗦 𝗜𝗦𝗧𝗜𝗠𝗘𝗪𝗔 𝗨𝗡𝗧𝗨𝗞 𝗔𝗡𝗗𝗔! 🎁\n\n"
        
        for bonus in selected_bonuses:
            ad_copy += f"{bonus}\n"
            
        ad_copy += f"\n{closing} 🤗\n\n"
        ad_copy += "Berminat Untuk Dapatkan Meja Portable Ini? 🥰\n\n"
        ad_copy += "Klik Link Atau Button 𝗪𝗮𝘀𝗮𝗽 Di Bawah 𝗦𝗘𝗞𝗔𝗥𝗔𝗡𝗚! 👇👇\n\n"
        
        for _ in range(3):
            ad_copy += f"{whatsapp_link}\n\n"
            
        return ad_copy
