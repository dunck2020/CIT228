print('-----------------------Exercise 3-10----------------------')
print('Use of f-string, append, insert, del, pop, remove, sorted, reverse, sort, len')
learningGuide = ['HTML', 'CSS', 'JavaScript', 'Python', 'C#', 'SQL', 'ReactJS', 'NodeJS', 'VueJS', 'Quasar']
print('Here is the list of items:',learningGuide)
# f-string and len
print(f'There are a total of {len(learningGuide)} things to learn for web applications.')
# append
learningGuide.append('Angular')
print(f'I added something new so there are now {len(learningGuide)} things to learn')
print('Here is the new list:', learningGuide)
# insert
learningGuide.insert(0, 'VS Code')
print(f'First you must understand how to use {learningGuide[0]}')
# pop
print(f'I guess you do not need to learn {learningGuide.pop(-2)}, I will remove the item')
print('Here is the new list:', learningGuide)
# remove
learningGuide.remove('VueJS')
print(f'Vue is really another framework you can learn later, so {learningGuide} is what you should learn')
# sorted
print(f'Here is the temp sorted list {sorted(learningGuide)}')
# sort
learningGuide.sort()
print(f'Here is the permanent sorted list alphabetical order {learningGuide}')
# reverse
learningGuide.reverse()
print(f'Here is the list in reverse{learningGuide}')
# del
del learningGuide[-1]
print(f'Angular is not really something you must know either here is a new list {learningGuide}')
