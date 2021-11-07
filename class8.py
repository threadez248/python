
# class User:

#     def __init__( self, name, id):
#         self.name = name
#         self.id = id
#         self.account_balance = 0
             
#     def deposit(self, amount):
#         self.account_balance += amount
#         return self

#     def withdraw(self, amount):
#         self.account_balance -= amount
#         return self


#     def transfer_amount(self, other_user, amount):
#         other_user.deposit(amount)
#         self.withdraw(amount)

# Kumar = User("Kumar", "id01")  ##Creating the Object Kumar
# print(Kumar.account_balance)   ##Printing the default account_balance =0
# Roa = User("Roa", "id02")      ##Creating the Object Roa
 
# Roa.deposit(1000)
# Kumar.deposit(1000)

# Kumar.transfer_amount( Roa, 200)
# print(Kumar.account_balance)
# print(Roa.account_balance)




class BankAccount:
    def __init__(self, int_rate, balance, account):
        self.int_rate = int_rate
        self.balance = balance
        self.account = account

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdraw(self, amount):
        self.balance -= amount
        return self

    def display_accout_balace(self):
        print( self.account ,"Balance", self.balance)
        return self

Act1 = BankAccount(0.025, 10000, "Act1")
Act2 = BankAccount(0.04, 20000, "Act2" )

Act1.display_accout_balace()
Act1.make_deposit(500)
Act1.display_accout_balace()
Act2.display_accout_balace()



    
