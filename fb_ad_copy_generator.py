import random
import pyperclip
import os

class FacebookAdGenerator:
    def __init__(self):
        self.attention_grabbers = [
            "🔥 Dah penat dengan {pain_point}?",
            "💡 Nak tau macam mana nak {benefit}?",
            "🚨 Jom stop {pain_point} hari ni!",
            "👉 Korang nak {benefit} tak?",
            "⚡ Akhirnya! Ada penyelesaian untuk {pain_point}",
            "🎯 Eh, korang tau tak macam mana nak {benefit}?",
            "💪 Dah cuba macam-macam tapi masih {pain_point}?",
            "🌟 Nak transform {pain_point} jadi kejayaan?",
            "📢 Pengumuman! Cara terbaru untuk {benefit}",
            "🎉 Ready tak nak {benefit}?"
        ]
        
        self.pain_points = [
            "sales tak naik-naik",
            "kerja manual yang membazir masa",
            "pelanggan lari ke competitor",
            "marketing tak konsisten",
            "terlepas peluang dapat customer",
            "bisnes tak boleh scale",
            "tak cukup leads",
            "website tak convert",
            "kos marketing tinggi tapi result kurang",
            "social media engagement rendah"
        ]
        
        self.benefits = [
            "double kan sales korang",
            "jimat masa 10 jam seminggu",
            "dapat customer yang premium",
            "scale kan bisnes dengan mudah",
            "tingkatkan conversion rate",
            "automatikan sistem marketing",
            "dapatkan leads berkualiti",
            "kurangkan kos iklan",
            "jadi expert dalam industri",
            "bina brand yang power"
        ]
        
        self.features = [
            "sistem yang terbukti berkesan",
            "framework step-by-step",
            "teknik revolutionary",
            "strategi game-changing",
            "sistem yang lengkap",
            "formula rahsia",
            "blueprint eksklusif",
            "sistem autopilot",
            "method yang telah dioptimize",
            "platform all-in-one"
        ]
        
        self.social_proof = [
            "Dah ada 10,000+ customer yang berjaya",
            "Digunakan oleh brand-brand top Malaysia",
            "95% customer satisfied dengan result",
            "Dipercayai oleh pakar industri",
            "Featured dalam BFM dan The Star",
            "Lebih 1,000 success stories",
            "Testimonial positive tak putus-putus",
            "ROI minimum 300% guaranteed",
            "Track record 5 tahun dalam industri",
            "Award winning system"
        ]
        
        self.ctas = [
            "Klik Sini Untuk Info Lanjut →",
            "Jom Mula Sekarang 🚀",
            "Grab Tempat Anda ✨",
            "Download Guide Percuma 📚",
            "Book Demo Skang 🎯",
            "DM 'INFO' Untuk Details 📱",
            "Klik Link Dalam Bio 👆",
            "Join Sekarang! Limited Slot! 🏃",
            "Daftar Sebelum Harga Naik ⚡",
            "Whatsapp Kami Untuk Offer 💬"
        ]

    def generate_aida_formula(self):
        """Attention, Interest, Desire, Action formula"""
        attention = random.choice(self.attention_grabbers).format(
            pain_point=random.choice(self.pain_points),
            benefit=random.choice(self.benefits)
        )
        interest = f"Kenalkan {random.choice(self.features)} yang boleh bantu korang {random.choice(self.benefits)}."
        desire = random.choice(self.social_proof)
        action = random.choice(self.ctas)
        return f"{attention}\n\n{interest}\n\n{desire}\n\n{action}"

    def generate_pas_formula(self):
        """Problem, Agitation, Solution formula"""
        problem = f"Korang ada masalah {random.choice(self.pain_points)}?"
        agitation = f"Setiap hari yang berlalu, korang terlepas peluang untuk {random.choice(self.benefits)}."
        solution = f"{random.choice(self.features)} adalah jawapannya. {random.choice(self.social_proof)}.\n\n{random.choice(self.ctas)}"
        return f"{problem}\n\n{agitation}\n\n{solution}"

    def generate_bab_formula(self):
        """Before, After, Bridge formula"""
        before = f"Masih {random.choice(self.pain_points)}?"
        after = f"Bayangkan kalau korang boleh {random.choice(self.benefits)}"
        bridge = f"{random.choice(self.features)} akan bantu korang! {random.choice(self.social_proof)}.\n\n{random.choice(self.ctas)}"
        return f"{before}\n\n{after}\n\n{bridge}"

    def generate_fomo_formula(self):
        """Fear Of Missing Out formula"""
        urgency = f"⏰ Last call! Limited slot je lagi!"
        problem = f"Ramai yang dah {random.choice(self.benefits)}"
        solution = f"Jangan tunggu lagi. {random.choice(self.features)} akan transform bisnes korang.\n\n{random.choice(self.ctas)}"
        return f"{urgency}\n\n{problem}\n\n{solution}"

    def generate_star_formula(self):
        """Situation, Task, Action, Result formula"""
        situation = f"Kalau korang {random.choice(self.pain_points)}"
        task = f"Korang perlukan sistem yang boleh {random.choice(self.benefits)}"
        action = f"Dengan {random.choice(self.features)}"
        result = f"{random.choice(self.social_proof)}\n\n{random.choice(self.ctas)}"
        return f"{situation}\n\n{task}\n\n{action}\n\n{result}"

    def generate_pppp_formula(self):
        """Picture, Promise, Prove, Push formula"""
        picture = f"Bayangkan bisnes korang boleh {random.choice(self.benefits)}"
        promise = f"Dengan {random.choice(self.features)}, semua ni possible!"
        prove = random.choice(self.social_proof)
        push = random.choice(self.ctas)
        return f"{picture}\n\n{promise}\n\n{prove}\n\n{push}"

    def generate_variants(self, count=10):
        formulas = [
            self.generate_aida_formula,
            self.generate_pas_formula,
            self.generate_bab_formula,
            self.generate_fomo_formula,
            self.generate_star_formula,
            self.generate_pppp_formula
        ]
        variants = []
        
        for i in range(count):
            formula = random.choice(formulas)
            ad_copy = formula()
            variants.append({
                'number': i + 1,
                'content': ad_copy,
                'display': f"Iklan {i+1}:\n{'='*40}\n{ad_copy}\n{'='*40}\n"
            })
            
        return variants

def clear_screen():
    print("\033[H\033[J", end="")

def main():
    generator = FacebookAdGenerator()
    variants = generator.generate_variants()
    
    while True:
        clear_screen()
        print("Variasi Copy Iklan Facebook:\n")
        for variant in variants:
            print(variant['display'])
        
        print("\nMenu:")
        print("1-10: Salin iklan yang dipilih")
        print("R: Jana iklan baru")
        print("Q: Keluar")
        
        choice = input("\nPilihan anda: ").strip().upper()
        
        if choice == 'Q':
            print("Terima kasih! Jumpa lagi! 👋")
            break
        elif choice == 'R':
            variants = generator.generate_variants()
        elif choice.isdigit() and 1 <= int(choice) <= 10:
            index = int(choice) - 1
            if index < len(variants):
                pyperclip.copy(variants[index]['content'])
                print(f"\n✅ Iklan {choice} telah disalin ke clipboard!")
                input("\nTekan Enter untuk teruskan...")
            else:
                print("\n❌ Nombor iklan tidak sah!")
                input("\nTekan Enter untuk teruskan...")
        else:
            print("\n❌ Pilihan tidak sah! Sila cuba lagi.")
            input("\nTekan Enter untuk teruskan...")

if __name__ == "__main__":
    main()
