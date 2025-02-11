# Default Parameters

def add_two_numbers(a, b=10):  # Default Parameter of b is 10
    """Returns the sum of two numbers"""
    sum = a + b
    return sum

print(add_two_numbers(5))

print("-------------------------------------")

# Flexible Arguments

def add_n_numbers(*args):
    """Returns the sum of n numbers"""
    sum = 0
    for num in args:
        sum += num
    return sum
#print(add_n_numbers(2,3,7,9,80,70))
sum1 = add_n_numbers(90.1, 30.5)
print(type(sum1))
print(sum1)


print("-------------------------------------")

# More than one Default Parameter
# Define shout_echo
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Make echo_word uppercase if intense is True
    if intense is True:
        # Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo("Hey", 5, True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo("Hey", intense=True)

# Print values
print(with_big_echo)
print(big_no_echo)

# Function with variable legth arguments
# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge = ""

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish("luke")

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)

print("-------------------------------------")

# Function using kwargs
# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke", affiliation="jedi", status="missing")

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")

print("-------------------------------------")

def print_students(**kwargs):
    """ Prints students details that is name and student number"""
    for key, value in kwargs.items():
        print(key + ":" + value)

print(print_students(name="John", student_number="123456"))

print("-------------------------------------")

# Write a function that takes Key word arguments of employee details, containing(name, age , ID, salary, marital status).
#  Call the funtion for two employees.

def employee_details(**kwargs):
    """ Prints employee details"""
    for key, value in kwargs.items():
        print(key + ":" + value)

employee_details(name="John", age="25", ID="123456", salary="10000", marital_status="Single")
employee_details(name="Jane", age="30", ID="123457", salary="20000", marital_status="Married")