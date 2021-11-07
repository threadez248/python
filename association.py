class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdraw(self, amount):
        self.balance -= amount
        return self

    def display_accout_balace(self):
        print( "Balance", self.balance)
        return self



class User:

    def __init__( self, name, id):
        self.name = name
        self.id = id
        self.account_balance = BankAccount(0.05, 0)
        
             
    def deposit(self, amount):
        self.account_balance.make_deposit(amount)
        return self

    def withdraw(self, amount):
        self.account_balance.make_withdraw(amount)
        return self


    def transfer_amount(self, other_user, amount):
        other_user.deposit(amount)
        self.withdraw(amount)




Jack = User("Jack", "id05")
Jack.deposit(7000).account_balance.display_accout_balace().make_withdraw(2000)
Jack.account_balance.display_accout_balace()



