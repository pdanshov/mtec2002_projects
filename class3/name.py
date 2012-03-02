"""
What's your name?
=====
Write a program that says "Hi there!".  Then, prompt the user for input.  If the user says "Hi" or "Hello", the program will ask another question - "what's your name?".  If their name is the same as your name, the program will say "Hi, [name of person], we have the same name!".  If the user does not have the same name, say "Hi, [name of person]" (but don't say you have the same name).  Finally, if the user didn't say "Hi" or "Hello" initially, the program should just say "Bye!".

Example Output (the > denotes user input):

$python name.py 
Hi there!
> *grumble*
Bye!

$python name.py 
Hi there!
> Hi
What's your name?
> Bob
Hi Bob!

$python name.py 
Hi there!
> Hi
What's your name?
> Joe   
Hi Joe, we have the same name!


Write this program in incremental steps.  
1. Write the part that says hi and prompts the user for input.  
2. Write a conditional to check the value of the input.... and say something appropriately.
3. Within that conditional, if the user said "Hi" or "Hello", ask the user for their name and store it in a variable.  
4. Finally, nest another conditional in your first if statement to check if your name matches the their name.  If you have the same name, print out a greeting again, but this time, with their name in it.
"""

"""
greeting=['Hi','Hello']
response=raw_input("> ")
if response in greeting:
"""

print "Hi there"
response=raw_input("> ")
if response=="Hi"or response=="Hello":
	print"What's your name?"
	response=raw_input("> ")
	if response=='Joe':
		print'Hi Joe, we have the same name.'
	else:
		print'Hi %s'%response
else:
	print"Bye"