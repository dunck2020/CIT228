number = input('Please enter a number and I will tell you if it is a multiple of 10:')
number = int(number)
if number % 10 == 0 and number != 0:
    print(f'The number {number} is a muliplte of 10')
else:
    print(f'The number {number} is not a muliplte of 10')