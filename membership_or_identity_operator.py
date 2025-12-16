'''
Membership  operator 

doers the give alue is present in the list , tuple ,dictornary etc 
keyword - "in"

Identity operator - it is used to check that if two thing correspondes ya refer to same memory location
keyword - "is"
== is for value camparison , of value is exactly same or not
but is - for memory location same or not

'''

list = ["suvi",100,"rockstar","Hacker"]
a= "Hacker" in list
print(a)

x=3
y=3

print(x is y)    # True because python reuse the small vallues for eg int that cannot change here x and y both pointing to 3

l1=[1,2]
l2=[1,2]
print(l1 is l2)   # False , because list are mutable can be change if i append something to y then it change so here l1 and l2 is pointing to [1,2]
print(l1==l2)


