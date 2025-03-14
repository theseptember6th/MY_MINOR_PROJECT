# app.py
from flask import Flask, render_template, request, send_file
import os
from werkzeug.utils import secure_filename
from main1 import process_video

app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'wmv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Create necessary directories
for folder in [UPLOAD_FOLDER, OUTPUT_FOLDER]:
    os.makedirs(folder, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return 'No video file uploaded', 400
    
    file = request.files['video']
    if file.filename == '':
        return 'No selected file', 400
    
    if file and allowed_file(file.filename):
        try:
            # Secure the filename and save the uploaded file
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(input_path)
            
            # Process the video
            output_filename = f'processed_{filename}'
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
            
            # Process the video
            process_video(input_path, output_path)
            
            return {'filename': output_filename}
            
        except Exception as e:
            return f'Error processing video: {str(e)}', 500
    
    return 'Invalid file type', 400

@app.route('/download/<filename>')
def download_video(filename):
    return send_file(
        os.path.join(app.config['OUTPUT_FOLDER'], filename),
        as_attachment=True,
        download_name=filename
    )

if __name__ == '__main__':
    app.run(debug=True)