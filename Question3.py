'''
Write a Python function to count the frequency of each character in a
given string and return the output in a dictionary. Example:
char_frequency("HELLO") returns {"H":1, "E":1, "L":2, "O":1}
'''

def count_freq_of_char(s):
    d={}
    for ch in s:
        if(ch!="\n" and ch!=" "):
            if(ch in d):
                d[ch]+=1
            else:
              d[ch]=1   
    return d          

s=input("Enter the string : ")
result=count_freq_of_char(s)
print(result)


