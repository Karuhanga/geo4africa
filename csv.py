import csv

INFO= []
with open("data.csv", 'r') as file:
	data= csv.reader(file)
	for item in data:
		INFO.append(item.split(","))

print INFO