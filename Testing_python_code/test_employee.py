import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for class Employee.""" 

    def setUp(self):
        """Creat an employee entry with a first name, last name and salary for use in all test methods."""
        first_name = 'John'
        last_name = 'Doe'
        self.salary = 50000
        self.employee = Employee(first_name, last_name, self.salary)

    def test_give_default_raise(self):
        """test that default raise works properly."""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, self.salary + 5000)

    def test_give_custom_raise(self):
        """Test that custom raise works properly."""
        custom_raise = 10000
        self.employee.give_raise(custom_raise)
        self.assertEqual(self.employee.salary, self.salary + custom_raise)

if __name__ == '__main__':
    unittest.main()     