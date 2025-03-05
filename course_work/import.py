#import functions
#"""importing entire module"""
#functions.make_pizza(16, 'pepperoni')
#functions.make_pizza(2, 'mushroom', 'green flav', 'cheese')

#importing specific function from a module
#from functions import make_pizza

#make_pizza(16, 'pepperoni')
#make_pizza(2, 'mushroom', 'green flav', 'cheese')

#importing entire module with an alias
#from functions import make_pizza as mp
#
#mp(16, 'pepperoni')
#mp(2, 'mushroom', 'green flav', 'cheese')

#importing all functions from a specific module
#from functions import *
#make_pizza(17, 'pepperoni')
#make_pizza(11, 'mushroom', 'greenpaper', 'cheese')

import functions

unprinted_designs=['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

functions.print_models(unprinted_designs, completed_models)
functions.show_completed_models(completed_models)