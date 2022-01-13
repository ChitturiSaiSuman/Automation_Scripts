# Finds password using grep
import pyperclip
import csv
import sys

filename = "/home/suman/Documents/Chrome Passwords/Passwords.csv"

with open(filename, 'r') as file:
    reader = csv.reader(file)
    fields = next(reader)

    rows = []
    for row in reader:
        rows.append(row)
    
    arguments = sys.argv[1:]
    
    results = []
    for i in range(len(rows)):
        string = ' '.join(rows[i])
        if all([arg in string for arg in arguments]):
            results.append(rows[i])

    print("Results\n")
    for row in results:
        print(row[:len(row) - 1])
    index = int(input("\nEnter Index: "))
    print("Copied password of " + ' '.join(results[index - 1][ :len(results[index - 1]) - 1]))
    pyperclip.copy(results[index - 1][-1])
    pyperclip.waitForPaste(15)
