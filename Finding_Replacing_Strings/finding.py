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