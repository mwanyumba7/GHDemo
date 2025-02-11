# Normal Function 
#from math import sqr

def raise_to_power(a,b):
    """Returns the power of a raised to b"""
    power = a ** b
    return power
print(raise_to_power(2,3))

print("-------------------------------------")

# A Lambda Function 
# Syntax: Func_name = lambda arguments/paameters : action
raise_to_power_lambda = lambda num1, num2 : num1 ** num2 
print(raise_to_power_lambda(8,30))

print("-------------------------------------")

# Write a Lambda function to concatenate two strings(Continent and Country) 

# Error handling 

def square_root(a):
    """Returns the square root of a number"""
    return a ** 0.5

print(square_root(-9))

print("-------------------------------------")

#Error Handling with the "try" and "except" clause
#Similar to "break" and "continue" statements in loops

def sqrt(b):
    """Returns the square root of a number
    But if the parameter passed is not a float/integer,
    It will return an error message"""
    try:
        return b ** 0.5
    except:
        print("Input must be an Integer ot float value")
        
print(sqrt(-10000))

print("-------------------------------------")

#Assignment
#Look into Anonymous Functions in respect to using lambda functions 
# Create an Anonymous function using the map()(Built in function) funnction
# Create a try and except clause for a sqaureroot function not to accept negative values  
#Create another try and except clause for when there is an import error in the math module importation 