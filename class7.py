###OOPS 
### Inheritence , Polymorphism, Encapsulation and Abastraction

### Inheritence

##Polymorphism - 

# print(type("adsad"))

# print(type(("adsad", "adfsad")))

# Encapsulation

###Abstction 

class User:

    def __init__( self, name, id):
        self.name = name
        self.id = id
        self.account_balance = 0
             
    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        self.account_balance -= amount
        return self


    def transfer_amount(self, other_user, amount):
        other_user.deposit(amount)
        self.withdraw(amount)


Kumar = User("Kumar", "id01")  ##Creating the Object Kumar
print(Kumar.account_balance)   ##Printing the default account_balance =0
Roa = User("Roa", "id02")      ##Creating the Object Roa
 
Roa.deposit(1000)
Kumar.deposit(1000).deposit(1000).withdraw(200)
# Kumar.transfer_amount(Roa, 100) ##Attributes of Kumar Object are refferred by self
User.transfer_amount(Kumar, Roa, 400)

print(Kumar.account_balance)
print(Roa.account_balance)
        
        



    



    

# Kumar = User("kumar", "iohdfo789", 90)

# # print(Kumar.deposit(100))

# print(Kumar)






    








