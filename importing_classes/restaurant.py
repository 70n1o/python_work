"""Excer1."""

class Restaurant:
    """Simple restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """initialize restaurant name and cuisine type args."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """describing restaurant."""
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        """describes that restaurant is open"""
        print(f"The restaurant {self.restaurant_name} is open.")

