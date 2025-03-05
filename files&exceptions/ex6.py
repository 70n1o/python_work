 
#num1 = input("Enter first number: ")
#num2 = input("Enter second number: ")
#
#try:
#    result = int(num1) + int(num2)
#    print(f"The result is: {result}")
#except ValueError:
#    print("Wrong value provided. Enter two numbers.")


#Ex7
# Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.

#rint("Give me two numbers, and I'll add them.")
#rint("Enter 'q' to quit.")

#hile True:
#   num1 = input("Enter first number: ")
#   if num1 == 'q':
#       break
#   num2 = input("Enter second number: ")
#   if num2 == 'q':
#       break

#   try:
#       result = int(num1) + int(num2)
#       print(f"The result is: {result}")
#   except ValueError:
#       #print("Wrong value provided. Enter two numbers.")
#       pass


#Ex8

#filename1 = 'cats.txt'
#filename2 = 'dog.txt'
#
#print("Cats: ")
#try:
#    with open(filename1, encoding='utf-8') as f:
#        contents = f.read()
#except FileNotFoundError:
#    print(f"Sorry, the file {filename1} does not exist.")
#else:
#    print(contents)
#
#print("Dogs: ")
#try:
#    with open(filename2, encoding='utf-8') as f:
#        contents = f.read()
#except FileNotFoundError:
#    print(f"Sorry, the file {filename2} does not exist.")
#    #pass
#else:
#    print(contents)


#Ex9

#filename = 'little_women.txt'
#
#with open(filename, encoding='utf-8') as f:
#    contents = f.read()
#
#print(contents.lower().count('the'))
#print(contents.lower().count('the '))


#Ex11

#import json
#
#filename  = 'favourite_number.json'
#
#favorite_number = input("What is your favorite number? ")
#
#with open(filename, 'w') as f:
#    json.dump(favorite_number, f)


#Loading the code above

#import json
#
#filename = 'favourite_number.json'
#
#with open(filename) as f:
#    favorite_number = json.load(f)
#
#print(f"I know your fav number! It's {favorite_number}")


#Ex12

#import json
#
#filename = 'favorite_number.json'
#
#try:
#    with open(filename) as f:
#        favorite_number = json.load(f)
#except FileNotFoundError:
#    favorite_number = input("What is your favorite number? ")
#    with open(filename, 'w') as f:
#        json.dump(favorite_number, f)
#        print(f"I know your fav no! It's {favorite_number}.")
#
#else:
#    print(f"I know your fav number! It's {favorite_number}.")


#Ex13

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
        answer = input(f"Hello, is this correct username: {username} (y/n)? ")
        if answer.lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}.")

    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()