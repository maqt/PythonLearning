# This program is used to test loops and if/else statements
# with number guessing game

import random

guess = 0
count = 0
print('Welcome to the guessing game!')
number = random.randint(1,20)
while(guess<1):
    count+=1
    myGuess = int(input('guess a number between 1 - 20\n')) 
    if myGuess > number:
        print('The number is smaller than ' + str(myGuess))
    elif myGuess < number:
        print('The number is greater than ' + str(myGuess))
    else:
        print('ding ding ding')
        guess = guess + 1
print('It took you ' + str(count) + ' attempts')
