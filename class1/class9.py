### Inheritence
## True reuse of code 
## Parent - Child
### Inherit both attributes and methods. Override or extend. 

# class User:

#     def __init__( self, name, id, balance):
#         self.name = name
#         self.id = id
#         self.balance = balance
             
#     def deposit(self, amount):
#         self.balance += amount
#         return self

#     def withdraw(self, amount):
#         self.balance -= amount
#         return self


#     def transfer_amount(self, other_user, amount):
#         other_user.deposit(amount)
#         self.withdraw(amount)

# class Bankaccount(User):

#     def __init__(self, name, id, balance, int_rate):
#         super().__init__(name, id, balance)
#         self.int_rate = int_rate 


#     def make_deposit(self, amount):
#         super().deposit(amount)

#     def withdraw(self, amount, age):
#         if age < 60:
#             print("you cannot Withdraw before you turn 60")
#         else:
#             super().withdraw(amount)

    
#     def display_accout_balace(self):
#         print( self.name, "Balance", self.balance)
#         return self


# Jack = Bankaccount("Jack", "id005", 0 , 0.25)
# Jack.make_deposit(7000)
# Jack.display_accout_balace()
# Jack.withdraw(2000, 69)
# Jack.display_accout_balace()


        
##While Loops

# for num in range(0,10):
#     print(num)

# num = 0
# while num < 11:
#     print(num)
#     num += 1

# arry = [2,5,6,8]

# for iter in arry:
#     print(iter)

# iter = 0
# while iter < len(arry):
#     print(iter , arry[iter])
#     iter += 1

## Data structures

##linked list
##D linked list
##Trees
##Graphs
##tie

# arry = [2,5,6,8,9,2,7]

# arry.sort()
# print(arry)

###Bubble sort
arry = [2,5,6,8,9,2,7]

def bubblesort(arry):
    for outer in range(len(arry)-1):
        print(arry)
        for iter in (range(len(arry)-1-outer)):
            if arry[iter] > arry[iter + 1]:
                arry[iter], arry[iter + 1] = arry[iter + 1],arry[iter]
    return(arry)

print(bubblesort(arry))


