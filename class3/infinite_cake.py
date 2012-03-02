"""
Infinite Cake
=====
How would you rewrite the original cake.py so that it continually asks you if you want cake unless you say "yes".  Do this without using loops.  Hint: wrap your original program in a function.... if the answer is no, call the function again. 

Example Output (the > denotes user input):

>>> from infinite_cake import *
>>> ask_cake()
want cake?
> no
want cake?
> no
want cake?
> no
"""
def cake():
    print'Do you want cake?'
    resp=raw_input('> ').lower()
    if resp!='yes':
        cake()
    elif resp=='yes':
        print'Do you want frosting?'
        resp=raw_input('> ').lower()
        if resp=='yes':
            print'Have a cake with frosting!'
        else:
            print'No frosting for you!'
    else:
        print'No cake for you!'
        print'No cake for you!'