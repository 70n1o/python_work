#class Dog:
#    """A simple attempt to model a dog."""
#
#    def __init__(self, name, age):
#        """initialize name and age attributes."""
#        self.name = name
#        self.age = age
#
#    def sit(self):
#        """simulate a dog sitting over in response to command."""
#        print(f"{self.name} is now sitting.")
#
#    def roll_over(self):
#        """simulate rolling over in response to a command."""
#        print(f"{self.name} rolled over!")
#
#my_dog = Dog('Sonko', 4)
#your_dog = Dog('Boss', 6)
#
#print(f"My dog's name is {my_dog.name}.")
#print(f"My dog is {my_dog.age} yrs old.")
#my_dog.sit()
#
#print(f"\nYour dog's name is {your_dog.name}.")
#print(f"Your dog is {your_dog.age} yrs old.")
#your_dog.sit()
#your_dog.roll_over()

"""prictice excer1."""
#class Restaurant:
#    """Simple restaurant class"""
#
#    def __init__(self, restaurant_name, cuisine_type):
#        """initialize restaurant name and cuisine type args."""
#        self.restaurant_name = restaurant_name
#        self.cuisine_type = cuisine_type
#
#    def describe_restaurant(self):
#        """describing restaurant."""
#        print(f"The restaurant is called {self.restaurant_name}.")
#        print(f"The cuisine type is {self.cuisine_type}.")
#
#    def open_restaurant(self):
#        """describes that restaurant is open"""
#        print(f"The restaurant {self.restaurant_name} is open.")
#
#restaurant = Restaurant('Winston', 'French')
#print(f"Restaurant name: {restaurant.restaurant_name}.")
#print(f"Restaurant cuisine: {restaurant.cuisine_type}.")
#restaurant.describe_restaurant()
#restaurant.open_restaurant()

#"""prictice excer2."""
#
#class Restaurant:
#    """Simple restaurant class"""
#
#    def __init__(self, restaurant_name, cuisine_type):
#        """initialize restaurant name and cuisine type args."""
#        self.restaurant_name = restaurant_name
#        self.cuisine_type = cuisine_type
#
#    def describe_restaurant(self):
#        """describing restaurant."""
#        print(f"The restaurant is called {self.restaurant_name}.")
#        print(f"The cuisine type is {self.cuisine_type}.")
#
#    def open_restaurant(self):
#        """describes that restaurant is open"""
#        print(f"The restaurant {self.restaurant_name} is open.")
#
#french_restaurant = Restaurant('Winston', 'French')
#italian_restaurant = Restaurant('Luigi', 'Italian')
#chinese_restaurant = Restaurant('Beijing temple', 'Chinese')
#
#
#french_restaurant.describe_restaurant()
#print("---")
#italian_restaurant.describe_restaurant()
#print("---")
#chinese_restaurant.describe_restaurant()
#print("Done!!!!")

"""Excer 3"""
#class User:
#    """Simple user class"""
#
#    def __init__(self, first_name, last_name, location, age):
#        """initialize the user class and attributes"""
#        self.first_name = first_name
#        self.last_name = last_name
#        self.location = location
#        self.age = age
#
#    def describe_user(self):
#        """describing user."""
#        print(f"The user's name is {self.first_name} {self.last_name}.")
#        print(f"The user is {self.age} yrs old and lives in {self.location}.")
#
#    def greet_user(self):
#        """greeting a user."""
#        print(f"Hello {self.first_name} {self.last_name}.")
#
#user_1 = User('Antonio', 'Hacker', 'Kisumu', 23)
#user_1.describe_user()
#user_1.greet_user()
#
#print("---")
#
#user_2 = User('Iano', 'Orina', 'Kayole', 22)
#user_2.describe_user()
#user_2.greet_user()

"""Working with classes and instances"""

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
#my_new_car = Car('audi', 'a4', 2019)
#print(my_new_car.get_descriptive_name())
#Modifying an Attribute’s Value Directly
#my_new_car.odometer_reading = 23
#my_new_car.read_odometer()

"""Modifying an Attribute’s Value Through a Method"""

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
#    #Incrementing an Attribute’s Value Through a Method
#    def increment_odometer(self, miles):
#        """Add the given amount to the odometer reading."""
#        self.odometer_reading += miles
#
#my_new_car = Car('audi', 'a4', 2019)
#print(my_new_car.get_descriptive_name())
#my_new_car.odometer_reading = 23
#my_new_car.read_odometer()
#
#my_new_car.update_odometer(23)
#my_new_car.read_odometer()
#
#my_used_car = Car('subaru', 'outback', 2015)
#print(my_used_car.get_descriptive_name())
#
#my_used_car.update_odometer(23_500)
#my_used_car.read_odometer()
#
#my_used_car.increment_odometer(100)
#my_used_car.read_odometer()#

"""Excer 1"""

#class Restaurant:
#    """Simple restaurant class"""
#
#    def __init__(self, restaurant_name, cuisine_type):
#        """initialize restaurant name and cuisine type args."""
#        self.restaurant_name = restaurant_name
#        self.cuisine_type = cuisine_type
#        self.number_served = 0
#
#    def describe_restaurant(self):
#        """describing restaurant."""
#        print(f"The restaurant is called {self.restaurant_name}.")
#        print(f"The cuisine type is {self.cuisine_type}.")
#
#    def open_restaurant(self):
#        """describes that restaurant is open"""
#        print(f"The restaurant {self.restaurant_name} is open.")
#
#    def set_number_served(self, guests):
#        """set no of served customers to given value."""
#        self.number_served =  guests
#
#    def increment_number_served(self, increment):
#        """Add a given number to the number of served guests."""
#        self.number_served += increment
#
#restaurant = Restaurant('Kempinski', 'Indian')
#print(f"Number served: {restaurant.number_served}")
#
#restaurant.number_served = 200
#print(f"Number served: {restaurant.number_served}")
#
#restaurant.set_number_served(300)
#print(f"Number served: {restaurant.number_served}")
#
#restaurant.increment_number_served(100)
#print(f"Number served: {restaurant.number_served}")

"""Excer 2"""

#class User:
#    """Simple user class"""
#
#    def __init__(self, first_name, last_name, location, age):
#        """initialize the user class and attributes"""
#        self.first_name = first_name
#        self.last_name = last_name
#        self.location = location
#        self.age = age
#        self.login_attempt = 0
#
#    def describe_user(self):
#        """describing user."""
#        print(f"The user's name is {self.first_name} {self.last_name}.")
#        print(f"The user is {self.age} yrs old and lives in {self.location}.")
#
#    def greet_user(self):
#        """greeting a user."""
#        print(f"Hello {self.first_name} {self.last_name}.")
#
#    def increment_login_attempt(self):
#        """incrementing login attempts by 1."""
#        self.login_attempt += 1
#
#    def reset_login_attempt(self):
#        """resets attempt to zero."""
#        self.login_attempt = 0
#
#user_login = User('Antonio', 'Hacker', 'Kisumu', 23)
#user_login.increment_login_attempt()
#user_login.increment_login_attempt()
#user_login.increment_login_attempt()
#print(f"Login attempts: {user_login.login_attempt}")
#
#user_login.reset_login_attempt()
#print(f"Login attempts (after reset): {user_login.login_attempt}")

"""INHERITANCE"""

#class Car:
#    """A simple attempt to represent a car."""

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
#
#class Battery:
#    """A simple attempt to model a battery for an electric car."""
#
#    def __init__(self, battery_size=75):
#        """Initialize the battery's attributes."""
#        self.battery_size = battery_size
#
#    def describe_battery(self):
#        """Print a statement describing the battery size."""
#        print(f"This car has a {self.battery_size}-kWh battery.")
#
#
#    def get_range(self):
#        """Print a statement about the range this battery provides."""
#        if self.battery_size == 75:
#                range = 260
#        elif self.battery_size == 100:
#            range = 315
#        print(f"This car can go about {range} miles on a full charge.")
#
#class ElectricCar(Car):
#    """
#    Initialize attributes of the parent class
#    then initialize attributes specific to an Electric.
#    """
#
#    def __init__(self, make, model, year):
#        """Initialize attributes of the parent class."""
#        super().__init__(make, model, year)
#        self.battery = Battery()
#
#    def describe_battery(self):
#        """Print a statement describing the battery size."""
#        print(f"This car has a {self.battery_size}-kWh battery.")
#
#    def fill_gas_tank(self):
#        """Electric cars don't have gas tanks."""
#        print("This car doesn't need a gas tank!")
#
#my_tesla = ElectricCar('tesla', 'model s', 2019)
#print(my_tesla.get_descriptive_name())
#my_tesla.battery.describe_battery()
#my_tesla.battery.get_range()


"""Excer 1."""

#class Restaurant:
#    """Simple restaurant class"""
#
#    def __init__(self, restaurant_name, cuisine_type):
#        """initialize restaurant name and cuisine type args."""
#        self.restaurant_name = restaurant_name
#        self.cuisine_type = cuisine_type
#
#    def describe_restaurant(self):
#        """describing restaurant."""
#        print(f"The restaurant is called {self.restaurant_name}.")
#        print(f"The cuisine type is {self.cuisine_type}.")
#
#    def open_restaurant(self):
#        """describes that restaurant is open"""
#        print(f"The restaurant {self.restaurant_name} is open.")
#
#class IceCreamStand(Restaurant):
#    """A simple ice cream stand inheriting restaurant x-ters"""
#    def __init__(self, restaurant_name, cuisine_type, flavors):
#        """initialize ice cream stand."""
#        super().__init__(restaurant_name, cuisine_type)
#        self.flavors = flavors
#
#    def display_flavor(self):
#        """Display ice cream flavors."""
#        print(f"The flavors are:")
#        for flavor in self.flavors:
#            print(f"- {flavor}")
#
#ice_cream = IceCreamStand('ice cream parlor', 'ice cream', ['chocolate', 'banana'])
#ice_cream.display_flavor()

"""Excer 2."""

#class User:
#    """Simple user class"""
#
#    def __init__(self, first_name, last_name, location, age):
#        """initialize the user class and attributes"""
#        self.first_name = first_name
#        self.last_name = last_name
#        self.location = location
#        self.age = age
#
#    def describe_user(self):
#        print(f"The user's name is {self.first_name} {self.last_name}.")
#        print(f"The user is {self.age} yrs old and lives in {self.location}.")
#
#    def greet_user(self):
#        print(f"Hello {self.first_name} {self.last_name}.")
#
#class Privileges:
#    """a simple privilege class."""
#
#    def __init__(self, privileges):
#        """A simple privilege class."""
#        self.privileges = privileges
#
#    def show_privileges(self):
#        """admin privileges."""
#        print(f"Admin privileges are:")
#        for privilege in self.privileges:
#            print(f"- {privilege}")
#
#
#class Admin(User):
#    """a simple admin class."""
#
#    def __init__(self, first_name, last_name, location, age, privileges):
#        """initializing admin class."""
#        super().__init__(first_name, last_name, location, age)
#        self.privileges = Privileges(privileges)
#
#
#admin = Admin('Antonio', 'Hacker', 'Kisumu', 23, ['can add post', 'can delete post', 'can ban user'])
#admin.privileges.show_privileges()
#admin.greet_user()


"""Excer 3."""

#class Car:
#    """A simple attempt to represent a car."""
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
#
#class Battery:
#    """A simple attempt to model a battery for an electric car."""
#
#    def __init__(self, battery_size=75):
#        """Initialize the battery's attributes."""
#        self.battery_size = battery_size
#
#    def describe_battery(self):
#        """Print a statement describing the battery size."""
#        print(f"This car has a {self.battery_size}-kWh battery.")
#
#
#    def get_range(self):
#        """Print a statement about the range this battery provides."""
#        if self.battery_size == 75:
#                range = 260
#        elif self.battery_size == 150:
#            range = 315
#        print(f"This car can go about {range} miles on a full charge.")
#
#    def upgrade_battery(self):
#        """Check batt and set capacity to 100."""
#        if self.battery_size != 100:
#            self.battery_size = 150
#
#class ElectricCar(Car):
#    """
#    Initialize attributes of the parent class
#    then initialize attributes specific to an Electric.
#    """
#
#    def __init__(self, make, model, year):
#        """Initialize attributes of the parent class."""
#        super().__init__(make, model, year)
#        self.battery = Battery()
#
#my_tesla = ElectricCar('tesla', 'model s', 2019)
#my_tesla.battery.get_range()
#my_tesla.battery.upgrade_battery()
#my_tesla.battery.get_range()


