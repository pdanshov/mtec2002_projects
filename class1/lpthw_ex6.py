# Initializes the x string variable
x = "There are %d types of people." % 10
# Initializes the binary string variable
binary = "binary"
# Initializes the do_not string variable
do_not = "don't"
# Initializes the y string variable
y = "Those who know %s and those who %s." % (binary, do_not)
# Displays string variables x and y
print x
print y
# Displays a string with the string stored in the x variable, Displays a string with the string stored in the y variable
print "I said: %r." % x
print "I also said: '%s'." % y
# Initializes the boolean variable hilarious, initializes string variable joke_evaluation
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# Displays string variable joke_evaluation with the boolean variable stored in hilarious
print joke_evaluation % hilarious
# Initializes string variables w and e
w = "This is the left side of..."
e = "a string with a right side."
# Prints together the strings stored in string variables w and e
print w + e