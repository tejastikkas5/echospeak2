from flask import Flask, render_template, request, send_file
from gtts import gTTS
import tempfile
import uuid
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    audio_file = None
    if request.method == 'POST':
        text = request.form['text']
        lang = request.form['language']

        try:
            temp_dir = tempfile.gettempdir()
            filename = os.path.join(temp_dir, f"{uuid.uuid4()}.mp3")

            tts = gTTS(text=text, lang=lang, slow=False)
            tts.save(filename)

            audio_file = f"/audio/{os.path.basename(filename)}"  # custom route
        except Exception as e:
            return f"Error: {str(e)}"

    return render_template('index.html', audio_file=audio_file)

@app.route('/audio/<filename>')
def get_audio(filename):
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, filename)
    return send_file(file_path, mimetype='audio/mp3')

if __name__ == '__main__':
    app.run(debug=True)
