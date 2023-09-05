import random


def guess(x):
    random_number = random.randint(1, x)
    estimate = 0
    while estimate != random_number:
        estimate = int(input(f'guess a number between 1 and {x}: '))
        if estimate < random_number:
            print('Sorry, guess again. Too low.')
        elif estimate > random_number:
            print('Sorry, guess again. Too high.')
        if estimate == random_number:
            print(f'yay, congrats. You have guessed the number {random_number} correctly!!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            scope = random.randint(low, high)
        else:
            scope = low
        feedback = input(f'is {scope} too high (H), too low (L), or correct (C) ')
        if feedback == 'h':
            high = scope - 1
        if feedback == 'l':
            low = scope + 1
    print(f'The Computer guessed you number, {guess} correctly')


guess(10)
