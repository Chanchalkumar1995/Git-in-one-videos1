class BankAccount:
    
    def __init__(self):
        self.balance=0
        
    def deposit(self,amount):
        self.balance=self.balance + amount
        
    def withdraw(self,amount):
        self.balance-=amount
        
    def __show_balance(self):
        print("Balance is",self.balance)
        
    def is_Auth_True(self,isAuth):
        if isAuth:
            print("You are Auth!!")
            self.__show_balance()
        else:
            print("Not Auth,No bal")  
        
account=BankAccount()
account.deposit(1000)
account.withdraw(499)
account.is_Auth_True(False)
                    