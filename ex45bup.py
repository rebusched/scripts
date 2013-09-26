from sys import argv
import random

def roll_dice():
    """This function will roll the dice and return value."""
    dice = random.randint(1, 6)  # Integer from 1 to 6, endpoints included
    return dice
	
"""Define prompt."""
prompt = '> '

"""Prompt names of players."""
print "What is the name of player 1?"
player1 = raw_input(prompt)
print "What is the name of player 2?"
player2 = raw_input(prompt)

"""Play game."""
sum1 = 0
sum2 = 0
activesum = 0
activeplayer = 1
activeplayername = ''

print " "
print "%s - you start!" % (player1)

while (sum1 < 100) and (sum2 < 100):
	dice = roll_dice()
	
	if dice == 1:
		print "The dice rolled %r and you lost the points in this round. Sum is now %r" % (dice, activesum)
		cont = 'n'
	else:
		if activeplayer == 1:
			sum1 = sum1 + dice
			activesum = sum1
		else:
			sum2 = sum2 + dice
			activesum = sum2

		print "The dice rolled %r and sum is %r" % (dice, activesum)
			
		if activesum < 100:
			print "Continue? (y/n)"
			cont = raw_input(prompt)
			
	if cont == 'n':
		if activeplayer == 1:
			activeplayer = 2
			activeplayername = player2
		else:
			activeplayer = 1
			activeplayername = player1
		
		print " "
		print "Player %s - your turn!" % (activeplayername)
else:
	"""Game has finished. Print results."""
	print "%s has %r points. %s has %r points." % (player1, sum1, player2, sum2)
	if sum1 > sum2:
		print "%s vant! Gratulerer!!" % (player1)
	else:
		print "%s vant! Gratulerer!!" % (player2)