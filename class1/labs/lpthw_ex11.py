print "How old are you?",
age = raw_input()
print "How tall are you?"
height = raw_input('--> ')
print "How much do you weigh?",
weight = raw_input('> ')
# Changes %r to %s to get rid of escape character '/', when displaying height in x'x" format
print "So, you're %r years old, %s tall and %r heavy." % (
    age, height, weight)