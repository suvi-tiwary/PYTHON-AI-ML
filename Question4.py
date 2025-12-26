'''Write a program to reverse the contents of a file character by character,
separating each character with a comma'''


with open("file.txt","r") as f:
    data=f.read()
    
    reversed=data[::-1]
    seperated=",".join(reversed)

with open("file.txt","w") as f1:
    f1.write(seperated) 
    print("Reversed contend is appended in the file.txt")


    