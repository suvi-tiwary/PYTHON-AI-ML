'''Determine a python function removenth(s,n) that takes an input a string and an
integer n>=0 and removes a character at index n. If n is beyond the length of s,
then whole s is returned. For example:
removenth(“MANGO”,1) returns MNGO
removenth(“MANGO”,3) returns MANO '''


def remove_n_index(s,n):
    if(n>len(s) and n<0):
       return s
    return s[:n]+s[n+1:]

s=input("Enter the string : ")
n=int(input("Enter the index that you want to remove : "))
result=remove_n_index(s,n)
print(result)