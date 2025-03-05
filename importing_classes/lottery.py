#Excer2

from random import choice

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

print("The following tickets have won a price")
for x in range(0, 4):
    print(choice(values))

