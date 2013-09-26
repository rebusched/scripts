import random

def who_starts():
    """This function will draw which player to start game."""
    draw = random.randint(1, 2)  # Integer from 1 to 2, endpoints included
    return draw

def roll_dice():
    """This function will roll the dice and return value."""
    dice = random.randint(1, 6)  # Integer from 1 to 6, endpoints included
    return dice

"""Definitions."""
prompt = '> '
sum1 = 0
sum2 = 0
activesum = 0
activeplayername = ''

"""Explain game and rules."""
print " "
print "PIG - A DICE GAME"
print "This is a game for 2 players. One of the players (selected by the computer)"
print "starts playing by rolling the dice. The player can continue until the"
print "player chooses to stop or rolls 1 on dice. The sum of the dices are added"
print "to their total turn. If the player rolls 1 all the points in the same round"
print "will be deleted. Then the next player starts to roll the dice. The player"
print "that first reaches 100 points win."
print " "

"""Prompt names of players."""
print "What is the name of player 1?"
player1 = raw_input(prompt)
print "What is the name of player 2?"
player2 = raw_input(prompt)

"""Draw who to start game."""
draw = who_starts()

if draw == 1:
	activeplayer = 1
	print " "
	print " "
	print "## PLAYER %s - YOU START! ##" % (player1)
else:
	activeplayer = 2
	print " "
	print " "
	print "## PLAYER %s - YOU START! ##" % (player2)

"""Play game."""
while activesum < 100:
	dice = roll_dice()
	
	if dice == 1:
		if activeplayer == 1:
			activesum = sum1
		else:
			activesum = sum2
			
		print "The dice rolled %r and you lost the points in this round. Sum is now %r" % (dice, activesum)
		cont = 'n'
	else:
		activesum = activesum + dice

		print "The dice rolled %r and sum is %r" % (dice, activesum)
			
		if activesum < 100:
			print "Continue? (y/n)"
			cont = raw_input(prompt)
			
			while cont != 'y' and cont != 'n':
				print "I did not understand that! Don't be a politician, answer yes (y) or no (n)!"
				print "Continue? (y/n)"
				cont = raw_input(prompt)			
		else:
			cont = 'y'
			if activeplayer == 1:
				sum1 = activesum
			else:
				sum2 = activesum
			
	if cont == 'n':
		if activeplayer == 1:
			sum1 = activesum
			activeplayer = 2
			activeplayername = player2
			activesum = sum2
		else:
			sum2 = activesum
			activeplayer = 1
			activeplayername = player1
			activesum = sum1
		
		print " "
		print " "
		print " "
		print "## PLAYER %s - YOUR TURN! ##" % (activeplayername)
else:
	"""Game has finished. Print results."""
	print " "
	print " "
	print "WE HAVE A WINNER!"
	print "%s has %r points. %s has %r points." % (player1, sum1, player2, sum2)
	if sum1 > sum2:
		print "%s won! Congratulations!!" % (player1)
	else:
		print "%s won! Congratulations!!" % (player2)
	print " "