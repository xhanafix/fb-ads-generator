from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_aida_copy(produk, kelebihan, target_market, call_to_action):
    template = [
        f"🔥 PERHATIAN {target_market}!\n\n{kelebihan}\n\nJangan tunggu lagi! {call_to_action}",
        
        f"📢 TAWARAN HEBAT untuk {target_market}!\n\n{produk} yang akan mengubah hidup anda.\n\n"
        f"✨ {kelebihan}\n\n{call_to_action}",
        
        f"⚡️ PENGUMUMAN PENTING!\n\nUntuk {target_market} yang mencari {produk}...\n\n"
        f"Kami ada penyelesaiannya!\n\n{kelebihan}\n\n{call_to_action}"
    ]
    return random.choice(template)

def generate_pas_copy(produk, masalah, kelebihan, call_to_action):
    template = [
        f"Penat {masalah}?\n\nJangan risau, anda tidak keseorangan.\n\n"
        f"Dengan {produk}, {kelebihan}\n\n{call_to_action}",
        
        f"🤔 Masih {masalah}?\n\nSudah cuba macam-macam tapi tak berkesan?\n\n"
        f"✅ {produk} adalah penyelesaian untuk anda!\n\n{kelebihan}\n\n{call_to_action}",
        
        f"😫 {masalah} buat anda stress?\n\nJangan biarkan masalah ini berterusan.\n\n"
        f"👉 {produk} boleh bantu anda. {kelebihan}\n\n{call_to_action}"
    ]
    return random.choice(template)

def generate_fab_copy(produk, features, advantages, benefits, call_to_action):
    template = [
        f"🌟 PRODUK TERHANGAT: {produk}\n\n✨ {features}\n\n💪 {advantages}\n\n"
        f"🎯 {benefits}\n\n{call_to_action}",
        
        f"🔥 TAWARAN ISTIMEWA!\n\n{produk} hadir dengan:\n✅ {features}\n\n"
        f"Kenapa pilih kami?\n👉 {advantages}\n\n{benefits}\n\n{call_to_action}",
        
        f"⭐️ PROMOSI TERHAD!\n\n{produk}\n\nCiri-ciri hebat:\n✅ {features}\n\n"
        f"Kelebihan:\n💫 {advantages}\n\n{benefits}\n\n{call_to_action}"
    ]
    return random.choice(template)

def generate_4u_copy(produk, kelebihan, target_market, masalah, benefits, call_to_action):
    # Formula 4U: Useful, Urgent, Unique, Ultra-specific
    template = [
        f"💥 TAWARAN EKSKLUSIF UNTUK {target_market} SAHAJA!\n\n"
        f"Anda {masalah}? Inilah penyelesaian yang anda cari selama ini!\n\n"
        f"🎯 {produk} adalah satu-satunya produk yang:\n"
        f"✅ {kelebihan}\n"
        f"✅ Terbukti berkesan untuk {target_market}\n"
        f"✅ {benefits}\n\n"
        f"⚡️ TAWARAN TERHAD:\n"
        f"- Bonus eksklusif bernilai RM XXX\n"
        f"- Jaminan wang dikembalikan 30 hari\n"
        f"- Sesi konsultasi 1-1 percuma\n\n"
        f"🔥 {call_to_action}\n"
        f"⏰ Tawaran tamat: HARI INI SAHAJA!",

        f"📢 PERHATIAN {target_market}!\n\n"
        f"Adakah anda:\n"
        f"❌ {masalah}\n"
        f"❌ Sudah cuba pelbagai cara tapi gagal?\n"
        f"❌ Tertekan dengan masalah ini?\n\n"
        f"✨ BERITA BAIK! {produk} hadir dengan:\n"
        f"✅ {kelebihan}\n"
        f"✅ {benefits}\n\n"
        f"🎁 BONUS ISTIMEWA:\n"
        f"🎯 3 Bonus Eksklusif\n"
        f"🎯 Panduan Lengkap\n"
        f"🎯 Sokongan 24/7\n\n"
        f"⚡️ {call_to_action}"
    ]
    return random.choice(template)

def generate_pastor_copy(produk, masalah, kelebihan, target_market, benefits, call_to_action):
    # Formula PASTOR: Problem, Amplify, Story, Testimony, Offer, Response
    template = [
        f"😫 {masalah}?\n\n"
        f"Saya faham perasaan anda. Dulu saya juga menghadapi masalah yang sama...\n\n"
        f"Sehinggalah saya menemui rahsia ini:\n"
        f"👉 {kelebihan}\n\n"
        f"Ramai pelanggan kami telah berjaya:\n"
        f"✨ Sarah dari KL: 'Dalam masa 30 hari, saya telah {...}'\n"
        f"✨ Ahmad dari JB: 'Tak sangka boleh {...}'\n\n"
        f"���� TAWARAN EKSKLUSIF:\n"
        f"{produk} + Bonus Bernilai RM XXXX\n\n"
        f"Anda akan dapat:\n"
        f"✅ {benefits}\n"
        f"✅ Sokongan komuniti eksklusif\n"
        f"✅ Jaminan kepuasan 100%\n\n"
        f"🔥 {call_to_action}",

        f"KISAH BENAR {target_market}...\n\n"
        f"'Dulu saya {masalah}. Setiap hari rasa tertekan dan tidak tahu nak buat apa...'\n\n"
        f"Tapi semuanya berubah apabila saya temui {produk}!\n\n"
        f"Mengapa {produk} berbeza?\n"
        f"💫 {kelebihan}\n"
        f"💫 {benefits}\n\n"
        f"Dan anda tidak perlu percaya kata-kata saya...\n"
        f"Dengar testimoni pelanggan kami:\n\n"
        f"'Hasil meningkat 300% dalam 2 bulan!' - Lisa T.\n"
        f"'Terbaik! Tak rugi langsung!' - Azman K.\n\n"
        f"🎁 TAWARAN TERHAD:\n"
        f"👉 {call_to_action}"
    ]
    return random.choice(template)

def generate_quest_copy(produk, masalah, kelebihan, target_market, benefits, features, call_to_action):
    # Formula QUEST: Qualify, Understand, Educate, Stimulate, Transition
    template = [
        f"🎯 UNTUK {target_market} YANG SERIUS MAHU BERJAYA\n\n"
        f"Jika anda {masalah}, anda perlu tahu ini...\n\n"
        f"Rahsia yang ramai tidak tahu:\n"
        f"🔍 90% {target_market} gagal kerana tidak tahu teknik yang betul\n"
        f"🔍 Hanya 10% yang berjaya menggunakan kaedah yang akan saya kongsi\n\n"
        f"Dalam {produk}, anda akan belajar:\n"
        f"📚 {features}\n"
        f"📚 {kelebihan}\n"
        f"📚 {benefits}\n\n"
        f"BONUS PEMBELAJARAN:\n"
        f"🎁 Template eksklusif\n"
        f"🎁 Kajian kes sebenar\n"
        f"🎁 Sesi group coaching\n\n"
        f"Bayangkan dalam 30 hari dari sekarang:\n"
        f"✨ Anda sudah menguasai semua teknik\n"
        f"✨ Hasil semakin meningkat\n"
        f"✨ Masalah anda selesai\n\n"
        f"⚡️ {call_to_action}",

        f"PELUANG EKSKLUSIF UNTUK {target_market}!\n\n"
        f"Tahukah anda mengapa {masalah}?\n\n"
        f"Mari saya kongsi 3 fakta penting:\n"
        f"1️⃣ 80% {target_market} melakukan kesilapan ini\n"
        f"2️⃣ Tanpa panduan yang betul, anda akan terus struggle\n"
        f"3️⃣ Ada cara yang lebih mudah!\n\n"
        f"{produk} akan mengajar anda:\n"
        f"🎯 {features}\n"
        f"🎯 {kelebihan}\n"
        f"🎯 {benefits}\n\n"
        f"BONUS ISTIMEWA:\n"
        f"💎 Akses seumur hidup\n"
        f"💎 Updates percuma\n"
        f"💎 Komuniti eksklusif\n\n"
        f"🔥 {call_to_action}"
    ]
    return random.choice(template)

@app.route('/', methods=['GET', 'POST'])
def home():
    generated_ads = []
    if request.method == 'POST':
        produk = request.form.get('produk')
        target_market = request.form.get('target_market')
        masalah = request.form.get('masalah')
        kelebihan = request.form.get('kelebihan')
        features = request.form.get('features')
        advantages = request.form.get('advantages')
        benefits = request.form.get('benefits')
        call_to_action = request.form.get('call_to_action')

        if produk and target_market and masalah and kelebihan:
            for i in range(10):
                formula = random.choice(['AIDA', 'PAS', 'FAB', '4U', 'PASTOR', 'QUEST'])
                if formula == 'AIDA':
                    copy = generate_aida_copy(produk, kelebihan, target_market, call_to_action)
                elif formula == 'PAS':
                    copy = generate_pas_copy(produk, masalah, kelebihan, call_to_action)
                elif formula == 'FAB':
                    copy = generate_fab_copy(produk, features, advantages, benefits, call_to_action)
                elif formula == '4U':
                    copy = generate_4u_copy(produk, kelebihan, target_market, masalah, benefits, call_to_action)
                elif formula == 'PASTOR':
                    copy = generate_pastor_copy(produk, masalah, kelebihan, target_market, benefits, call_to_action)
                else:
                    copy = generate_quest_copy(produk, masalah, kelebihan, target_market, benefits, features, call_to_action)
                generated_ads.append({'formula': formula, 'copy': copy})

    return render_template('index.html', generated_ads=generated_ads)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
