guestList=['Isaac Newton', 'Albert Einstein', 'Stephen Hawking']
invite = ', can you make it to dinner this Saturday?'
cancelled = 'sorry, I have to cancel Saturday, maybe next week?'

print('-----------------------Exercise 3-4----------------------')
print(guestList[0],invite)
print(guestList[1],invite)
print(guestList[2],invite)

print('-----------------------Exercise 3-5----------------------')
print(guestList[0], 'cannot make it to dinner.')
del guestList[0]
guestList.append('Galileo Galilei')
print(guestList[0],invite)
print(guestList[1],invite)
print(guestList[2],invite)

print('-----------------------Exercise 3-6----------------------')
guestList.insert(0, 'Nikola Tesla')
guestList.insert(2, 'Archimedes')
guestList.append('Neil deGrasse Tyson')
print('We have room for more guests!!')
print(f'I have a total of {len(guestList)} guests coming for dinner.')
print(guestList[0],invite)
print(guestList[1],invite)
print(guestList[2],invite)
print(guestList[3],invite)
print(guestList[4],invite)
print(guestList[5],invite)

print('-----------------------Exercise 3-7----------------------')
print('I am sorry the seating has changed again, I can only invite 2, so sorry...')
print(guestList.pop(), cancelled)
print(guestList.pop(), cancelled)
print(guestList.pop(), cancelled)
print(guestList.pop(), cancelled)
print(guestList[0], invite)
print(guestList[1], invite)
del guestList[0]
del guestList[0]
print('Revised guest list:',guestList)