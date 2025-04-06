from flask import Flask, render_template, request, send_file
from PIL import Image
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    image = request.files['image']
    target_format = request.form['format'].lower()

    filename = str(uuid.uuid4()) + '.' + target_format
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    img = Image.open(image)

    if target_format in ['jpg', 'jpeg']:
        img = img.convert('RGB')  # Remove alpha channel for JPEG

    img.save(filepath, target_format.upper())

    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
