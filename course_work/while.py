#current_no = 1
#while current_no <= 5:
#    print(current_no)
#    current_no += 1

#prompt ="\nTell me something and I will repeat it back: "
#prompt += "\nEnter 'quit' to end the program "
#message = ""
#
#while message != 'quit':
#    message = input(prompt)
#    print(message)

#using flag active instead
"""prompt ="\nTell me something and I will repeat it back: "
prompt += "\nEnter 'quit' to end the program "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
"""

#prompt ="\nPlz enter the name of the city u like: "
#prompt += "\n(Enter 'quit' when u finish) "
#
#while True:
#    city = input(prompt)
#    if city == 'quit':
#        break
#    else:
#        print(f"I'd love to go to {city.title()}!")

#current_no = 0
#while current_no < 10:
#    current_no += 1
#    if current_no % 2 == 0:
#        continue
#    print(current_no)

#unconfirmed_users = ['alice', 'bob', 'antonio']
#confirmed_users = []
#
#while unconfirmed_users:
#    current_user = unconfirmed_users.pop()
#
#    print(f"verifying user: {current_user.title()}")
#    confirmed_users.append(current_user)
#
#print("\nThe following have been verified: ")
#for confirmed_user in confirmed_users:
#    print(confirmed_user.title())

pets = ['dog', 'cat', 'rabbit', 'cat', 'squrel', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

