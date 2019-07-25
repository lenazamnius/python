import random

print('...ROCK...\n...PAPER...\n...SCISSORS...')
first_player = input('Make your choice. Rock, paper or scissors... ').lower()
choice = ['rock', 'paper', 'scissors']
random_num = random.randint(0, 2)
second_player = choice[random_num]
print(f'Second player chose {second_player}')

if (first_player in choice) and (second_player in choice):
    if first_player == second_player:
        print("It's a tie!")
    else:
        if first_player == choice[0]:
            if second_player == choice[1]:
                print('Second player win!!!')
            else:
                print('You win!!!')
        elif first_player == choice[1]:
            if second_player == choice[0]:
                print('You win!!!')
            else:
                print('Second player win!!!')
        elif first_player == choice[2]:
            if second_player == choice[0]:
                print('Second player win!!!')
            else:
                print('You win!!!')
else:
    print('Choose only between rock, paper or scissors, please)')
