'''
Food   Calories  Potassium   fat
Meat       250 40 8
Banana     130 55 5
Avocados   140 20 3
Sweet
Potatoes   120 30 6
Spinach    20 40 1
Watermelon 20 32 1.5
water      10 10 0
Beans      50 26 2
Legumes    40 25 1.5
Tomato     19 20 2.5

'''

import matplotlib.pyplot as plt
import numpy as np

food_items=["meat","banana","avocados","sweet potatoes","spinach","watermelon","water","beans","legumes","tomato"]
calories=[250,130,120,20,20,10,50,40,19,15]
potassium=[40,55,20,30,40,32,10,26,25,20]
fat=[8,5,3,6,1,3,0,2,1,5]

width=0.3
x=np.arange(len(food_items))
plt.bar(x-width,calories,width,label="Calories",color="red")
plt.bar(x,potassium,width,label="Potassium",color="blue")
plt.bar(x+width,fat,width,label="fat",color="green")
plt.xticks(x, food_items, rotation=45)
plt.ylabel("amount")
plt.legend()
plt.title("Food Nutrient Comparison")
plt.show()