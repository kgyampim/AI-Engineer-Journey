import random

options = ['rock', 'paper', 'scissors']

while True:
    user = input('rock, paper, or scissors? (q to quit): ').lower()
    if user == 'q':
        break
    comp  = random.choice(options)
    print(f'computer chose: {comp}')
    if user == comp:
     print('game ends in a tie, since all players chose the same options!')
    elif (user == 'rock' and comp == 'scissors') or \
         (user == 'paper' and comp == 'rock') or \
         (user == 'scissors' and comp == 'paper'):
     print('You win!')
    else:
        print('You lose!')

print("Game Over!")
    

