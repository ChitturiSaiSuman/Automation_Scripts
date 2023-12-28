from subprocess import run
from sys import argv
import os
from gtts import gTTS

def parse_arguments():
	query_keys = argv[1:]
	query_keys = [key.lower().strip() for key in query_keys]
	return query_keys

def pre_process():
	db = run(['find', '/home/suman/Music'], capture_output = True)
	db = db.stdout.decode()
	db = list(map(str, db.split('\n')))
	return db

def speak(text):
	obj = gTTS(text = text, lang = 'en', slow = False)
	obj.save("/home/suman/Jarvis/voice.mp3")
	os.system("mpg123 /home/suman/Jarvis/voice.mp3")
	os.system("rm /home/suman/Jarvis/voice.mp3")

def play_local(path):
	run(['vlc', os.path.realpath(path), '&'])

def play_youtube(query):
	run(['python3', '/home/suman/Automation_Scripts/music.py', query])

def search(keys, db):
	matched = []
	for path in db:
		count = 0
		for item in keys:
			if item in path.lower():
				count += 1
		matched.append([count, path])
	matched.sort(reverse = True)
	return matched


if __name__ == '__main__':
	query_keys = parse_arguments()
	db = pre_process()
	matched = search(query_keys, db)
	if matched[0][0] == 0:
		speak("Sorry, I couldn't find any song on your machine")
		speak("Playing " + ' '.join(query_keys) + " on youtube")
		play_youtube(' '.join(query_keys))
	elif '.ogg' in matched[0][1]:
		pass
	else:
		speak("Playing " + ' '.join(query_keys) + " on your local music")
		play_local(matched[0][1])
