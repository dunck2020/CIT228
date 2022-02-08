class Restaurant:
    """A simple restaurant class"""
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name} serves {self.cuisine_type}')
        
    def open_restaurant(self):
        print(f'{self.restaurant_name} is open for business')

restaurant = Restaurant('The Sandwich Shoppe', 'Hot Sandwiches')
print(f'Restaurant name: {restaurant.restaurant_name}')
print(f'Cuisine type: {restaurant.cuisine_type}')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant("Bob's Burgers", 'American Food')
restaurant1.describe_restaurant()
restaurant2 = Restaurant('El Azteco Taco', 'Mexican Food')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('Annie BBQ', 'The Best BBQ Around')
restaurant3.describe_restaurant()