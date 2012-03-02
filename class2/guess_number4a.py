n=5
o=2
print("I'm thinking of a number between 1 and 1000, what is it?")
u=int(raw_input("> "))
while u!=n:
	if n-u==o or u-n==o:
		print('You guessed %d. You were off by just %d! Btw, the number is %d.')%(u,o,n)
		u=int(raw_input("> "))
	elif u<n:
		o2=n-u
		print("You guessed %d. You were off by %d, go higher :P Psst.. it's %d.")%(u,o2,n)
		u=int(raw_input("> "))
	else:
		o2=u-n
		print("You guessed %d. You were off by %d, go lower :) Hey! The number is %d.")%(u,o2,n)
		u=int(raw_input("> "))
print("You guessed %d. You got it!")%u