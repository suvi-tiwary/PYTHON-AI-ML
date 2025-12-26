'''
def count(s):
for str in string.split():
s = “&”.join(str)
return s
print(count(“Python is fun to learn.”)) 
'''


def count(s):
    for ch in s.split():
        s= "&".join(ch)
    return s

s=input("Enter the string : ")
result=count(s)    
print(result)