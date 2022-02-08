class Restaurant:
    """A simple restaurant class"""
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name} serves {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open for business')

    def set_number_served(self, actual_number_served):
        self.number_served = int(actual_number_served)

    def increment_number_served(self, daily_number_served):
        if int(daily_number_served) < 0:
            print('Number of patrons served must be a positive number')
        else:
            self.number_served += int(daily_number_served)

restaurant = Restaurant('The Sandwich Shoppe', 'Hot Sandwiches')
print('Initial number of customers served')
print(f'{restaurant.restaurant_name} has served {restaurant.number_served} customers')

restaurant.number_served = 43
print('\nNumber of customers served has been updated by attribute')
print(f'{restaurant.restaurant_name} has served {restaurant.number_served} customers')

restaurant.set_number_served(435)
print('\nNumber of customers served updated by method')
print(f'{restaurant.restaurant_name} has served {restaurant.number_served} customers')

restaurant.increment_number_served(199)
print('\nNumber of customers server has been incremented')
print(f'{restaurant.restaurant_name} has served {restaurant.number_served} customers')