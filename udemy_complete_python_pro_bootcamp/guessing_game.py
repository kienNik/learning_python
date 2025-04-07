'''
rules:
- guess from 1-100
- 2 levels: easy (10 attemps), hard (5 attemps)
'''


from random import randint

def guessing_game():
    answer = randint(1, 100)
    attemps = 0
    level = input('Choose a level. easy or hard: ')
    if level == 'easy':
        attemps = 10
    elif level == 'hard':
        attemps = 5

    guess = 0
    for i in range(attemps):
        print(f'You have {attemps - i} attempts left')
        guess = int(input('Guess a number: '))
        if guess > answer:
            print('Lower')
        elif guess < answer:
            print('Higher')
        else:
            print('Bingo')
            return
    print('Lose')

while input('New game? y or n: ') == 'y':
    print('\n')
    guessing_game()