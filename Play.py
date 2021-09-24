from subprocess import run
from sys import argv
import os

out = run(['find', '/home/suman/Music'], capture_output = True)
out = out.stdout.decode()
out = list(map(str, out.split('\n')))

song_keys = argv[1:]
paths = []
for item in out:
    if all([key.lower() in item.lower() for key in song_keys]):
        paths.append(item)

if paths == []:
	print("Song not found")
	exit(0)

for i in range(len(paths)):
	print(str(i + 1) + "). " + paths[i])

index = int(input("Enter index: "))

print(os.path.realpath(paths[index - 1]))

run(['vlc', os.path.realpath(paths[index - 1])])
