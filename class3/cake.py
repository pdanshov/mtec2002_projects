"""
Cake
=====
Write a program that asks the user if they want cake.  If the user wants cake, ask the user if they want frosting.  If the user answers yes to either of these questions print out a statement giving them what they want.  If the user says no to either, print out a message say no frosting or cake for you!

Example Output (the > denotes user input):

$ python cake.py 
Do want cake?
> yes
Do you want frosting on your cake?
> yes
Have a cake with frosting!

$ python cake.py 
Do want cake?
> yes
Do you want frosting on your cake?
> no
No frosting for you!

$ python cake.py 
Do want cake?
> no
No cake for you!

Extra Credit #1 - normalize the user input by using a string function that will transform any variation in casing  ("Yes", "yes", "YES") so that you only have to compare the input to "yes"

Extra Credit #2 - if you didn't add an explicit check for "no", do so.  If the user does not respond with either a yes or a no, add a code path that berates the user for not answering appropriately!

Extra Credit #3... Could you use lists to help normalize user input?  If so, how?  Implement it.  Would a list's index() function work?  What would you need to watch out for?
"""
"""
print'Do you want cake?'
resp=raw_input('> ').lower()
if resp=='yes':
	print'Do you want frosting?'
	resp=raw_input('> ').lower()
	if resp=='yes':
		print'Have a cake with frosting!'
	else:
		print'No frosting for you!'
elif resp=='no':
	print'No cake for you!'
"""

l=['yes','no']
print'Do you want cake?'
resp=raw_input('> ').lower()
while resp not in l:
	print'Type either Yes or No!'
	resp=raw_input('> ')
if resp=='yes':
	print'Do you want frosting?'
	resp=raw_input('> ').lower()
	if resp=='yes':
		print'Have a cake with frosting!'
	else:
		print'No frosting for you!'
else:
	print'No cake for you!'
	print'No cake for you!'