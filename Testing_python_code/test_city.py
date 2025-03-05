import unittest
from city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do city, country pairs like 'nairobi', 'kenya' works?"""
        formatted_city_country = get_city_country('nairobi', 'kenya')
        self.assertEqual(formatted_city_country, 'Nairobi, Kenya')

    def test_city_country_population(self):
        """Test that optional ppltion argmnt works properly."""
        formatted_input = get_city_country('nairobi', 'kenya', 1000002)
        self.assertEqual(formatted_input, 'Nairobi, Kenya - Population 1000002')        

if __name__ == '__main__':
    unittest.main()
