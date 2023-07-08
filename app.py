from sklearn.linear_model import LogisticRegression
import sounddevice as sd
import vosk
import queue
import traceback
import words
from skills import *
from gtts import gTTS
import tempfile
import os
from sklearn.feature_extraction.text import CountVectorizer
import time
import subprocess
from playsound import playsound


q = queue.Queue()
model = vosk.Model('model_small')  # голосовую модель vosk нужно поместить в папку с файлами проекта

device = 0, 11  # <--- по умолчанию
# или -> sd.default.device = 1, 3, python -m sounddevice просмотр
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])  # получаем частоту микрофона

stop_listening = False


def callback(indata, frames, time, status):
    q.put(bytes(indata))


def recognize(data, vectorizer, clf):
    global stop_listening

    trg = words.TRIGGERS.intersection(data.split())
    if not trg:
        return

    data.replace(list(trg)[0], '')

    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    func_name = answer.split()[0]
    response = answer.replace(func_name, '')
    tts = gTTS(text=response, lang='ru')
    tts.save('output.mp3')
    playsound('output.mp3')
    time.sleep(0.1)  # Добавляем паузу в 0.1 секунды
    os.remove('output.mp3')  # Удаление файла

    if func_name in ["стоп", "стой", "остановись"]:
        stop_listening = True
    else:
        try:
            exec(func_name + '()')
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            traceback.print_exc()


def main():
    global stop_listening

    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set

    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16', channels=1,
                          callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            if stop_listening:
                break

            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)


if __name__ == '__main__':
    main()