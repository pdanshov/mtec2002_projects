"""
quit_it.py
===
1. Ask the user to type quit if they want to leave the program - "Type quit to stop this program"
2. Prompt the user for input, and store the input in a variable named command
3. Use a while loop to continue to ask for input until the user types in quit

Example Output:
Type quit to stop this program
>I don't want it to stop yet
Type quit to stop this program
>Still ok
Type quit to stop this program
>quit
Thanks!  See you later.
"""
command=None
while command!='quit':
	command=raw_input('Type quit to stop this program \n> ').lower()
print'Thanks! See you later.'