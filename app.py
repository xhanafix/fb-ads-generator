from flask import Flask, render_template, request, jsonify
from src.fb_ad_copy_generator import FBAdCopyGenerator
import os

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
    # Get port from environment variable or default to 8080
    port = int(os.environ.get('PORT', 8080))
    # Run the app on 0.0.0.0 to make it accessible externally
    app.run(host='0.0.0.0', port=port) 
