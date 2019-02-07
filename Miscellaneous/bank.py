

class BankAccount:
    def __init__(self, balance=0):
        self.balance = 0
        print("Account opened.")
        self.print_balance()
    def deposit(self,amount):
        self.balance += amount
        print("${} deposited.".format(amount))
        self.print_balance()
    def withdraw(self,amount):
        self.balance -= amount
        print("${} withdrawn.".format(amount))
        self.print_balance()
    def print_balance(self):
        print("Account balance is ${}.".format(self.balance))
    def transfer(self, other_account, amount):
        self.withdraw(amount)
        other_account.deposit(amount)
    def __str__(self):
        return "Account with balance of ${}".format(self.balance)
    def __repr__(self):
        return "BankAccount(balance={})".format(self.balance)
