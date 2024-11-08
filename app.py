from flask import Flask, render_template, request, jsonify
from src.fb_ad_copy_generator import FBAdCopyGenerator
import os

app = Flask(__name__)
generator = FBAdCopyGenerator()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form
        variants = generator.generate_ad_copies(
            data['product_name'],
            data['usp'],
            data['benefit1'],
            data['benefit2'],
            data['benefit3'],
            [  # Send array of pain points
                data['pain_point1'],
                data['pain_point2'],
                data['pain_point3']
            ]
        )
        return render_template('index.html', variants=variants)
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
