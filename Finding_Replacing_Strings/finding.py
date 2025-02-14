# We use the .find method when we want to search a target string for a specified substring 
# Syntax: string.find(substing, start, end) "start" and "end" are optional attributes

my_name = "My student names are Brian, Bethany, Brian, Ryan, Abdhulahi"  # Target string
print(my_name)

print(my_name.find("jk", 0, 21))  # Subtring = "Brayan"

print(my_name[0:21])

# Using the .index() method to find a substring in a target string
# Syntax: string.index(substring, start, end) "start" and "end" are optional attributes

#print(my_name.index('kl',0,9))

# Using try and escape to handle the value error
try:
    print(my_name.index("jk"))
except ValueError:
    print("Substring not found")

#Counting Occurences 
# We use the .count() method to count the number of times a substring appears in a target string
# Syntax: string.count(substring, start, end) "start" and "end" are optional attributes

print(my_name.count("a",0,7))

# Replacing Substrings 
# We use the .replace() method to replace a substring in a target string
# Syntax: string.replace(old_substring, new_substring, count) "count" is an optional attribute

print(my_name.replace("Brian", "Brayan", 2))

# RECAP 
"""
STRING MANIPULATION
- Slicing and Concatenation 
- Adjust Cases 
- Split and Join 
- Removing Characters from beggining and end(Stripping)
- Finding Substrings
- Counting Occurences 
- Replacing Substrings 
"""

# Assignment 
"""
FORMATTING IN STRINGS (With Code Examples)
Look into the following methids of formatting 
   a) Positional Formatting
        i) Reodering Values
        ii) Named Placeholders
        iii) Format Specifiers
   b) Formatted String iterals 
        i) F-strings
        ii) Type Conversion
        iii) Format Specifiers(datetime)
        iv) Escape Sequences in F-strings
   c) Template Method of Formatting strings
        i) Substitution
        ii) Safe Substitution

Why should you use 
 - `stt.format()
 - f-strings
 - Template strings 
"""

print("******************************8")

#A. Positional Formatting
#i) Reordering Values
"""Positional formatting allows you to reorder values inside a string using placeholders {}."""

# Reordering values
print("My name is {1}, and I am {0} years old.".format(25, "John"))

#ii) Named Placeholders
""" Named placeholders allow you to use keywords instead of positions. """

print("My name is {name}, and I am {age} years old.".format(name="John", age=25))

#iii) Format Specifiers
""" Format specifiers help control decimal places, alignment, and padding."""

# Displaying numbers with specific decimal places
num = 3.14159
print("Pi to 2 decimal places: {:.2f}".format(num))  

# Padding numbers with zeros
print("The number is {:05d}".format(42))  
"""
1. {} → This is a placeholder for formatting the number.
2. :05d → This is a format specifier:
3. 0 → Pads the number with leading zeros.
4. 5 → Ensures the total width of the output is 5 characters.
5. d → Specifies that the value is an integer (decimal format).
6. format(42) → Inserts the number 42 into the placeholder.
"""

# B. Formatted String Literals (f-strings)
#i) F-strings
""" F-strings use an f before the string and allow direct variable interpolation. """

name = "John"
age = 25
print(f"My name is {name}, and I am {age} years old.")

#ii) Type Conversion
"""F-strings allow automatic type conversion with !r, !s, and !a."""

number = 42
print(f"The number in repr format: {number!r}")  

#iii) Format Specifiers (datetime)
"""You can format dates inside f-strings. """

from datetime import datetime
now = datetime.now()
print(f"Today's date: {now:%B %d, %Y}")
"""
f"Today's date: {now:%B %d, %Y}"

Uses an f-string to format the date.
%B → Full month name (e.g., "February").
%d → Day of the month (e.g., "14").
%Y → Full year (e.g., "2025")
"""

#iv) Escape Sequences in F-strings
""" Escape sequences allow special characters inside f-strings. """

print(f"She said, \"Hello!\"")  


#C. Template Method of Formatting Strings
"""The string.Template class provides an alternative to format() and f-strings."""

from string import Template
template = Template("Hello, $name!")
print(template.substitute(name="John"))


#i) Substitution
"""If a value is missing, substitute() raises an error."""

template = Template("Hello, $name!")
# print(template.substitute())  # KeyError if 'name' is missing

#ii) Safe Substitution
"""safe_substitute() avoids errors by leaving placeholders unchanged."""

template = Template("Hello, $name!")
print(template.safe_substitute())  #Using safe_substitute() to Prevent Errors
