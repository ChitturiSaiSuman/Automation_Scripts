#!/usr/bin/env python3
import os
import shutil
import datetime

now = datetime.datetime.now()
now = str(now.strftime("%Y-%m-%d %H:%M:%S"))
header = "Author: Chitturi Sai Suman\n"
header += "Partner: Github Copilot\n"
header += "Created: " + now + "\n"

source = "/home/suman/Desktop/Templates/"
files = os.listdir(source)
path = input("Enter Path: ")
contest_name = input("Contest Name: ")
header += "Contest: " + contest_name + "\n"

try:
    os.makedirs(path)
    print("Environment Initialised with Directories")
except:
    print("Environment Already Exists!")

shutil.copy(source + "Default.cpp", path + "/Default.cpp")
shutil.copy(source + "Extended.cpp", path + "/Extended.cpp")

n = int(input("Enter Number of Challenges: "))

cpp_source = ""

with open(source + "Default.cpp", "r") as file:
    cpp_source += file.read()
    cpp_source = "/*\n" + header + "*/\n" + cpp_source

for count in range(1, n+1):
    with open(path + "/p" + str(count) + ".cpp", "w") as file:
        file.write(cpp_source)

local = ["STDIN", "STDOUT", "STDEXPOUT", "STDERR", "Generator.cpp", "Test.cpp"]

for file in local:
    shutil.copy(source + file, path + "/" + file)

print("Opening {} in VS Code".format(path))
os.system("code " + path)
print("Done")