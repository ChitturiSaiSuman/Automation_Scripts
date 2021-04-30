import os
# Python program to locate files in Local Machine
vlc_files = [".flac",".mp3",".wav",".mp4"]
text_files = [".txt",".py",".c",".cpp",".java",".html",".css",".js"]
os.chdir("/home/suman/")
dir_path = os.path.dirname(os.path.realpath("."))
keys = list(map(str,input("Enter space separated keys: ").split()))
results = []
for root,dirs,files in os.walk(dir_path):
    for file in files:
        if all([item.lower() in str(file).lower() for item in keys]):
            temp = (root+'/'+str(file))
            results.append(os.path.realpath(temp))
for i in range(len(results)):
    print(i+1,results[i])
if len(results)>1:
    index = int(input("Enter Index: "))
else:
    index = 1
file = '"'+results[index-1]+'"'
if any([i in file for i in vlc_files]):
    os.system("vlc "+file)
elif any([i in file for i in text_files]):
    os.system("gedit "+file)
else:
    command = input("Enter Commnand: ")
    os.system(command+" "+file)
