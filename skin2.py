import tkinter as tk
import subprocess
import winsound
import openai
from gtts import gTTS
def start_assistant():
    # Укажите полный путь к файлу app.py
    app_file_path = 'C:/Users/Никитик/PycharmProjects/lastassistent2/app.py'
    subprocess.Popen(['python', app_file_path])
    play_sound("sound.wav")  # Воспроизведение звука

def play_sound(file_path):
    winsound.PlaySound(file_path, winsound.SND_FILENAME)

# Создание графического интерфейса
window = tk.Tk()
window.title("Voice Assistant")
window.geometry("300x200")

# Фон
background_image = tk.PhotoImage(file="background_image.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Кнопка для запуска ассистента
button = tk.Button(window, text="Запустить ассистента", command=start_assistant)
button.pack(pady=50)

# Запуск основного цикла приложения
window.mainloop()