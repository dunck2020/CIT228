import random
problems = int(input('How many math problems would you like to practice today? '))
counter = 0
numberCorrect = 0
while counter < problems:
    randomNum1 = random.randrange(1,1000)
    randomNum2 = random.randrange(1,1000)
    correctAnswer = randomNum1 + randomNum2
    userAnswer = int(input(f'What is {randomNum1} + {randomNum2}? '))
    if correctAnswer == userAnswer:
        print('Correct! Great job!')
        numberCorrect += 1
    else:
        print(f'Wrong answer, the correct answer is {correctAnswer} better luck next time...')
    counter += 1 
print(f'You answered {numberCorrect} out of {counter} problems correct')
if numberCorrect == counter:
    print('You answered them all correctly! Great job!')
print('Thank you for playing the math game!')