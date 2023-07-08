# -*- coding: utf-8 -*-
import sys
import subprocess
import voice
import json
import datetime
import webbrowser
import os
import ctypes
import wikipediaapi
import textwrap
import locale
import psutil
import openai
import pyscreenshot
import pygame
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play


try:
    import requests  # pip install requests
except:
    pass

#===================================================================================================================
#Запуск игр и приложений
#===================================================================================================================

def ragemp():
    program_path = 'N:/RAGEMP/GTA5.exe'
    subprocess.call(program_path)

def open_yandex_browser():
    browser_path = r'C:/Users/Никитик/AppData/Local/Yandex/YandexBrowser/Application/browser.exe'
    subprocess.Popen(['start', browser_path], shell=True)

def Discord():
    subprocess.Popen(['start', 'C:/Users/Никитик/AppData/Local/Discord/app-1.0.9013/Discord.exe'], shell=True)

def Discordclose():
    for proc in psutil.process_iter():
        if proc.name() == "Discord.exe":
            proc.kill()

def open_sound_settings_windows():
    subprocess.Popen('mmsys.cpl', shell=True)

def minimize_windows_windows():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

def wake_up_computer():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def PyCharm():
    subprocess.Popen('C:/Program Files/JetBrains/PyCharm Community Edition 2023.1/bin/pycharm64.exe').detach()

def PyCharmclose():
    os.system("taskkill /F /IM pycharm64.exe")

def panely_ypravleniy():
    subprocess.call("control panel", shell=True)

def dispetcher_zadach():
    subprocess.Popen(['taskmgr'], shell=True)

def parametry_ekrana():
    subprocess.call("control desk.cpl", shell=True)

#===================================================================================================================
#Стим игры
#===================================================================================================================

def steam_wallpaper64():
    steam_path = r"N:/Program Files/steam/steam.exe"
    game_id = "431960"
    command = f'"{steam_path}" -applaunch {game_id}'
    subprocess.Popen(command, shell=True)


#===================================================================================================================
#Скриншот
#===================================================================================================================

def screenshot_desktop():
    image = pyscreenshot.grab()
    image.show()
    image.save("GeeksforGeeks.png")

#===================================================================================================================
#Открытие сайтов
#===================================================================================================================

def open_website():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите название сайта:")
        audio = recognizer.listen(source)

    try:
        website_name = recognizer.recognize_google(audio, language="ru-RU")
        print("Название сайта:", website_name)

        # Словарь для соответствия ключевых слов сайтам
        websites = {
            "яндекс": "https://www.yandex.ru",
            "youtube": "https://www.youtube.com/",
            "вк": "https://vk.com/feed",
            "telegram": "https://web.telegram.org/a/",
            "кинопоиск": "https://www.kinopoisk.ru/lists/movies/?b=films&utm_referrer=yandex.ru",
            "ВКонтакте": "https://vk.com/feed"
            # Добавьте другие сайты и ключевые слова по своему усмотрению
        }

        # Поиск URL-адреса сайта по ключевому слову
        website_url = websites.get(website_name.lower())

        if website_url:
            webbrowser.open(website_url)
            print("Сайт открыт:", website_url)
        else:
            print("Сайт не найден.")

    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as e:
        print("Ошибка сервиса распознавания речи: {0}".format(e))

#===================================================================================================================
#Поиск в википедии
#===================================================================================================================

def wikipedia_search():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите запрос для поиска в Википедии:")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio, language="ru-RU")
        print("Запрос для поиска:", query)

        search_query = query.lower().strip()
        if search_query.startswith("что такое"):
            search_query = search_query.replace("что такое", "").strip()

        wiki_wiki = wikipediaapi.Wikipedia('ru')
        page = wiki_wiki.page(search_query)

        if page.exists():
            summary = page.summary
            print("Результаты поиска в Википедии:")
            print(summary)
            summary = ' '.join(summary.split()[:120])  # Ограничение на 220 слов
        else:
            print("Ничего не найдено в Википедии по данному запросу.")
            return

    except sr.UnknownValueError:
        print("Не удалось распознать речь")
        return
    except sr.RequestError as e:
        print("Ошибка сервиса распознавания речи: {0}".format(e))
        return
    except wikipediaapi.exceptions.WikipediaException as e:
        print("Ошибка при обращении к Википедии: {0}".format(e))
        return

    engine = pyttsx3.init()
    engine.setProperty('rate', 220)
    wrapped_summary = '\n'.join(textwrap.wrap(summary, width=70))  # Разбиваем текст на строки по 70 символов
    engine.say(wrapped_summary)
    engine.runAndWait()



#===================================================================================================================
#Режим сна
#===================================================================================================================

# def sleep_computer():
#     ctypes.windll.powrprof.SetSuspendState(0, 1, 0)

#===================================================================================================================
#Отключение бота
#===================================================================================================================
def offBot():
    '''Отключает бота'''
    sys.exit()

#===================================================================================================================
#Функция заглушка при простом диалоге с ботом
#===================================================================================================================
def passive():
    pass
#===================================================================================================================
#Погода и время
#===================================================================================================================
def get_weather():
    API_KEY = "8858413d3193ff97d3e7f2878c6cdb8e"

    city = 'Москва'  # Жестко закодированный город Москва
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = json.loads(response.text)

    weather_description = data["weather"][0]["description"]
    temperature_kelvin = data["main"]["temp"]
    temperature_celsius = temperature_kelvin - 273.15  # Преобразование из Кельвинов в Цельсии
    humidity = data["main"]["humidity"]

    weather_conditions = {
        "clear sky": "ясное небо",
        "few clouds": "малооблачно",
        "scattered clouds": "рассеянные облака",
        "broken clouds": "облачно с прояснениями",
        "overcast clouds": "пасмурно",
        "shower rain": "кратковременный дождь",
        "rain": "дождь",
        "thunderstorm": "гроза",
        "snow": "снег",
        "mist": "туман"
    }
    if weather_description in weather_conditions:
        weather_description_ru = weather_conditions[weather_description]
    else:
        weather_description_ru = weather_description


    voice.speaker(f"Погода в городе {city}:")
    voice.speaker(f"Описание: {weather_description_ru}")
    voice.speaker(f"Температура: {temperature_celsius:.2f}°C")
    voice.speaker(f"Влажность: {humidity}%")


def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    voice.speaker(f"Текущее время: {current_time}")
#===================================================================================================================
#Браузер
#===================================================================================================================
def Ybrauser():
    browser_path = r'C:/Users/Никитик/AppData/Local/Yandex/YandexBrowser/Application/browser.exe'
    subprocess.Popen([browser_path]).detach()

def Ybrauserclose():
    os.system("taskkill /im browser.exe /f")

#===================================================================================================================
#Дата Время День Год И Праздники
#===================================================================================================================

def denu_nedeli():
    # Получаем текущий день недели
    locale.setlocale(locale.LC_TIME, 'ru_RU')
    current_date = datetime.date.today()
    day_of_week = current_date.strftime("%A")
    voice.speaker(day_of_week)

def tekushiy_mesuiac():
    # Получаем текущий месяц
    locale.setlocale(locale.LC_TIME, 'ru_RU')
    current_date = datetime.date.today()
    month = current_date.strftime("%B")
    voice.speaker(month)

def tekushiy_god():
    # Получаем текущий год
    locale.setlocale(locale.LC_TIME, 'ru_RU')
    current_date = datetime.date.today()
    year = current_date.strftime("%Y")
    voice.speaker(year)

#===================================================================================================================
#ChatGPT
#===================================================================================================================

import speech_recognition as sr
import pyttsx3
import openai

def activate_chatgpt():
    # Инициализация распознавания речи и синтеза речи
    recognizer = sr.Recognizer()
    synthesizer = pyttsx3.init()

    # Установка голоса для синтеза речи
    voices = synthesizer.getProperty('voices')
    synthesizer.setProperty('voice', voices[0].id)  # Выберите индекс нужного голоса

    # Инициализация OpenAI API
    openai.api_key = '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'

    # Приветствие
    synthesizer.say('Привет, чем я могу помочь?')
    synthesizer.runAndWait()

    while True:
        try:
            # Слушаем команду пользователя
            with sr.Microphone() as source:
                print("Слушаю...")
                audio = recognizer.listen(source)

            # Распознавание речи
            command = recognizer.recognize_google(audio, language='ru-RU')
            print("Вы сказали:", command)

            # Проверка на команду завершения диалога
            if command.lower() == 'пока':
                break

            # Обрабатываем команду
            # Отправляем команду в OpenAI API для получения ответа
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=command,
                max_tokens=500
            )

            # Получаем ответ от OpenAI API
            reply = response.choices[0].text.strip()

            # Произносим ответ
            synthesizer.say(reply)
            synthesizer.runAndWait()

            # Выводим ответ также в консоль
            print(reply)

        except sr.UnknownValueError:
            print("Не удалось распознать речь")
        except sr.RequestError as e:
            print("Ошибка сервиса распознавания речи: {0}".format(e))
        except Exception as e:
            print("Ошибка OpenAI API: {0}".format(e))
        except KeyboardInterrupt:
            break

    # Прощание
    synthesizer.say('До свидания!')
    synthesizer.runAndWait()

#===================================================================================================================
#Рандомные треки
#===================================================================================================================


def play_music_from_folder():
    # Установка пути к папке с музыкой
    music_folder = "N:/music_for_python/random_treack"

    # Инициализация Pygame
    pygame.init()

    # Создание списка для хранения песен
    playlist = []

    # Заполнение списка песнями из папки
    for file in os.listdir(music_folder):
        if file.endswith(".mp3"):
            playlist.append(os.path.join(music_folder, file))

    # Воспроизведение музыки
    pygame.mixer.init()
    pygame.mixer.music.load(playlist[0])  # Загрузка первой песни из плейлиста
    pygame.mixer.music.play()

    # Функция для распознавания голосовых команд
    def recognize_speech():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            command = r.recognize_google(audio, language="ru-RU").lower()
            return command
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print("Ошибка при обращении к сервису распознавания речи: {0}".format(e))
            return ""

    # Начальная громкость
    volume = 0.05  # 5 процентов

    # Установка начальной громкости
    pygame.mixer.music.set_volume(volume)

    # Список чисел, записанных словами
    number_words = {
        "один": 1,
        "два": 2,
        "три": 3,
        "четыре": 4,
        "пять": 5,
        "шесть": 6,
        "семь": 7,
        "восемь": 8,
        "девять": 9,
        "десять": 10
    }

    # Основной цикл программы
    while True:
        command = recognize_speech()

        # Обработка команды
        if "громкость" in command:
            words = command.split()
            for i, word in enumerate(words):
                if word.isdigit() and i > 0:
                    value = int(word)
                    if value >= 0 and value <= 100:
                        volume = value / 100
                        print("Громкость:", value, "%")
                        pygame.mixer.music.set_volume(volume)
                    else:
                        print("Значение громкости должно быть в диапазоне от 0 до 100.")
                    break
                elif word in number_words:
                    value = number_words[word]
                    if value >= 0 and value <= 100:
                        volume = value / 100
                        print("Громкость:", value, "%")
                        pygame.mixer.music.set_volume(volume)
                    else:
                        print("Значение громкости должно быть в диапазоне от 0 до 100.")
                    break
        elif command == "стоп":
            pygame.mixer.music.stop()
            break

        # Обработка окончания песни
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                # Получение индекса текущей песни
                current_index = playlist.index(pygame.mixer.music.get_music())
                # Переключение на следующую песню
                next_index = (current_index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[next_index])
                pygame.mixer.music.play()

    # Очистка ресурсов Pygame
    pygame.quit()


#===================================================================================================================
#QueenAlbom
#===================================================================================================================

def QueenAlbom():
    # Установка пути к папке с музыкой
    music_folder = "N:/music_for_python/Queen"

    # Инициализация Pygame
    pygame.init()

    # Создание списка для хранения песен
    playlist = []

    # Заполнение списка песнями из папки
    for file in os.listdir(music_folder):
        if file.endswith(".mp3"):
            playlist.append(os.path.join(music_folder, file))

    # Воспроизведение музыки
    pygame.mixer.init()
    pygame.mixer.music.load(playlist[0])  # Загрузка первой песни из плейлиста
    pygame.mixer.music.play()

    # Функция для распознавания голосовых команд
    def recognize_speech():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            command = r.recognize_google(audio, language="ru-RU").lower()
            return command
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print("Ошибка при обращении к сервису распознавания речи: {0}".format(e))
            return ""

    # Начальная громкость
    volume = 0.05  # 5 процентов

    # Установка начальной громкости
    pygame.mixer.music.set_volume(volume)

    # Список чисел, записанных словами
    number_words = {
        "один": 1,
        "два": 2,
        "три": 3,
        "четыре": 4,
        "пять": 5,
        "шесть": 6,
        "семь": 7,
        "восемь": 8,
        "девять": 9,
        "десять": 10
    }

    # Основной цикл программы
    while True:
        command = recognize_speech()

        # Обработка команды
        if "громкость" in command:
            words = command.split()
            for i, word in enumerate(words):
                if word.isdigit() and i > 0:
                    value = int(word)
                    if value >= 0 and value <= 100:
                        volume = value / 100
                        print("Громкость:", value, "%")
                        pygame.mixer.music.set_volume(volume)
                    else:
                        print("Значение громкости должно быть в диапазоне от 0 до 100.")
                    break
                elif word in number_words:
                    value = number_words[word]
                    if value >= 0 and value <= 100:
                        volume = value / 100
                        print("Громкость:", value, "%")
                        pygame.mixer.music.set_volume(volume)
                    else:
                        print("Значение громкости должно быть в диапазоне от 0 до 100.")
                    break
        elif command == "стоп":
            pygame.mixer.music.stop()
            break

        # Обработка окончания песни
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                # Получение индекса текущей песни
                current_index = playlist.index(pygame.mixer.music.get_music())
                # Переключение на следующую песню
                next_index = (current_index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[next_index])
                pygame.mixer.music.play()

    # Очистка ресурсов Pygame
    pygame.quit()

#===================================================================================================================
#QueenAlbom
#===================================================================================================================