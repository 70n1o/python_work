#Exer1
"""importing random values using python std library"""

from random import randint

class Die:
    """creating a simple die class"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


die = Die(23)
for x in range(0, 10):
    die.roll_die()

