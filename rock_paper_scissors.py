print('...ROCK...\n...PAPER...\n...SCISSORS...')
first_player = input('Make your choice. Rock, paper or scissors... ')
second_player = input('Your turn. Make your choice. Rock, paper or scissors... ')

if first_player == 'rock':
    if second_player == 'paper':
        print('Second_player win!!!')
    else:
        print('First_player win!!!')
elif first_player == 'paper':
    if second_player == 'rock':
        print('First_player win!!!')
    else:
        print('Second_player win!!!')
elif first_player == 'scissors':
    if second_player == 'rock':
        print('Second_player win!!!')
    else:
        print('First_player win!!!')
