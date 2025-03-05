#passing test

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Antoney Omondi' work?"""
        formatted_name = get_formatted_name('antoney', 'omondi')
        self.assertEqual(formatted_name, 'Antoney Omondi')

    """Adding New Tests by adding another method."""

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ =='__main__':
    unittest.main()