from flask import Flask, render_template, request, jsonify
from src.fb_ad_copy_generator import FacebookAdGenerator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    business_name = request.form.get('business_name', 'MEJA PORTABLE MY')
    whatsapp_link = request.form.get('whatsapp_link', 'https://wasap.my/+60123456789')
    generator = FacebookAdGenerator()
    ad_copy = generator.generate_ad_copy(business_name, whatsapp_link)
    return jsonify({'ad_copy': ad_copy})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
