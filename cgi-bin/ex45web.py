import cgitb; cgitb.enable()
import cgi
import sys
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
sum1 = 0
sum2 = 0
activesum = 0
activeplayername = ''
player1 = ''
player2 = ''
cont = ''

print """
<html>
<head>
  <title>PIG - A DICE GAME</title>
  <meta name='viewport' content='width=device-width,minimum-scale=1.0,maximum-scale=1.0' />
</head>
<body>
  <h3>PIG - A DICE GAME</h3>
  <p>This is a game for 2 players. One of the players (selected by the computer) starts playing by rolling the dice. The player can continue until the player chooses to stop or rolls 1 on dice. The sum of the dices are added to their total turn. If the player rolls 1 all the points in the same round will be deleted. Then the next player starts to roll the dice. The player that first reaches 100 points win.</p>
"""

"""Prompt names of players."""
print """
<form action="ex45web.py" method="post">
What is the name of player 1? <input type="text" name="player1">
What is the name of player 2? <input type="text" name="player2">
<input type="submit" name="submit" value="Start game!" /> 
</form>
"""

form = cgi.FieldStorage()
player1 = form.getvalue("player1", "(no player1)")
player2 = form.getvalue("player2", "(no player2)")

"""Draw who to start game."""
if player1 != '(no player1)' and player2 != '(no player2)':
	draw = who_starts()

	if draw == 1:
		activeplayer = 1
		print " "
		print " "
		print "## PLAYER %s - YOU START! ##" % (player1)
		print " "
	else:
		activeplayer = 2
		print " "
		print " "
		print "## PLAYER %s - YOU START! ##" % (player2)
		print " "

	"""Play game."""
	while activesum < 100:
		dice = roll_dice()
		
		if dice == 1:
			if activeplayer == 1:
				activesum = sum1
			else:
				activesum = sum2
				
			print " "
			print "The dice rolled %r and you lost the points in this round. Sum is now %r" % (dice, activesum)
			cont = 'n'
		else:
			activesum = activesum + dice

			print " "
			print "The dice rolled %r and sum is %r" % (dice, activesum)
				
			if activesum < 100:
				while cont != 'y' and cont != 'n':
					print """
					<form action="ex45web.py" method="post">
					Continue? (y/n) <input type="text" name="cont" maxlength="1" size="2">
					<input type="submit" name="submit" value="Enter" /> 
					</form>
					"""
					
					form = cgi.FieldStorage()
					cont = form.getvalue("cont", "(no cont)")
				
				if cont == '(no cont)':
					while cont != 'y' and cont != 'n':
						print """
						<form action="ex45web.py" method="post">
						I did not understand that! Don't be a politician, answer yes (y) or no (n)!
						Continue? (y/n) <input type="text" name="cont" maxlength="1" size="2">
						<input type="submit" name="submit" value="Enter" /> 
						</form>
						"""

						form = cgi.FieldStorage()
						cont = form.getvalue("cont", "(no cont)")
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
		
		"""End of html"""
		print "</body></html>"