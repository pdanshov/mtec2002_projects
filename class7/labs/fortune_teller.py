"""
fortune_teller.py
===
1. Create a list of fortunes: 'you will write a program', 'you have a lot of tabs in your future', 'boo!' and store it in a variable called fortunes
2. Use random to print out a random fortune when you run the program
3. Run the program several times

Expected Output:

$ python fortune_teller.py 
boo!
$ python fortune_teller.py 
you have a lot of tabs in your future
$ python fortune_teller.py 
you have a lot of tabs in your future
"""
import random
fortunes = ['you will write a program', 'you have a lot of tabs in your future', 'boo!']
index = random.randint(0, 2)
print "\n%s\n" % fortunes[index]