import random

options = ['rock', 'paper', 'scissors']
userScores = 0
compScores = 0
rounds = 0
results = []

while rounds < 7 and userScores < 4 and compScores < 4:
    print(f'---Round {rounds +1}---')
    user = input('rock, paper, or scissors? (q to quit): ').lower()
    if user == 'q':
        break
    comp = random.choice(options)
    print(f'computer chose: {comp}')
    if user == comp:
        print("It's a tie, No round counted.\n")
        continue 
    elif (user == 'rock' and comp == 'scissors') or \
         (user == 'paper' and comp== 'rock') or \
         (user == 'scissors' and comp == 'paper'):
     outcome = 'user'
     userScores += 1
    else:
        outcome = "computer"
        compScores += 1

    rounds += 1
    results.append((rounds, user, comp, outcome))
    print(f'Round {rounds} Winner -> {outcome}')
    print(f'Score -> You: {userScores}, Computer: {compScores}')

print("Game Review")
for r in results:
   print(f'Round {r[0]} \n You chose {r[1]} -> Computer chose {r[2]} \n Winner: {r[3]}')
print('---Final results---')
if userScores == 4:
   print(f'You are the overall winner!')
elif compScores == 4:
   print(f'Computer is the overall winner!')
else:
   print("Game Over! No one reached 4 wins in 7 rounds.")

    

