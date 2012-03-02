n=5
print("I'm thinking of a number between 1 and 1000, what is it?")
u=raw_input("> ")
u=int(u)
while u!=n:
	if u<n:
		print("Go higher :P")
		u=raw_input("> ")
		u=int(u)
	else:
		print("Go lower :)")
		u=raw_input("> ")
		u=int(u)
print("You got it!")