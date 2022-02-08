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
        self.number_served = actual_number_served

    def increment_number_served(self, daily_number_served):
        if daily_number_served < 0:
            print('Number of patrons served must be a positive number')
        else:
            self.number_served += daily_number_served

class IceCreamStand(Restaurant):
    """Ice cream stand is a specific type of restaurant"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print('We carry the following flavors of ice cream:')
        for flavor in self.flavors:
            print(f'\t-{flavor.title()}')

ice_cream_shop = IceCreamStand('Moomers', 'Ice Cream', ['chocolate', 'caramel sea salt', 'moose tracks', 'heath bar crunch', 'vanilla', 'raspberry sorbet'])
ice_cream_shop.display_flavors()
