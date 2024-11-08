from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_random_benefits():
    benefits = [
        "kualiti terbaik dalam pasaran",
        "harga yang berpatutan",
        "perkhidmatan pelanggan 24/7",
        "jaminan kepuasan 100%",
        "penghantaran percuma",
        "tawaran terhad masa",
        "diskaun istimewa",
        "bonus eksklusif",
        "hasil yang terbukti",
        "pengalaman lebih 10 tahun"
    ]
    return random.sample(benefits, 3)

def generate_random_target():
    targets = [
        "anda yang mahukan yang terbaik",
        "mereka yang menghargai kualiti",
        "pelanggan yang bijak",
        "anda yang ingin berjimat",
        "sesiapa yang mencari penyelesaian terbaik",
        "anda yang mementingkan kualiti"
    ]
    return random.choice(targets)

def generate_ad_copy(produk):
    benefits = generate_random_benefits()
    target = generate_random_target()
    
    templates = [
        f"🔥 TAWARAN HEBAT!\n\n"
        f"Memperkenalkan {produk}!\n\n"
        f"✨ Kenapa pilih kami?\n"
        f"✅ {benefits[0]}\n"
        f"✅ {benefits[1]}\n"
        f"✅ {benefits[2]}\n\n"
        f"Untuk {target}!\n\n"
        f"📞 Hubungi kami sekarang!\n"
        f"⚡️ Tawaran terhad masa sahaja!",

        f"⭐️ PROMOSI TERHAD!\n\n"
        f"{produk} - Pilihan Terbaik Anda\n\n"
        f"Kami menawarkan:\n"
        f"👉 {benefits[0]}\n"
        f"👉 {benefits[1]}\n"
        f"👉 {benefits[2]}\n\n"
        f"Khas untuk {target}!\n\n"
        f"🎯 Dapatkan sekarang!\n"
        f"📱 PM untuk maklumat lanjut",

        f"💥 JANGAN LEPASKAN PELUANG INI!\n\n"
        f"Dapatkan {produk} sekarang dengan:\n\n"
        f"🌟 {benefits[0]}\n"
        f"🌟 {benefits[1]}\n"
        f"🌟 {benefits[2]}\n\n"
        f"Sesuai untuk {target}\n\n"
        f"⏰ Tawaran terhad!\n"
        f"💬 DM untuk tempah sekarang!"
    ]
    
    return random.choice(templates)

@app.route('/', methods=['GET', 'POST'])
def home():
    generated_ads = []
    if request.method == 'POST':
        produk = request.form.get('produk')
        if produk:
            for i in range(10):
                ad_text = generate_ad_copy(produk)
                generated_ads.append({'formula': f'Iklan {i+1}', 'copy': ad_text})

    return render_template('index.html', generated_ads=generated_ads)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 
