import random

class Account:
    id = ''
    name = ''
    balance = ''
    def __init__(self, name, balance):
        self.id = f"{random.randint(100000000, 9999999999)}"
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"


ali = Account("Ali Abu", 1000000)
wong = Account('Wong CK', 500000)
siva = Account('Sivarajah', 1500000)


savingaccs = dict = {
    ali.id: ali,
    wong.id: wong,
    siva.id: siva
    }

for key in savingaccs:
    print("Account No:" + key + " Name: " + savingaccs[key].name )