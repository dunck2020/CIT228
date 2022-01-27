print('-------------------------Hands on #2-----------------------\n')
import random
randomNumber = random.randrange(10,100)
listOfNumbers = list(range(randomNumber))
print(listOfNumbers)
print(f'The largest number = {max(listOfNumbers)}')
print(f'The smallest number = {min(listOfNumbers)}')
print(f'The total of all the numbers = {sum(listOfNumbers)}')
print(f'The average number = {sum(listOfNumbers) / len(listOfNumbers)}\n')