# ##Fibanocci series using recurssion

# # from memoization import cached
# # @cached(max_size=1000)

# # def fib(n):
# #     if (n == 1) or (n == 2):
# #         return 1
# #     elif (n>2):
# #         return fib(n - 1) + fib(n - 2)


# # for num in range(1,1100):
# #     print(num, fib(num))

# # import os 
 
# # ##Fibanocci series using recurssion
# # print(os.path.exists("/Users/snarla/python/class6.py"))


# # print(os.walk("/Users/snarla/python/class6.py"))


# import requests
# response = {}

# base_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"

# response = requests.get(base_url)

# print(response.json)




from requests.api import get


class User:
    def __init__(self, name, email, id):
        self.name = name
        self.email = email
        self.id = id
        self.account_balance = "0"

kumar = User("yanamandra", "kk.tt", "dasf98")



