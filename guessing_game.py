from random import randint


rand_num = randint(1, 8)
while True:
    guess = input('Guess a number between 1 and 8 -> ')
    guess = int(guess)

    if guess > rand_num:
        print('Too high, try again')
    elif guess < rand_num:
        print('Too low, try again')
    else:
        print('You got it. You won!')
        repeat_game = input('Do you want to keep playing? (y/n) -> ')
        if repeat_game == 'y':
            rand_num = randint(1, 8)
            guess = guess
        elif repeat_game == 'n':
            print('Thanks for playing. Bye)')
            break
