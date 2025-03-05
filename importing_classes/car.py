"""This files works as our module."""
"""Importing a Single Class."""
#
#class Car:
#    """A simple attempt to represent a car."""
#
#    def __init__(self, make, model, year):
#        """Initialize attributes to describe a car."""
#        self.make = make
#        self.model = model
#        self.year = year
#        self.odometer_reading = 0
#
#    def get_descriptive_name(self):
#        """Return a neatly formatted descriptive name."""
#        long_name = f"{self.year} {self.make} {self.model}"
#        return long_name.title()
#
#    def read_odometer(self):
#        """Print a statement showing the car's mileage."""
#        print(f"This car has {self.odometer_reading} miles on it.")
#
#    def update_odometer(self, mileage):
#        """
#        Set the odometer reading to the given value.
#        Reject the change if it attempts to roll the odometer back.
#        """
#        if mileage > self.odometer_reading:
#            self.odometer_reading = mileage
#        else:
#            print("You can't roll back an odometer!")
#
#    def increment_odometer(self, miles):
#        """Add the given amount to the odometer reading."""
#        self.odometer_reading += miles


"""Storing Multiple Classes in a Module"""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
                range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """
    Initialize attributes of the parent class
    then initialize attributes specific to an Electric.
    """

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

     
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


