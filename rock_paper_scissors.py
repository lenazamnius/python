from random import randint


choice = ['rock', 'paper', 'scissors']
human_score = 0
computer_score = 0
count = 1
while True:
    print(f'Score between human and computer is {human_score}:{computer_score}\n')
    print(f'Round {count}')
    print('...ROCK...\n...PAPER...\n...SCISSORS...')
    human = input('Make your choice human being. Rock, paper or scissors... ').lower()
    computer = choice[randint(0, 2)]
    print(f'Computer picked {computer}')

    if human == computer:
        print("It's a tie!")
    else:
        if human == choice[0]:
            if computer == choice[1]:
                print('Computer succeed!!!')
                computer_score += 1
            else:
                print('Human succeed!!!')
                human_score += 1
        elif human == choice[1]:
            if computer == choice[0]:
                print('Human succeed!!!')
                human_score += 1
            else:
                print('Computer succeed!!!')
                computer_score += 1
        elif human == choice[2]:
            if computer == choice[0]:
                print('Computer succeed!!!')
                computer_score += 1
            else:
                print('Human succeed!!!')
                human_score += 1
    count += 1
    if human_score == 3 or computer_score == 3:
        break

if human_score > computer_score:
    print('Human is the best!')
else:
    print('Human was defeated!')
