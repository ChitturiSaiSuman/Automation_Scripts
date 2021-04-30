# Reads a CSV file and outputs required fields
import csv
filename = input("Enter Filename: ")
fields = []
rows = []
with open(filename,'r') as csvfile:
	csvreader = csv.reader(csvfile)
	fields = next(csvreader)
	for row in csvreader:
		rows.append(row)
print('\t'.join(field for field in fields))
"""
for row in rows:
	for col in row:
		print("%s"%col,end="\t")
	print()
"""
answer = []
query = input("Enter any item to search: ")
for row in rows:
	for col in row:
		if query in col:
			answer.append(row)
for i in answer:
	for j in i:
		print(j,end=" ")
	print()
