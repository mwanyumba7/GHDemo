
#print("This is my First Function in Python by Bethany")


 #   print(new_value)
 #   print(value2,"is half the entered number")

#square()

print("-------------------------------------")

# A function that takes a value as an argument
def divide_by_2(value):
    new_value = value / 2
#    print(new_value)

divide_by_2(4)

print("-------------------------------------")

# Function Parameters
# Return a value from a function using the return keyword

def multiply_by_hundred(value):
    new_value = value * 100
    return new_value

prediction = multiply_by_hundred(0.7598)

#print(prediction)

print("-------------------------------------")

# DocStrings
# Describe what your function does, Serve as Documentation

def divide_by_6(value):
    """Returns the value of a number divided by 6"""
    divided_by_6 = value / 6
    return divided_by_6

print("-------------------------------------")

#Multiple Parameters and Return Values 

def mutilpy_by_hundred(prediction1, prediction2, prediction3):
    new_value1 = prediction1 * 100
    new_value2 = prediction2 * 100
    new_value3 = prediction3 * 100
    return (new_value1, new_value2, new_value3)

predictions= mutilpy_by_hundred(0.7598, 0.9876, 0.679)

#print(predictions)

print("-------------------------------------")

# Returning Multiple Values
def raise_two(value1, value2):
    """Raise value1 to the power of value2 and vice versa"""
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1

    new_tuple = (new_value1, new_value2)

    return new_tuple

result = raise_two(4, 5)

#print(result)

print("-------------------------------------")

#print(type(result))
#Write a function that takes key word arguments of employee details, containing(name, age, ID, salary)
#Call the function for two employees
def employee_details(**kwargs):
    "Print employee details that is name, age, ID and salary"
    for key, value in kwargs.items():
     print(key + ":" + str(value))

employee_details(name="Roy",age="18",ID="200045",salary="Ksh 40000")        
employee_details(name="Dylan",age="22",ID="300046",salary="Ksh 50000")
print("employee_details")        