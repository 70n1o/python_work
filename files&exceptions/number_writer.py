"""Storing Data"""

"""Here’s how you can use json.dump() to store a list of numbers:"""

#import json
#
#numbers = [2, 3, 5, 7, 11, 13]
#
#filename = 'numbers.json'
#
#with open(filename, 'w') as f:
#    json.dump(numbers, f)


# a program that uses json.load() to read the list back into memory:

#import json
#
#filename = 'numbers.json'
#with open(filename) as f:
#    numbers = json.load(f)
#print(numbers)


"""Saving and Reading User-Generated Data"""
#sample1

#import json
#
#username = input("What is your name? ")
#
#filename = 'username.json'
#with open(filename, 'w') as f:
#    json.dump(username, f)
#    print(f"We'll remember you when you come back, {username}!")

#sample2
# a new program that greets a user whose name has already been stored:

#import json
#
#filename = 'username.json'
#with open(filename) as f:
#    username = json.load(f)
#    print(f"Welcome back {username}!")

#We need to combine these two above programs into one file

#import json
#
## Load the username, if it has been stored previously.
## Otherwise, prompt for the username and store it.
#
#filename = 'username.json'
#try:
#    with open(filename) as f:
#        username = json.load(f)
#except FileNotFoundError:
#    username = input("What is your name? ")
#    with open(filename, 'w') as f:
#        json.dump(username, f)
#        print(f"We'll remember you when you come back, {username}!")
#else:
#    print(f"Welcome back, {username}!")


#Refactoring makes your code cleaner, easier to understand, and easier to extend.

#import json
#
#def greet_user():
#    """Greet the user by name."""
#    filename = 'username.json'
#    try:
#        with open(filename) as f:
#            username = json.load(f)
#    except FileNotFoundError:
#        username = input("What is your name? ")
#        with open(filename, 'w') as f:
#            json.dump(username, f)
#            print(f"We'll remember you when you come back, {username}!")
#    else:
#        print(f"Welcome back, {username}!")
#
#greet_user()


#Let’s refactor greet_user() so it’s not doing so many different tasks.

#import json
#
#def get_stored_username():
#    """Get stored username if available."""
#    filename = 'username.json'
#    try:
#        with open(filename) as f:
#            username = json.load(f)
#    except FileNotFoundError:
#        return None
#    else:
#        return username
#
#def greet_user():
#    """Greet the user by name."""
#    username = get_stored_username()
#    if username:
#        print(f"Welcome back, {username}!")
#    else:
#        username = input("What is your name? ")
#        filename = 'username.json'
#        with open(filename, 'w') as f:
#            json.dump(username, f)
#            print(f"We'll remember you when you come back, {username}!")
#greet_user()



import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()