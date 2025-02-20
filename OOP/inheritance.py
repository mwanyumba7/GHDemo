# Creating a parent class called Bank Account

class BankAccount:
    """Resresents a bank account
    States: balance
    Behaviours: withdraw
    """
    def __init__(self, balance):
        """Initializes the balance attribute"""
        self.balance = balance

    def withdraw(self, amount):
        """Withdraws the amount from the balance"""
        self.balance -= amount

# Creating a child class called Savings Account
class SavingsAccount(BankAccount):
    """
    Represents a savings account thats inheriting from BankAccount
    States : balance, interest_rate
    Behaviours: withdraw, compute_interest
    """
    def __init__(self, balance, interest_rate):  # Constructor specifically for the savings account with an aditional paramete.
      BankAccount.__init__(self,balance)
      self.interest_rate = interest_rate

    def compute_interest(self, n_periods=1):
        """Computes the interest earned for a given period"""
        return self.balance * ((1+ self.interest_rate) ** n_periods - 1)
    
class CheckingAccount(BankAccount):
    """
    Represents a Cheque Book type of account thats inheriting from BankAccount
    States : balance, limit
    Behaviour : withdraw, deposit  
    """

    def __init__(self, balance, limit):
        BankAccount.__init__(self, balance)
        self.limit = limit
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount, fee= 200):
        """Widhraws the amount from the balance with a fee"""
        if fee <= self.limit:
            BankAccount.withdraw(self, amount+fee)
        else:
            BankAccount.withdraw(self, amount+self.limit)

kai_cheque = CheckingAccount(1000, 100) 
print(kai_cheque.balance)

print("------------------------------------")
kai_cheque.withdraw(50)
print(kai_cheque.balance)

print("-------------------------------------")

bethany_acc = BankAccount(1000)
bethany_acc.withdraw(50)
print(bethany_acc.balance)

print("------------------------------------")

check_acc = CheckingAccount(1000, 100)
check_acc.withdraw(50)
print(check_acc.balance)



print("--------------------------------------")

# Constructing a new object of the SavingsAccount class
acc = SavingsAccount(1000,20.7)
print(acc.interest_rate)

savings_account = SavingsAccount(2000, 8.9)

print(isinstance(savings_account, BankAccount))

print("------------------------------------")

print(isinstance(savings_account, SavingsAccount))
