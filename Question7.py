'''
Write a program to read a CSV file and display the rows where a
specific column value exceeds a given threshold.
'''


import csv

with open("csv.txt","r") as f:
    threshold=75
    data=csv.DictReader(f)
    for row in data:
        if(int(row["marks"])>threshold):
            print(row)