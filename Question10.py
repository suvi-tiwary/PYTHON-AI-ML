'''Construct a function perfect_square(number) that returns a number if it is a perfect
square otherwise it returns -1.
 For example:
perfect_square(1) returns 1
perfect_square (2) returns -1'''

import math

def perfect_square(number):
    if(number<0):
        return -1
    root=math.sqrt(number)
    if(root*root==number):
        return number
    else:
        return -1
n=int(input("Enter the number : "))    
result=perfect_square(n)
print(result)
