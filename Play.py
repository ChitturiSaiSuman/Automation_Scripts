from subprocess import run
from sys import argv
import os
from gtts import gTTS

def parse_arguments():
	query_keys = argv[1:]
	query_keys = [key.lower().strip() for key in query_keys]
	return query_keys

def pre_process():
	database = run(['find', '/home/suman/Music'], capture_output = True)
	database = database.stdout.decode()
	database = list(map(str, database.split('\n')))
	return database

def speak(text):
	obj = gTTS(text = text, lang = 'en', slow = False)
	obj.save("/home/suman/Jarvis/voice.mp3")
	os.system("mpg321 /home/suman/Jarvis/voice.mp3")
	os.system("rm /home/suman/Jarvis/voice.mp3")

def play_local(path):
	run(['vlc', os.path.realpath(path)])

def play_youtube(query):
	run(['python3', '/home/suman/Automation_Scripts/music.py', query])

def search(keys, database):
	matched = []
	for path in database:
		count = 0
		for item in keys:
			if item in path.lower():
				count += 1
		matched.append([count, path])
	matched.sort(reverse = True)
	return matched


if __name__ == '__main__':
	query_keys = parse_arguments()
	database = pre_process()
	matched = search(query_keys, database)
	if matched[0][0] == 0:
		speak("Sorry, I couldn't find any song")
		speak("Playing " + ' '.join(query_keys) + " on youtube")
		play_youtube(' '.join(query_keys))
	else:
		speak("Playing " + ' '.join(query_keys) + " on your local music")
		play_local(matched[0][1])