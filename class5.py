


# dict1 = {"name1": ("kumar","kaushik"),"name2": ("kumar2","kaushik2")}
# print(id(dict1["name1"]))

##Stack and Queue

# Queue FIFO 

# Stac : LIFO


##Global,Local 

# name1 = "Modi"
# print(name2)

# def pm(name="", age="0"):
#     # name1 = "Chaiwala"
#     name2 = name1
#     return name2
    



# print(name1)
# print(pm())


# num = 10

# def sum():
#     # global num 
#     print("print2", num)
#     num = (num + 10)
#     print("print4",num)
#     return num

# print("print3", num)
# print(sum())
# print("print5", num)



# list = [2,4,8]
# print(list)
# total = 0

import sys
sys.path.append("/Users/snarla/python")
from utils import sum as sm
def sumDouble(list):
    total = 0
    for item in list:
        item = sm(item)
        total = total + item
    return total 

# print(sumDouble([2,4,8]))

print(sumDouble([2,4,8]))
        










