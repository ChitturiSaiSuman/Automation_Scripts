#!/usr/bin/env python3
import os
import shutil
import datetime

now = datetime.datetime.now()
now = str(now.strftime("%Y-%m-%d %H:%M:%S"))
header = "Author: Chitturi Sai Suman\n"
header += "Created: " + now + "\n"

source = "/home/suman/Desktop/Templates/"
files = os.listdir(source)
path = input("Enter Path: ")
contest_name = input("Contest Name: ")
header += "Contest: " + contest_name + "\n"
only_cpp = input("Only C Plus Plus? (Y/N): ") in "YESyes"

try:
    os.makedirs(path)
    print("Environment Initialised with Directories")
except:
    print("Environment Already Exists!")

choice = input("Load Defaults?(Y/N): ")

if choice in "YESYesyes":
    # Copy files for Global benefit

    if not only_cpp:
        shutil.copy(source + "Default.c", path + "/Default.c")
        shutil.copy(source + "Default.cpp", path + "/Default.cpp")
        shutil.copy(source + "Main.java", path + "/Main.java")
        shutil.copy(source + "Default.py", path + "/Default.py")

        shutil.copy(source + "Extended.c", path + "/Extended.c")
        shutil.copy(source + "Extended.cpp", path + "/Extended.cpp")
        shutil.copy(source + "Extended.java", path + "/Extended.java")
        shutil.copy(source + "Extended.py", path + "/Extended.py")

    else:
        shutil.copy(source + "Default.cpp", path + "/Default.cpp")
        shutil.copy(source + "Extended.cpp", path + "/Extended.cpp")

    # Copy files for Individual benefit
    n = int(input("Enter Number of Challenges: "))

    c_source = ""
    py_source = ""
    java_source = ""
    cpp_source = ""

    with open(source + "Default.c", "r") as file:
        c_source += file.read()
        c_source = "/*\n" + header + "*/\n" + c_source

    with open(source + "Default.cpp", "r") as file:
        cpp_source += file.read()
        cpp_source = "/*\n" + header + "*/\n" + cpp_source

    with open(source + "Default.py", "r") as file:
        py_source += file.read()
        py_source = '"""\n' + header + '"""\n' + py_source

    with open(source + "Main.java", "r") as file:
        java_source += file.read()
        java_source = "/*\n" + header + "*/\n" + java_source


    for count in range(1, n+1):
        if not only_cpp:
            os.makedirs(path + "/p" + str(count))
            with open(path + "/p" + str(count) + "/sol.c", "w") as file:
                file.write(c_source)
            with open(path + "/p" + str(count) + "/Main.java", "w") as file:
                file.write(java_source)
            with open(path + "/p" + str(count) + "/sol.py", "w") as file:
                file.write(py_source)
            with open(path + "/p" + str(count) + "/sol.cpp", "w") as file:
                file.write(cpp_source)
        else:
            with open(path + "/p" + str(count) + ".cpp", "w") as file:
                file.write(cpp_source)

        local = ["debug.py", "err.err", "generator.py", "in.in", "out.out", "out1.out"]
        local += ["out2.out", "run.py", "verify.py"]

        if not only_cpp:
            local += ["test.c", "test.cpp", "test.java", "test.py"]
        else:
            local += ["test.cpp"]

        for file in local:

            if only_cpp:
                shutil.copy(source + file, path + "/" + file)
                if "verify" in file or "run" in file or "debug" in file or "generator" in file:
                    pre = ""
                    with open(path + "/" + file, "r") as target:
                        pre += target.read()
                    with open(path + "/" + file, "w") as target:
                        pre = '"""\n' + header + '"""\n' + pre
                        target.write(pre)

                elif ".py" in file:
                    with open(path + "/" + file, "w") as target:
                        target.write(py_source)
                        
                elif ".c" in file or ".java" in file:
                    with open(path + "/" + file, "w") as target:
                        if ".cpp" in file:
                            target.write(cpp_source)
                        elif ".c" in file:
                            target.write(c_source)
                        else:
                            target.write(java_source)

            else:
                shutil.copy(source + file, path + "/p" + str(count) + "/" + file)

                if "verify" in file or "run" in file or "debug" in file or "generator" in file:
                    pre = ""
                    with open(path + "/p" + str(count) + "/" + file, "r") as target:
                        pre += target.read()
                    with open(path + "/p" + str(count) + "/" + file, "w") as target:
                        pre = '"""\n' + header + '"""\n' + pre
                        target.write(pre)

                elif ".py" in file:
                    with open(path + "/p" + str(count) + "/" + file, "w") as target:
                        target.write(py_source)
                        
                elif ".c" in file or ".java" in file:
                    with open(path + "/p" + str(count) + "/" + file, "w") as target:
                        if ".cpp" in file:
                            target.write(cpp_source)
                        elif ".c" in file:
                            target.write(c_source)
                        else:
                            target.write(java_source)

else:
    name_of_file = input("Name of file: ")
    os.system("touch " + path + "/" + name_of_file)
    if ".cpp" in name_of_file:
        shutil.copy(source + "Default.cpp", path + "/" + name_of_file)
    elif ".c" in name_of_file:
        shutil.copy(source + "Default.c", path + "/" + name_of_file)
    elif ".java" in name_of_file:
        shutil.copy(source + "Main.java", path + "/" + name_of_file)
    else:
        shutil.copy(source + "Default.py", path + "/" + name_of_file)

print("Opening {} in VS Code".format(path))
os.system("code " + path)
print("Done")