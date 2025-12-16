'''
Write a program to reverse the contents of a file character by character,
separating each character with a comma. 
'''

with open("file.txt","r") as f:
    data=f.read()

reversed_data=data[::-1]
result = ",".join(reversed_data)  

with open("outputfile.txt", "w") as w:
    w.write(result)

print("file completed successfully")