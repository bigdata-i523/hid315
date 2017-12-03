import csv
with open ('tbi assessment.csv') as file:
    reader = csv.reader(file) 
    for row in reader:
        print (row)
