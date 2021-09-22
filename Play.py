from subprocess import run
from sys import argv
import os

out = run(['find', '/home/suman/Music'], capture_output = True)
out = out.stdout.decode()
out = list(map(str, out.split('\n')))

song_keys = argv[1:]
path = ""
for item in out:
    if all([key.lower() in item.lower() for key in song_keys]):
        path = item
        break

print(os.path.realpath(path))

run(['cvlc', os.path.realpath(path)])
