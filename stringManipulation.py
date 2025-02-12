#Types of In-built functions for strings

# .lower() - Converts all characters in a string to lowercase
# .upper() - Converts all characters in a string to uppercase

my_name = 'Ruth-Mwaura'
print(len(my_name))

# Indexing 
print(my_name[4])

print(my_name[0:5])

print(my_name[::-1])  # Reversing a string

print(my_name[-6:])

# Strides 

my_surname = "mwanyumba"
print(my_surname[0 : 6 : 1])

#Splittung a string 

students = "My name is Brayan Kai Mwanyumba"

# We use the .split() method to split a string and return the splitted values as a list
students_list = students.split(sep=" ", maxsplit=1)
print(students_list)

# Split a string starting from the right
students_left = students.rsplit(sep=" ", maxsplit=1)
print(students_left)

print("------------------------------------")

# Escape Sequence
# We can escape a sequence of characters in a string using \n and \r 
# \n - New line
# \r - Carriage return 

sentence1 = "I am a teacher at\n University of Nairobi\n I teach Chemical Engineering"
print(sentence1)

print("------------------------------------")

sentence2 = "I am a teacher at\r University of Nairobi\r I teach Chemical Engineering"
print(sentence2)

print("------------------------------------")

sentence3 = "I am a student at\r Zindua School"
print(sentence3)

print("------------------------------------")

# JOINING Strings 
# We use the .join() method to join strings
# Syntax: separator.join(iterable)

my_list = ["Brayan", "Kai", "Mwanyumba"]
print(" ".join(my_list))

print("------------------------------------")

# Stripping Characters from a string
# We use the .strip() method to remove characters from a string
# Syntax: string.strip(characters)

sentence4 = "I am a student at Zindua school am"
print(sentence4.strip("I am student"))

print("------------------------------------")

# Assignmenmt
# 1. Understand the logic between the .split() and .rsplit() methods
# 2. Look into the \r escape sequence and understand how it works with code examples
# 3. Try and see if the issues we faced with \r and .split() are re;lated to python versions 
# 4. Look into Finding and Replacing Strings 
#       - Use the .find() method to find a string in a string
#       - Use the .index() method to find a string in a string
#            - Implement try and accept clause to handle value error when you dont find the string
# 5. Use .count() method to count the number of times a substring appears in a string 
# 6. Use the .replace() method to replace a substring in a string with another substring