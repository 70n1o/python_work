"""Importing a Single Class."""
#Importing a Module into a Module

#from car import Car
#
#my_new_car = Car('audi', 'a4', 2017)
#print(my_new_car.get_descriptive_name())
#
#my_new_car.odometer_reading = 23
#my_new_car.read_odometer()


"""
Importing All Classes from a Module.
this is the recommended method
"""

#import car
#
#my_bettle = car.Car('bmw', 'm4', 2023)
#print(my_bettle.get_descriptive_name())
#
#my_tesla = car.Car('benz', 'g-class', 2022)
#print(my_tesla.get_descriptive_name())


"""
Importing All Classes from a Module.
this method not recommended bcoz it will cause errors
"""

#from car import *

#Using Aliases

from car import ElectricCar as EC

my_bettle = EC('bmw', 'm4', 2023)
print(my_bettle.get_descriptive_name())

my_tesla = EC('benz', 'g-class', 2022)
print(my_tesla.get_descriptive_name())

