#def greet_user(username):
#    """Display a simple greeting."""
#    print(f"Hello, {username.title()}!")
#greet_user('Anto')


#positinal arguments

#def describe_pet(animal_type, pet_name):
#    """Display info about a pet"""
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}.")
#describe_pet('hamster', 'harry')

#def describe_pet(pet_name, animal_type='dog'):
#    """Display info about a pet"""
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}.")
#describe_pet('Sonko')
#describe_pet(pet_name='Sonko')
#describe_pet('Sonko', 'hamster')
#describe_pet(pet_name='Sonko', animal_type='hamster')
#describe_pet(animal_type='hamster', pet_name='Sonko')

#def get_format_name(first_name, last_name):
#    """Full format names"""
#    full_name = f"{first_name} {last_name}"
#    return full_name.title()
#    
#musician = get_format_name('anto', 'gucci')
#print(musician)

#function in dictinary
#def build_person(f_name, l_name, age=None):
#    """Return dict of person's info"""
#    person = {'first': f_name, 'last': l_name}
#    if age:
#        person['age'] = age
#    return person
#
#musician = build_person('antonio', 'gucci', age=23)
#print(musician)

#def get_formatted_name(f_name, l_name):
#    """Return formatted names."""
#    full_name = f"{f_name} {l_name}"
#    return full_name.title()
#
#while True:
#    print("\nPlz tell me your name: ")
#    print("(Enter 'q' to quit)")
#    first_name = input("Firts name: ")
#    if first_name == 'q':
#        break
#
#    last_name = input("Last name: ")
#    if last_name =='q':
#        break
#
#    formatted_names = get_formatted_name( first_name, last_name)
#    print(f"\nHello, {formatted_names}!")

#functions to store info in a dictonary
#def make_album(artist, title, songs=None):
#    """Return album dictionary"""
#    album = {'artist': artist, 'title': title, 'songs': songs}
#    return album
#
#print(make_album("Michael Jackson", "Thriller"))
#print(make_album("The Beatles", "Let It Be", 12))

#def make_album(artist, title, songs=None):
#    """Return album dictionary"""
#    album = {'artist': artist, 'title': title, 'songs': songs}
#    return album

#while True:
#    print("\nEnter album information.")
#    print("(Enter 'q' at any time to quit)")
#
#    artist = input("Artist name: ")
#    if artist == 'q':
#        break
#
#    title = input("Title name: ")
#    if title =='q':
#        break
#
#    song = input("Song number (optional): ")
#    if song =='q':
#        break
#
#    album = make_album(artist, title, song)
#    print(album)

#passing a list

#def greet_user(names):
#    """Print a simple greetiing to users"""
#    for name in names:
#        msg = f"Hello, {name.title()}!"
#        print(msg)
#
#usernames = ['hannety', 'prince', 'jibril']
#greet_user(usernames)


def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed""" 
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahendron']
completed_models =[]
"""not to modify the original list, use a copy instead use this  
sclice notation to pass a copy to a function
rather than passing original list to it[:]"""
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)

#def make_pizza(size, *toppings):
#    """summarize the pizza we are abt to make"""
#    print(f"\nMaking a {size}-inch pizza with the following toppings:")
#    for topping in toppings:
#        print(f"- {topping}")
#
#make_pizza(13, 'Pepperoni')
#make_pizza(43, 'mushroom', 'green paper', 'extra cheese')

#def build_profile(first, last, **user_info):
#    """build a dict containing everything we know abt a user"""
#    user_info['first_name'] = first
#    user_info['last_name'] = last
#    return user_info
#
#user_profile = build_profile('albert', 'eistein', location='nairobi', field='physics')
#print(user_profile)

#def sandwich_ingrid(*args):
#    """Sandwich ordered"""
#    print("\nThese  are the sandwich ingridients:")
#    for arg in args:
#        print(f"- {arg}")
#
#sandwich_ingrid()
#sandwich_ingrid('salad', 'cucumber', 'chicken')
#sandwich_ingrid('salad', 'cucumber', 'chicken', 'pastrami', 'tuna')

#def make_pizza(size, *toppings):
#    """summarize the pizza we are abt to make"""
#    print(f"\nMaking a {size}-inch pizza with the following toppings:")
#    for topping in toppings:
#        print(f"- {topping}")
