import random
import logging	
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s-  %(message)s')
guess = ''
logging.disable(logging.CRITICAL)
logging.debug('Start of a program')
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('In loop')

toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 1 and guess =='heads':
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    toss = random.randint(0,1)
    if toss == 1 and guess == 'tails':
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

