def guess_number(secret_number,close_by):
	n=secret_number
	o=close_by
	print("I'm thinking of a number between 1 and 1000, what is it?")
	u=int(raw_input("> "))
	while u!=n:
		o2=abs(n-u)
		if o2==o or o2==o:
			print('You guessed %d. You were off by just %d! Btw, the number is %d.')%(u,o,n)
			u=int(raw_input("> "))
		elif u<n:
			print("You guessed %d. You were off by %d, go higher :P Psst.. it's %d.")%(u,o2,n)
			u=int(raw_input("> "))
		else:
			print("You guessed %d. You were off by %d, go lower :) Hey! The number is %d.")%(u,o2,n)
			u=int(raw_input("> "))
	print("You guessed %d. You got it!")%u