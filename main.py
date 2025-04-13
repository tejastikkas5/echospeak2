from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    audio_file = None
    if request.method == 'POST':
        text = request.form['text']
        lang = request.form['language']
        filename = f"static/{uuid.uuid4()}.mp3"

        try:
            tts = gTTS(text=text, lang=lang, slow=False)
            tts.save(filename)
            audio_file = filename
        except Exception as e:
            return f"Error: {str(e)}"

    return render_template('index.html', audio_file=audio_file)

if __name__ == '__main__':
    app.run(debug=True)
