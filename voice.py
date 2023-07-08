import pyttsx3		#pip install pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 210)				#скорость речи


def speaker(text):
	'''Озвучка текста'''
	engine.say(text)
	engine.runAndWait()

