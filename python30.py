'''
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance #for private use __
    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount
    def show_balance(self):
        print("The balance is ",self.wallet_balance)
c1=Customer(100, "Gopal", 24, 1000)
print(c1.__wallet_balance)       #error because it is outside class

c1.show_balance()
'''
#---------------------------------------------------------
#31
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance #for private use __
    def set_balance(self, amount):
        if amount < 50000 and amount > 0:
            self.__wallet_balance += amount
    def get_wallet_balance(self):
        return self.__wallet_balance
        
c1=Customer(100, "Gopal", 24, 1000)
print(c1.get_wallet_balance())      
c1.set_balance(5000)
print(c1.get_wallet_balance())
