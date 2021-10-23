##Dict



##key:Value
##string:tuple
# print(dict1)
# print(type(dict1))
dict1 = {
    "id001":("kumar","VA"), 
    "id002":("Roa",9009) 
     }



# # print(dict1.get("id002"))
# dict1.update({"id002":("kk","MA")})
# print(dict1)

# for key,value in dict1.items():
#     print(key,value)

##Functions 
##Reuse 
##modularity

# ##Sytax 
# def Greetings(name):
#     return

# Greetings("Roa")

# def sum(num1, num2):
#     sum = num1 + num2
#     return sum

# sum1 = sum(10, 20)
# sum2 = sum(sum1, 90)
# print(sum2)


### Fizzbuzz program
import timeit
# from memoization import cached
# @cached(max_size=1000)

import timeit
import random
 
def test(): 
    return random.randint(10, 100)
 
starttime = timeit.default_timer()
print("The start time is :",starttime)
def fizzbuzz(lowr,upr):
    for num in range(lowr,upr):
        if (num % 2 == 0) and (num % 3== 0):
            print(num, "fizzbuzz")
        elif(num % 2 == 0):
            print(num, "fizz")
        elif( num % 3 == 0):
            print(num, "buzz")
        else:
            print(num)

print("The time difference is :", timeit.default_timer() - starttime)
fizzbuzz(1,100)


# ## Fibinocci series
# 1,1,2,3,5,8,13

##0.0074283749999999316
##0.00758054400000141


















