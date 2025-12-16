

import csv

with open("file.txt","r") as f:
    reader=csv.reader(f)
    header=next(reader)

    for row in reader:
        name=row[0]
        marks=[]
        for mark in row[1:]:
          marks.append(int(mark))
        avg=sum(marks)/len(marks)
        print(f"avg marks of {name} is : ",avg)
              
    