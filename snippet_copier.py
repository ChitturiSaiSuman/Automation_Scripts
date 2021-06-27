import pyperclip
import sys
sys.path.append("/home/suman/Automation_Scripts")

from C_PLUS_PLUS import *

print("Select one from the following languages")

print()
print("1. C")
print("2. CPP")
print("3. Java")
print("4. Python3")
print()

print("Choice: ", end = "")

index = int(input())

if index == 2:
    c_plus_plus_keys = list(c_plus_plus_functions.keys())

    function_name = input("Which Function do you need?: ")
    function_name = list(map(str, function_name.lower().split()))

    function_key = ""

    for function in c_plus_plus_keys:
        if all([key_word in function.lower() for key_word in function_name]):
            function_key = function
            break

    pyperclip.copy(c_plus_plus_functions[function_key])
    pyperclip.waitForPaste(15)
