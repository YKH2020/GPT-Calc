"""
This is week 2 of the Python Bootcamp for Data assignment. All of your questions
for this week will come commented out.
To pass, all automated testing of your inputs have to pass their tests.
"""


# This function has a syntax error, no tests will run until this function is
# fixed first
def invalid(domain ,prefix="https"):
    pass


# The following function needs to use variable arguments to work. The developer
# created this function with a single argument which is breaking the tests. We
# need this function to change to allow any number of arguments
def create_urls(*domains):
    return [f"https://{domain}/" for domain in domains]


# This function creates a dictionary based on the arguments passed in. The
# `metadata` argument is expected to be a dictionary and the `username`
# argument to be a string. Update the function so that:
# - It accepts a new keyword argument named `verified` which default to `False`
# - Changes `metadata` argument to be a variable keyword argument
def social_media_user(username, verified=False, **metadata):
    information = {
        "username": username,
        "verified": verified
    }

    information.update(metadata)
    return information


# This class has a problem with the `as_celsius` method. Update the class so
# that the method works correctly and the test passes
class Fahrenheit:

    def __init__(self, value):
        self.value = value

    def as_celsius(self):
        return (self.value - 32) / 1.8


# The two social media classes have a `verified` and `url` methods
# that can come from a base class instead.
# Update the classes so that:
# - They both inherit from a base class (you must create a new one)
# - The `verified` and `url` methods come from the base class
class SocialMediaUser:
    def url(self):
        return f"{self.domain}/{self.username}"

    def verified(self):
        if self.username:
            return True
        return False

class TwitterUser(SocialMediaUser):

    domain = "https://twitter.com"

    def __init__(self, username):
        self.username = username

class LinkedInUser(SocialMediaUser):

    domain = "https://linkedin.com/in"

    def __init__(self, username):
        self.username = username

# Import the str_to_bool utility in the utils.py module and use it in the
# function below, passing the `string` variable to str_to_bool function and
# return the resulting value.
def convert(string):
    from utils import str_to_bool

    return str_to_bool(string)