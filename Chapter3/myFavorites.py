favoriteFoods = ['tacos', 'burgers', 'steak', 'spaghetti', 'salad', 'soup']
favoriteNumbers = [1, 7, 44, 2008, 2006, 13]
favoriteMovies=['Jaws', 'Alien', 'A Quiet Place']
comboList = [favoriteFoods[0], favoriteFoods[1], favoriteNumbers[0], favoriteNumbers[1], favoriteMovies[0], favoriteMovies[1]]

print('-----------------------Hands on 1----------------------')
print('Favorite foods:', favoriteFoods)
print('Favorite numbers:', favoriteNumbers)
print('Favorite movies:', favoriteMovies)
print('Combo List:', comboList)
print('Last item in food list:', favoriteFoods[-1])
print('2nd, 4th and 6th numbers:', favoriteNumbers[1], favoriteNumbers[3],favoriteNumbers[5])
print('All movies:', favoriteMovies[0], favoriteMovies[1], favoriteMovies[2])
print('First food, first number and first movie in list:', favoriteFoods[0], favoriteNumbers[0], favoriteMovies[0])

print('-----------------------Hands on 2----------------------')
favoriteMovies.append('Good Fellas')
print('Added movie to list:',favoriteMovies)
favoriteNumbers.insert(3, 199)
print('Added number to sub 3:', favoriteNumbers)
favoriteFoods.insert(5, 'bacon')
print('Added food at sub 5:', favoriteFoods)
del favoriteFoods[-1]
print('Deleted "Soup" at sub -1:', favoriteFoods)
favoriteNumbers.pop()
print('Deleted last number from numbers list:', favoriteNumbers)
favoriteNumbers.pop(2)
print('Deleted number st sub 2:', favoriteNumbers)

print('-----------------------Hands on 3----------------------')
favoriteMovies.sort()
print('Sorted movie list:', favoriteMovies)
favoriteFoods.sort()
print('Sorted food list:', favoriteFoods)
print('Temp sorted list:', sorted(favoriteNumbers))
print('Unsorted number list:', favoriteNumbers)
favoriteMovies.reverse()
print('Movie list sorted in reverse:', favoriteMovies)
