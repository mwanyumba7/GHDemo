class Customer:
    """Represent a customer
    States : name, balance
    Behaviours : None
    """

    def __init__(self,name,balance, id):
        self.name, self.balance, self.id = name, balance, id

customer1 = Customer("Reagan", 1000, 123)
customer2 = Customer("Reagan", 1000, 123)

print(customer1 == customer2)

print("------------------------------------")

print(customer1)

print("------------------------------------")

print(customer2)

print("------------------------------------")

# Persforming Comparison of objects
class BankCustomer:
    """Represent a bank customer 
    States : name, id
    Behavior: __eq__ (Compare Objects of Our class)"""

    def __init__(self, id, name):
        self.id, self.name = id, name

    def __eq__(self, other):
        #diagnostic print out
        print("eq has been called. Performing comparison now")

        # Returns true if all attributes Match
        return(self.id == other.id and\
               self.name == other.name)

cust_1 = BankCustomer(110, "Kai")
cust_2 = BankCustomer(110, "Kai")

print(cust_1 == cust_2)

"""
With Code Examples:
    - Look into the __hash__ method in OOP
    - Understand the Liskov Substitution Principle and write code examples of when it is met and when not met 
"""
