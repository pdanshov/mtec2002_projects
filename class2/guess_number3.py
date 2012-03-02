n=5
print("I'm thinking of a number between 1 and 1000, what is it?")
u=int(raw_input("> "))
while u!=n:
	if u<n:
		if n-u==1:
			print("You guessed %d. You were off by just 1! Psst.. it's %d")%(u,n)
			u=int(raw_input("> "))
		else:
			print("You guessed %d. Go higher :P Psst.. it's %d")%(u,n)
			u=int(raw_input("> "))
	elif u>n:
		if u-n==1:
			print("You guessed %d. You were off by just 1! Hey! The number is %d")%(u,n)
			u=int(raw_input("> "))
		else:
			print("You guessed %d. Go lower :) Hey! The number is %d")%(u,n)
			u=int(raw_input("> "))
print("You guessed %d. You got it!")%u