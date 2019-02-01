import csv
from operator import itemgetter


gradesFile = open("grades.csv", "r")
gradesCSV = csv.reader(gradesFile)

table = []
for row in gradesCSV:
	row1 = [row[0], int(row[1]), int(row[2]), int(row[3])]
	table.append(row1)

gsort = sorted(table, key=itemgetter(3), reverse=False)

for r in gsort:
	print(r)




