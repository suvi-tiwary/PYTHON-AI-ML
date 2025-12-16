'''
Create a pie chart using matplotlib to represent the following data:
Languages  Popularity
Python     30
Java       25
C++        20
JavaScript 15
Ruby       10

'''

import matplotlib.pyplot as plt
print("matplotlib works")


Languages=["python","java","c++","javascript","Ruby"]
Popularity=[30,25,20,15,10]

plt.plot(Languages,Popularity)
plt.xlabel("Languages Name in the programming world ",color="red")
plt.ylabel("Popularity across the world", color="green")
plt.grid(True)
plt.show()