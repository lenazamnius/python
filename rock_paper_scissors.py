print('...ROCK...\n...PAPER...\n...SCISSORS...')
first_player = input('Make your choice. Rock, paper or scissors... ')
second_player = input('Your turn. Make your choice. Rock, paper or scissors... ')

choice = ['rock', 'paper', 'scissors']

if (first_player in choice) and (second_player in choice):
    if first_player == second_player:
        print("It's a tie!")
    else:
        if first_player == choice[1]:
            if second_player == choice[2]:
                print('Second player win!!!')
            else:
                print('First player win!!!')
        elif first_player == choice[2]:
            if second_player == choice[1]:
                print('First player win!!!')
            else:
                print('Second player win!!!')
        elif first_player == choice[3]:
            if second_player == choice[1]:
                print('Second player win!!!')
            else:
                print('First player win!!!')
else:
    print('Chose only between rock, paper or scissors, please)')
