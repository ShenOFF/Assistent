import tkinter as tk
import subprocess
import winsound
import pywinauto


def start_assistant():
    app_file_path = 'C:/Users/Никитик/PycharmProjects/lastassistent2/app.py'
    subprocess.Popen(['pythonw', app_file_path])  # Используйте 'pythonw' вместо 'python' для запуска без окна командной строки
    play_sound("sound.wav")  # Воспроизведение звука
    hide_console_window()


def play_sound(file_path):
    winsound.PlaySound(file_path, winsound.SND_FILENAME)


def hide_console_window():
    app = pywinauto.Application().connect(title='app.py')
    console_window = app.window()
    console_window.minimize()  # Сворачиваем окно командной строки


window = tk.Tk()
window.title("Voice Assistant")
window.geometry("300x200")

background_image = tk.PhotoImage(file="background_image.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

button = tk.Button(window, text="Запустить ассистента", command=start_assistant)
button.pack(pady=50)

window.mainloop()
