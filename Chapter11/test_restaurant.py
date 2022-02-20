import unittest
from restaurant import Restaurant

class TestRestaurant(unittest.TestCase):
    """Unit Tests for the restaurant class """
    
    def setUp(self):
        restaurant_name = "Bob's Burgers"
        cuisine_type = "American"
        number_served = 150
        self.restaurant = Restaurant(restaurant_name, cuisine_type, number_served)

    def test_set_number_served(self):
        number_served = 230
        self.restaurant.set_number_served(number_served)
        self.assertEqual(self.restaurant.number_served, 230)

    def test_increment_number_served(self):
        increment_amount = 100
        self.restaurant.increment_number_served(increment_amount)
        self.assertEqual(self.restaurant.number_served, 250) 

if __name__ == '__main__':
    unittest.main()