from gtts import gTTS
import os


def create_audio(text_file, output_file):
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    tts = gTTS(text=text, lang='en')

    tts.save(output_file)
    print(f"Audio save as {output_file}")


text_file = 'text.txt'
output_file = 'audio.mp3'

create_audio(text_file, output_file)
os.system(f'start {output_file}')
