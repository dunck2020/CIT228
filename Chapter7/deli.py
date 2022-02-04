from os import remove


sandwich_orders = ['pastrami', 'ham and swiss', 'pastrami', 'italian', 'cuban', 'pastrami', 'philly', 'tuna', 'pastrami', 'reuben']
finished_orders = []
print('\n------Try it yourself 7-8-------')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'Currently making a {sandwich.title()} sandwich...')
    finished_orders.append(sandwich.title())

print('\nThe following sandwiches have been made:')
for sandwich in finished_orders:
    print(sandwich)

print('\n------Try it yourself 7-9-------')
sandwich_orders = ['pastrami', 'ham and swiss', 'pastrami', 'italian', 'cuban', 'pastrami', 'philly', 'tuna', 'pastrami', 'reuben']
finished_orders = []
print("I'm sorry we are out of pastrami today")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'Currently making a {sandwich.title()} sandwich...')
    finished_orders.append(sandwich.title())

print('\nThe following sandwiches have been made:')
for sandwich in finished_orders:
    print(sandwich)