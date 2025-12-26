'''
Create a pie chart using matplotlib to represent the following data:
Languages  Popularity
Python     30
Java       25
C++        20
JavaScript 15
Ruby       10 
'''


# import matplotlib.pyplot as plt

# languages=["python","java","c++","javascript","Ruby"]
# popularity=[30,25,20,15,10]

# plt.plot(languages,popularity)
# plt.xlabel("languages")
# plt.ylabel("popularity")
# plt.title("Languages and their Popularity ")
# plt.grid()
# plt.show()


# for pie chart

import matplotlib.pyplot as plt

languages=["python","java","c++","javascript","Ruby"]
popularity=[30,25,20,15,10]

plt.pie(popularity,labels=languages,autopct='%1.1f%%')
plt.title("Languages and their Popularity ")
plt.show()