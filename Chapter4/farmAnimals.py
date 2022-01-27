animals = ['cow', 'pig', 'goat', 'horse', 'chicken', 'dog']
moreAnimals = animals[:]
moreAnimals.append('barn cat')
moreAnimals.append('pigeon')
moreAnimals.append('sheep')
moreAnimals.append('turkey')
print('--------------Original List--------------')
for animal in animals:
    print(animal)
print('--------------New List--------------')
for animal in moreAnimals:
    print(animal)
print('--------------Exercise 4-10--------------')
print(f'The first 3 items in the list are:{moreAnimals[:3]}')
print(f'The middle 4 items in the list are:{moreAnimals[3:7]}')
print(f'The last 3 items in the list are:{moreAnimals[7:]}')