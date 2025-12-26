'''Write a program to read data from a CSV file 'students.csv', calculate the
average marks for each student, and display the results'''


import csv

with open("studentcsv.txt","r") as f:
    data=csv.DictReader(f)

    for row in data:
        total=int(row["maths"])+int(row["science"])+ int(row["english"])
        avg=total/3
        print(row["name"], "Average : ",avg)