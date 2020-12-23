import random
numberOfStreaks = 0
head_tails = ['H','T']
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips100 = []
    for i in range(1,101):
    	flip = random.choice(head_tails)
    	flips100.append(flip)


    # Code that checks if there is a streak of 6 heads or tails in a row.

    for i in range(1,len(flips100)-6):
    	if flips100[i] == flips100[i+1] == flips100[i+2] == flips100[i+3] == flips100[i+4] == flips100[i+5] != flips100[i+6]:
    		numberOfStreaks+=1
  
print('Chance of streak: %s%%' % (numberOfStreaks / 100))