people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."
    people += 20
elif cars < people:
    print "We should not take the cars."
    people -= 10
else:
    print "We can't decide."

buses += 40
if buses > cars:
    print "That's too many buses."
    buses -= 40
elif buses < cars:
    print "Maybe we could take the buses."
    buses += 25
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

if cars > people and buses < cars:
  print "People:",people,"cars:",cars,"Buses:",buses,"True"
else:
	print "People:",people,"cars:",cars,"Buses:",buses,"False"
