import csv
import random
import os


f = open('MapData.csv')
csv_f = csv.reader(f)

for row in csv_f:
    row[8] = round(random.uniform(0.01, 1), 2)
    print(row[8])

f.close()
