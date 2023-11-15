import random
guess=''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess=input().lower() 
toss=random.randint(0, 1)
if toss==0:
    flip='tails'
else:
    flip='heads'
if flip==guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess=input().lower()
    if flip==guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
