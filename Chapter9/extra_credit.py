from random import randint
from random import choice

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        player_roll = randint(1,self.sides)
        print(f'Player has rolled a {player_roll}')

    def roll_ten_times(self):
        ten_times = 0
        while ten_times < 10:
            player_roll = randint(1,self.sides)
            print(f'Player has rolled a {player_roll}')
            ten_times +=1

print('Now rolling the 6 sided dice 10 times')
dice_game_six_sides = Dice(6)
dice_game_six_sides.roll_ten_times()

print('\nNow rolling the 10 sided dice 10 times')
dice_game_ten_sides = Dice(10)
dice_game_ten_sides.roll_ten_times()

print('\nNow rolling the 20 sided dice 10 times')
dice_game_twenty_sides = Dice(20)
dice_game_twenty_sides.roll_ten_times()

print('\nNow you can create your own game')
number_of_sides = int(input('How many sides does your dice have?'))
rolls_total = int(input('How many times would you like to roll the dice?'))
dice_game = Dice(number_of_sides)
counter = 0
while counter < rolls_total:
    dice_game.roll_dice()
    counter += 1
print('Thanks for playing!')