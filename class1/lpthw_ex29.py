people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"
  
people += 20
if people > cats:
    print "Not many cats! The world is saved!"
	
people -= 30
if people < dogs:
    print "The world is drooled on!"
	
people += 10
if people > dogs:
    print "The world is dry!"
	

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

people -= 10
if people <= dogs:
    print "People are less than or equal to dogs."

people = dogs
print "People: ",people
print "Dogs: ",dogs
if people == dogs:
    print "People are dogs."