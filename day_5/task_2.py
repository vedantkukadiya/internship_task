#Read and Display CSV Data Using Python
import csv
with open('day_5/record.csv', mode ='r')as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(f"Header: {header}")
    for row in csvreader:
        print(row)
