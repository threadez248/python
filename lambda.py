## What is Lambda : anonymous function or function without name
## Usecase is you can pass a function as an argument, quick function

# def double(num):
#     x = num + num
#     return x

# print(double(6))

# lambda num: num + num


# x = lambda a : a + 10
# print(x(5)) 


#Example 2
# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = list(filter(lambda x: (x%2 == 0) , my_list))
# print(new_list)


# #Example 3
# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = list(map(lambda x: x * 2 , my_list))
# print(new_list)


#Example 4
import pandas as pd
df = pd.DataFrame({
    'Name': ['Luke','Gina','Sam','Emma'],
    'Status': ['Father', 'Mother', 'Son', 'Daughter'],
    'Birthyear': [1976, 1984, 2013, 2016],
})

df['age'] = df['Birthyear'].apply(lambda x: 2021-x)

print(df)







# listA = [4, "string1", lambda num: num * num]

# print(listA[2](8))


# array = [3,6,7]

# def double(num):
#     return num + num 

# print(list(map(double, array)))


# print(list(map(lambda num: num + num, array)))

