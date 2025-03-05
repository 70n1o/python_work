"""Excer2."""

class User:
    """Simple user class"""

    def __init__(self, first_name, last_name, location, age):
        """initialize the user class and attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age

    def describe_user(self):
        print(f"The user's name is {self.first_name} {self.last_name}.")
        print(f"The user is {self.age} yrs old and lives in {self.location}.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}.")

class Privileges:
    """a simple privilege class."""

    def __init__(self, privileges):
        """A simple privilege class."""
        self.privileges = privileges

    def show_privileges(self):
        """admin privileges."""
        print(f"Admin privileges are:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """a simple admin class."""

    def __init__(self, first_name, last_name, location, age, privileges):
        """initializing admin class."""
        super().__init__(first_name, last_name, location, age)
        self.privileges = Privileges(privileges)