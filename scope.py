#Global vs Local Scope Pt 1

def square(value):
    """Returns the square of a number"""
    new_value = value ** 2
    return new_value

print(square(4))

#print(new_value) #This will throw an error because new_value is a local variable and can only be accessed within the function it was defined in

print("-------------------------------------")

#Global vs Local Scope Pt 2

new_val = 14 #This is a global variable

def sqaure2(value):
    """Returns the square of a number"""
    new_val = value ** 2 #This is a local variable
    return new_val
print(sqaure2(5))


print("-----------------------")

print(new_val) #This will print 14 because new_val is a global variable and can be accessed anywhere in the code

print("-------------------------------------")

#Global vs Local Scope Pt 3

new_val2 = 10

def square3(value):
    """Return the Square of a number"""
    new_value3 = new_val2 ** 2
    return new_value3

print(square3(5))

print("-------------------------------------")

# Global vs Local Scope Pt 4

new_val3 = 10

def square4(value):
    """Return the Square of a number"""
    global new_val3
    new_val3 = new_val3 ** 2
    return new_val3

print(square4(3))

print("-------------------------------------")

# Nested Functions Pt 1

def mod2plus5(x1, x2, x3):
    """Returns the reminder plus 5 of three values"""
    new_x1 = x1 % 2 + 5
    new_x2 = x2 % 2 + 5
    new_x3 = x3 % 2 + 5
    return (new_x1, new_x2, new_x3)

print(mod2plus5(3, 4, 5))

print("-------------------------------------")

#Lets Solve this with a nested function

def mod2plus5_1(x1, x2, x3):
    """Returns the reminder plus 5 of three values"""

    def inner(x):
        """Return the remainder plus 5 of a value"""
        return x % 2 + 5
    
    return (inner(x2), inner(x1), inner(x3))
print(mod2plus5_1(9,11,30))

print("-------------------------------------")

#Assignment  - Nathan
#1. Look into default and Flexible arguments in functions
#Default arguements
#Default arguements
"""used to simplify function by assigning default values to parameters with similar arguements"""

def selling_price(buying_price,discount=0,tax=50):
    """finding net price by adding tax to buying price and subtracting discount"""
    costing=(buying_price + tax - discount)
    return costing
print(selling_price(300,10))

#'Arg'
#'Arg' allows passing of multiple non key elements
def add(*nums):
    """summing multiple non key tuple element"""
    total=0 #initializing
    for num in nums:
        total += num
        return total
print (add(90,76,93,71,15,83))

#**kwarg
#'**kwarg' allows passing of multiple ky words arguements
def traffic_light(**kwargs):
    """Assigning traffic light colours to expected action"""
    traffic_light={red:"stop"
    ,yellow:"get_ready"
    ,green:"go"}
    for key,value in kwargs.items():
        print (key)

#Assignment  - Ruri
#1. Look into default and Flexible arguments in functions
#2. In flexible arguments look into *args and **kwargs
#3. Look into Lambda Functions

#Assignment  - Ryan
#1. Look into default and Flexible arguments in functions
#2. In flexible arguments look into *args and **kwargs
#3. Look into Lambda Functions

# Default arguments are arguments that are passed to a function that have a default value. 
# If the argument is not passed to the function, the default value is used. 
# Flexible arguments are arguments that can take any number of values. 

#example of default arguments:
def order_1(size = "small", flavor = "vanilla"):
    print(f"Your order is a {size} {flavor} cake")
print(order_1("large", "chocolate"))

#example 2
def introduce(name,city="kigali"):
    print(f"Hello, my name is {name} and I am from {city}")
    
introduce("Ryan")

#fexible arguments are arguments that can take any number of values.
def add_numbers(*args):
    print(args) #this will print the values in a tuple
    return sum(args)
print(add_numbers(23,2,43,34,5))

#example 2 **kwargs
# unlike *args, **kwargs can take any number of keyword arguments and store them in a dictionary
#syntax: def function_name(**kwargs):
def patient_details(**kwargs):
    print(kwargs) #this will print patient details in a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")    
patient_details(name = "John", age = 34, weight = 78)

#lambda functions are anonymous functions that are defined using the lambda keyword
#they are used for creating small, one-time and simple functions
#syntax: lambda arguments: expression
#example
#lamda function used to obtain the squares of a number
#simple lambada shortcut
square = lambda x: (x*x)
print (square(5))

#simple lambda () mapping
scores = [34, 56, 78, 90, 23, 45, 67]
new_scores = list(map(lambda x: x + 5, scores))
print(new_scores)

#lambda function used to determine the value of passing grades in a class(simple lambda filter())
scores = [34, 56, 78, 90, 23, 45, 67]
passing = list(filter(lambda x: x > 50, scores))
print(passing)



#2. In flexible arguments look into *args and **kwargs:
#3. Look into Lambda Functions

#Assignment  - Abdhullahi
#1. Look into default and Flexible arguments in functions
#2. In flexible arguments look into *args and **kwargs
#3. Look into Lambda Functions

#Assignment  - Bethany
#1. Look into default and Flexible arguments in functions
#2. In flexible arguments look into *args and **kwargs
#3. Look into Lambda Functions

#Assignment  - Reagan
#1. Look into default and Flexible arguments in functions
#2. In flexible arguments look into *args and **kwargs
#3. Look into Lambda Functions

#Assignment  - John
#1. Look into default and Flexible arguments in functions
#2. In flexible arguments look into *args and **kwargs
#3. Look into Lambda Functions
