"""
This is week 1 of the Python Bootcamp for Data assignment. All of your questions
for this week will come commented out.
To pass, all automated testing of your inputs have to pass their tests.
"""


# The following exception is breaking the function. You haven't seen
# functions yet, but concentrate in fixing the exception so that:
# * the exception doesn't happen
# * The exception_message is correctly defined as a string
def create_message():
    try:
        exception_message = "This message is broken " + str(1)
    except RuntimeError:
        raise
    return exception_message


# Make single_string use both the `name` and `greeting` variables to
# create a single string. The single_string should be a string and not a `None`
name = "Monday"
greeting = "Hello students!"
single_string = f"{greeting} It's {name}"


# Use the following text to create a string and assign it to quoted_string:
# Sometimes you can use a ' character to denote minutes or " for seconds
quoted_string = """Sometimes you can use a ' character to denote minutes or " for seconds"""


# The current condition does not evaluate correctly. Python has truthy values
# and dictionaries is one of them. Update the code so that has_contacts will
# evaluate to True instead of False
contacts = {"Key": "Value"}
if contacts:
    has_contacts = True
else:
    has_contacts = False


# Make the numbers_string variable use both the `apples` and `cost` variables to
# create a single string. The numbers_string should be a string and not a `None`
# Feel free to use any text within the string, however, it must include both the
# `apples` and `cost` variables
apples = 4
cost = 7.3
numbers_string = f"I had {apples} apples which cost {cost} in total."


# from the following dictionary, define the file_sizes variable to hold all the sizes
files = {
    "HEAD": 344,
    "config": 84,
    "index": 93,
    "logs": 14,
    "objects": 55,
    "packed-refs refs": 120,
}
file_sizes = files.values()

# from the same `files` dictionary, define the file_names variable so that it holds
# the names only
file_names = files.keys()


# from the list of first names below write code that gets rid of Melvin and Carlos
# and assign the resulting list to new_first_names
first_names = [
    'Jason',
    'Melvin',
    'Susan',
    'Rachel',
    'Dean',
    'Helen',
    'Carmen',
    'Xavier',
    'Carlos',
    'Michael'
 ]

first_names.pop(1)
first_names.pop(-2)

new_first_names = first_names

# from the same list of first names, assign the last 4 names to the last_four_names
first_names = [
    'Jason',
    'Melvin',
    'Susan',
    'Rachel',
    'Dean',
    'Helen',
    'Carmen',
    'Xavier',
    'Carlos',
    'Michael'
 ]
last_four_names = first_names[-4:]


# The following code breaks the function. You haven't seen
# functions yet, but concentrate in fixing the exception so that:
# * the exception doesn't happen
# * a fallback value of "John Doe" is returned
def get_name():
    information = {}
    return information.get("Default Value" ,"John Doe")