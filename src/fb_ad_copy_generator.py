import random

class FBAdCopyGenerator:
    def __init__(self):
        self.hooks = [
            "🤯 Kisah sebenar yang ramai tak tahu...",
            "😱 Dulu saya pun macam korang...",
            "💭 Pernah tak rasa macam ni?",
            "🔥 Baru je semalam ada customer share pengalaman dia...",
            "⚡ Plot twist yang tak disangka!",
            "💝 Nak kongsi sesuatu yang special dengan korang...",
            "🎯 Untuk korang yang selalu struggle dengan masalah ni...",
            "💫 Cerita ni mesti ramai yang boleh relate...",
            "🌟 RAHSIA yang viral di TikTok!",
            "✨ Akhirnya... Penyelesaian yang korang tunggu dah sampai!"
        ]
        
        self.stories = [
            # Template 1: Personal Story
            "Korang tau tak?\n\n"
            "Dulu saya pun sama macam korang. Selalu struggle dengan {pain_point}. "
            "Sampai satu hari tu, saya jumpa {product_name}.\n\n"
            "Mula-mula memang ragu. Tapi lepas try sendiri... {usp}\n\n"
            "Yang best pasal {product_name}:\n"
            "✨ {benefit_1}\n"
            "✨ {benefit_2}\n"
            "✨ {benefit_3}\n\n"
            "Sekarang dah ramai yang dah buktikan sendiri. "
            "Testimoni masuk setiap hari! 😍\n\n"
            "Kalau korang nak transform macam customer-customer lain...",
            
            # Template 2: Customer Testimony
            "Semalam ada customer share pengalaman dia...\n\n"
            "\"Dulu memang tak percaya sangat. Tapi lepas cuba {product_name}, "
            "baru tau kenapa ramai cakap {usp}\"\n\n"
            "Apa yang buat {product_name} ni special:\n"
            "🌟 {benefit_1}\n"
            "🌟 {benefit_2}\n"
            "🌟 {benefit_3}\n\n"
            "Tapi tu lah... ramai yang tunggu sampai sold out baru nak beli. "
            "Lepas tu stress sebab kena waitlist pulak 🥺\n\n"
            "Untuk yang serious nak upgrade...",
            
            # Template 3: Problem-Solution
            "Korang pernah tak rasa macam ni?\n\n"
            "➡️ Dah try macam-macam tapi tak berkesan\n"
            "➡️ Dah habis duit tapi still sama je\n"
            "➡️ Nak sesuatu yang betul-betul berbaloi\n\n"
            "Good news! {product_name} dah sampai untuk selesaikan masalah tu.\n\n"
            "{usp}\n\n"
            "3 sebab kenapa {product_name} jadi pilihan ramai:\n"
            "💫 {benefit_1}\n"
            "💫 {benefit_2}\n"
            "💫 {benefit_3}\n\n"
            "Tapi ingat... stock limited je sebab permintaan tinggi!\n\n"
            "Untuk yang tak nak missed out...",
            
            # Template 4: Viral Story
            "RAHSIA yang ramai tak tau! 🤫\n\n"
            "Kenapa {product_name} jadi viral sampai trending?\n\n"
            "Sebab {usp}!\n\n"
            "Tapi bukan tu je... Customer suka sebab:\n"
            "⭐ {benefit_1}\n"
            "⭐ {benefit_2}\n"
            "⭐ {benefit_3}\n\n"
            "Yang best, sekarang ada PROMOSI TERHAD!\n"
            "Tapi kena cepat sebab ramai dah mula booking...\n\n"
            "Untuk yang serious nak grab...",
            
            # Template 5: Before-After Story
            "TRANSFORMASI yang tak masuk akal! 🎯\n\n"
            "BEFORE:\n"
            "❌ Struggle dengan {pain_point}\n"
            "❌ Dah cuba macam-macam product\n"
            "❌ Tak nampak hasil\n\n"
            "AFTER cuba {product_name}:\n"
            "✅ {benefit_1}\n"
            "✅ {benefit_2}\n"
            "✅ {benefit_3}\n\n"
            "Rahsia dia? {usp}\n\n"
            "Tapi kena cepat sebab stock terhad..."
        ]
        
        self.cta = [
            "📲 DM 'NAK INFO' sekarang! Nanti takde slot tau!\n\n"
            "🎁 FREE GIFT untuk 50 orang yang first je!",
            
            "💝 Whatsapp admin sekarang untuk dapat SPECIAL PRICE!\n\n"
            "🔥 Bonus eksklusif untuk yang grab hari ni!",
            
            "🌟 DM 'YES' untuk dapat full details + free gift!\n\n"
            "⚡ Tawaran terhad untuk yang pantas je!",
            
            "💫 PM 'DEAL' untuk dapat harga special + free shipping!\n\n"
            "🎯 Bonus rahsia untuk yang confirm hari ni!",
            
            "🎊 Comment 'MINE' untuk dapat FREE CONSULTATION!\n\n"
            "✨ Limited slot untuk 24 jam je!"
        ]

    def generate_ad_copies(self, product_name, usp, benefit_1, benefit_2, benefit_3, pain_points):
        variants = []
        template_names = [
            "💫 Personal Story Style",
            "👥 Customer Testimony Style",
            "❓ Problem-Solution Style",
            "🔥 Viral Story Style",
            "✨ Before-After Style"
        ]
        
        # Generate 5 different variants
        used_stories = list(enumerate(self.stories))
        for i in range(5):
            hook = random.choice(self.hooks)
            idx, story = used_stories.pop(random.randint(0, len(used_stories)-1))
            call_to_action = random.choice(self.cta)
            
            ad_copy = story.format(
                product_name=product_name,
                usp=usp,
                benefit_1=benefit_1,
                benefit_2=benefit_2,
                benefit_3=benefit_3,
                pain_point=random.choice(pain_points)
            )
            
            hashtags = "\n\n#PromosiTerhad #JanganTungguLagi #DealTerbaik #MurahMeriah #ReviewJujur"
            full_copy = f"{hook}\n\n{ad_copy}\n\n{call_to_action}{hashtags}"
            
            variants.append({
                'name': template_names[idx],
                'content': full_copy
            })
        
        return variants
