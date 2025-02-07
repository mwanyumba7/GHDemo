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


#Assignment  - John
#1. Look into default and Flexible arguments in functions
#2. In flexible arguments look into *args and **kwargs
#3. Look into Lambda Functions

#Assignment  - John
#1. Look into default and Flexible arguments in functions
""""
A default function calls the function without argument, it uses the default value:
"""
def DS_students(Town = "Juja"): #using a default parameter
  print("I am a Zindua student and I am from " + Town)

DS_students("Tatu City")
DS_students("Kasarani")
DS_students()
DS_students("Dagoretti")

#2. In flexible arguments look into *args and **kwargs
"""
If you not sure of how many arguments to pass to a function, 
you can add * before the parameter name, this is known as *args
"""
def DS_students(*students):
  print("The Zindua DS Student that comes from Juja is " + students[0])

DS_students("John", "Ryan", "Ruri")

"""
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: 
** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
This is known as **kwargs
"""
def DS_students(**student):
  print("The Zindua DS Student that comes from Juja is " + student["student3"])

DS_students(student2 = "John", student1 = "Ryan", student3 = "Gichia")


#3. Look into Lambda Functions
"""
A lambda function is a small, anonymous function that can have any number of arguments but only one expression.
The syntax is lambda arguments : expression
"""
#The exponential function raises y to power x and adds the product of yx and 5 using the lambda function
Exponential_function = lambda x,y: y ** x + y*x + 5 
print(Exponential_function(5,6))

#A lambda function using 4 arguments
quadratic_equation = lambda a,b,c,x: a*(x**2) + b*x + c
sum1 = quadratic_equation(2,3,5,-4)
sum2 = quadratic_equation(2,3,5,4)
print([sum1,sum2])

"""
A lambda function can take several arguments but should be in one expression
"""