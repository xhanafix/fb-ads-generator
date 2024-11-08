from flask import Flask, render_template, request, jsonify
from src.fb_ad_copy_generator import FBAdCopyGenerator

app = Flask(__name__)
generator = FBAdCopyGenerator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    variants = generator.generate_ad_copies(
        data['product_name'],
        data['usp'],
        data['benefit1'],
        data['benefit2'],
        data['benefit3']
    )
    return jsonify(variants)

if __name__ == '__main__':
    app.run(debug=True) 
