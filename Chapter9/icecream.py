from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Ice cream stand is a specific type of restaurant"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print('We carry the following flavors of ice cream:')
        for flavor in self.flavors:
            print(f'\t-{flavor.title()}')