# list = [103,100,20,500]
# print(list)
# print(list[0])
# print(list[0:2])
# list.sort()
# print(list)
# list.reverse()
# print(list)
# print(list.pop(2))
# print(list)

# #store all prime no btw range from x to y in a list

prime =[]
x=int(input("x : "))
y=int(input("y : "))

for i in range(x,y):
    for j in range(2,i):
        if( i%j==0):
          break
        else:
            prime.append(i)




# ask the user to enter any name . if the name has a given set of string "the" , it has to stored in a list .print the list

# name_containing_the =[]
# n=int(input("how many names you want to enter : "))
# for i in range(n):
#     name=input("enter the name : ")

#     if "the" in name.lower():
#         name_containing_the.append(name)

# print(name_containing_the)

