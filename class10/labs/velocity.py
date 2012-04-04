"""
velocity.py
=====
Write a program that asks for distance and time.  It will print out the velocity.  It should be able to recover from invalid input or division by 0 errors.

1. Loop forever
2. Ask for distance; store in a variable named d
3. Ask for time; store in a variable named t
4. Calculate velocity by converting both values to floats and dividing d/t and print out the result
5. Put that inside a try: except: block... and catch the follow exceptions:
	ValueError
	ZeroDivisionError
6. If an exceptions happens print a message about it

Expected Output (> implies user input):
distance:
>24
time:
>12
distance: 24, time: 12
velocity: 2.0

distance:
>12
time:
>0
distance: 12, time: 0
Uh oh! can't divide by zero!

distance:
>42  
time:
>"asdf"
distance: 42, time: "asdf"
I don't think you put in two numbers.
>
"""
while True:
	d = raw_input("enter the distance: ")
	t = raw_input("enter the time: ")
	try:
		print float(d)/float(t)
	except ValueError:
		print "I don't think you put in two numbers."
	except ZeroDivisionError:
		print "Uh oh! can't divide by zero!"