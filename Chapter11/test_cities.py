import unittest
from city_functions import format_city_country

class CitiesTestCase(unittest.TestCase):
    """Tests format_city_country"""

    def test_city_country(self):
        """Does 'Santiago' and 'Chile' work?"""
        formatted_city_country = format_city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does 'Santiago' and 'Chile' and '15000' work?"""
        formatted_city_country_pop = format_city_country('santiago', 'chile', '15000')
        self.assertEqual(formatted_city_country_pop, 'Santiago, Chile Population 15000')


if __name__ == '__main__':
    unittest.main()


    