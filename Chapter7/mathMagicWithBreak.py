import random
print('Today you will be tested with 10 math problems.')
counter = 0
numberCorrect = 0
numberIncorrect = 0
while counter < 10:
    randomNum1 = random.randrange(1,1000)
    randomNum2 = random.randrange(1,1000)
    correctAnswer = randomNum1 + randomNum2
    userAnswer = int(input(f'What is {randomNum1} + {randomNum2}? '))
    if correctAnswer == userAnswer:
        print('Correct! Great job!')
        numberCorrect += 1
    else:
        print(f'Wrong answer, the correct answer is {correctAnswer} better luck next time...')
        numberIncorrect += 1
        if numberIncorrect > 5:
            print('Please get some help from a tutor, you have answered the max number allowed incorrectly')
            break
    counter += 1 
print(f'You answered {numberCorrect} out of {counter} problems correct')
if numberCorrect == counter:
    print('You answered them all correctly! Great job!')
print('Thank you for playing the math game!')