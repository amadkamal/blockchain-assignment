
from Q1 import Account 

class DevAccount(Account):
    def __init__(self, name, balance):
        super().__init__(self, name, balance)
    
    def GetBalance():
        return super().balance
    
    def SetBalance(balance):
        super().balance = balance

    def transfer(target: Account, amount):
        target.deposit(amount)
        super().withdraw(amount)
    