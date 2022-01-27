car = 'audi'
number1 = 7
number2 = 45
color = 'Red'
food = ['taco', 'burger','bacon','sandwich']

print('---------------------True Results-----------------')
print(number1, '<', number2, number1 < number2)
print(number1, '<=', number2, number1 <= number2)
print('Is car == "audi": ', car == 'audi')
print(f'Is burger in the food list?', 'burger'in food)
print('Is the color Red in title case?', color == 'Red')
print(color, '== Red', color == 'Red')
print('red == red', color.lower() == 'red')
print(number1, '!=', number2, number1 != number2)
print('Is the color = Red and number1 = 7', color == 'Red' and number1 == 7)
print('Is the color = Blue or number1 = 7', color == 'Blue' or number1 == 7)
print(f'Is taco in the food list?', 'taco'in food)
print(f'Is burrito not in the food list?', 'burrito'not in food)

print('---------------------False Results-----------------')
print(number1, '>', number2, number1 > number2)
print(number1, '>=', number2, number1 >= number2)
print('Is car != "audi": ', car != 'audi')
print(f'Is watermelon in the food list?', 'watermelon'in food)
print('Is the chosen color Red in uppercase?', color == 'RED')
print(color, '!= Red', color != 'Red')
print('RED == red', color.lower() == 'RED')
print(number1, '==', number2, number1 == number2)
print('Is the color = Blue and number1 = 7', color == 'Blue' and number1 == 7)
print('Is the color = Blue or number1 = 41', color == 'Blue' or number1 == 41)
print(f'Is burrito in the food list?', 'burrito'in food)
print(f'Is taco not in the food list?', 'taco'not in food)