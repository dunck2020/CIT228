from re import T


def addition(n1, n2):
    return n1 + n2

letter_entered = True
quit = ''
while letter_entered != False or quit != 'no': 
    try:
        first_number = int(input('Please enter the first number to add:'))
        second_number = int(input('Please enter the second number to add:'))
    except ValueError:
        print('You entered a letter and not a number please try again.\n')
        letter_entered = True
    else:
        answer = addition(first_number, second_number)
        print(f'The answer of {first_number} + {second_number} = {answer}')
        letter_entered = False
        quit = input('Would you like to add two more numbers? (enter "yes" or "no")')

