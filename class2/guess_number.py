n=5
print("I'm thinking of a number between 1 and 1000, what is it?")
u=raw_input("> ")
print("%s") %u
u=int(u)
print("%d") %u
if u==n:
	print("You got it!")
elif u>n:
	print("Go lower :)")
else:
	print("Go higher :P")