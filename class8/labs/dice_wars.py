"""
dice_wars.py
===
Break down your problem using a flow chart, pseudocode, etc.  Here's a basic list of what should happen:
1. Print out ASCII art!!!
   ------
  /     /|  ~Dice Warz~
 ------| |
 |     | |
 |     |/
 ------
2. Keep track of scores using a dictionary
3. Loop forever
4. Ask for command
5. If command is roll, roll random dice for computer and player
6. Determine who wins (3 states: computer wins, player wins or tie)
7. For each state add scores appropriately, and print out both rolls and scores
8. If command is quit, then exit the game
9. If the command is not quit or roll, say "I don't know that command"
"""
import random
print """
   ______
  /  o  /|  ~Dice Warz~
 .-----, |
 | o o | |
 | o o |/
 '-----'
 """
scores = {"player":0, "computer":0}
while True:
	print "roll or quit?"
 	command = raw_input("> ")
 	if command == "roll":
 		for x in range(100):
 			animation = "|/-\\"
			idx = 0
			while x:
				print (animation[idx % len(animation)] + "\r")
    			idx += 1
    			#time.sleep(0.1)
 		player_roll = random.randint(1, 6)
 		computer_roll = random.randint(1, 6)
 		print "Player roll: %s, Computer roll: %s" % (player_roll, computer_roll)
 		if player_roll > computer_roll:
 			print "Player won!"
 			scores["player"] += 1
 		elif player_roll < computer_roll:
 			print "Computer won!"
 			scores["computer"] += 1
 		else:
 			print "Tie!"
 		print scores
 	elif command == "quit":
 		exit()