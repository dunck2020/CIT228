print('--------------------Exercise 5-8-----------------')
userNames = ['Admin', 'Larry', 'Candice', 'Amos', 'Sam']
for name in userNames:
    if name == 'Admin':
        print(f'Hello {name}, with Administrative rights you can view user reports.')
    else:
        print(f'Hello {name}, successful login, please choose what you would like to do.')
print('--------------------Exercise 5-9-----------------')
userNames = []
if userNames:
    print('We have active users.')
else:
    print('There are currently no users.')


