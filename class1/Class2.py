##Files>Module>Package>Library>Framework>Application




# ##Data types
# ## Primitive: Numbers, Boolean, string

##Printing Strings

corpName = "ItMunk"
stateName = "Virginia"

print("Welcome to ", corpName)

print(f"Welcome to {corpName}")

print("Welcome to %s, %s" %(corpName, stateName))

##String Methods
corpName = "ItMunk"

print(corpName.upper())

print(corpName.split())

print(corpName.count('It'))

##How to find the type of data
corpName = "ItMunk"
print(type(corpName))

corpZip = "20105"
print(type(corpZip))

corpZip = int(corpZip)
print(type(corpZip))

##Numbers: int and float
## Arthimetic Operators +, - , *, %, / 
## logical >, <, >=, <=, ==
##if, elseif, else statements

##Zipcode validation 
corpZip = input("Enter zip code \n" )
if (len(corpZip) == 5) :
    print("Zipcode valid")
else:
    print("Zipcode invalid")
##Type casting 
corpZip = input("Enter zip code \n" )
corpZip = int(corpZip)
print(isinstance(corpZip, int))
## Passing a vaule to a variable
## eliminating the duplicates by converting from list to set 
## printing 

# 2

# # ## Composite: Lists, Tuples, Set, dict




# # ##Variables

# # num1 = 45
# # # num2 = 40
# # num3 = num1 + num2
# # print(num1 + num2)

# ##How to pass values to Variables
# ## 1.Initiate the variable with a value
# ## 2.Declare the variable by declaring in bash
# ## 3.Assing the value by user input 

# ##Variable.py
# import os
# ##assign a value for the variable

# os.environ
# num1 = 20
# num2 = 50

# num3 = num1 + num2
# print(num3)
# ##assign a value through user input

# num4 = int(input("please enter a value for num4:\n "))

# num3 = num3 + num4
# print(num3)

# ##assign the value from the bash env variable

# num5 = os.environ["num5"]
# num5 = int(num5)
# num3 = num3 + num5

# print(num3)
