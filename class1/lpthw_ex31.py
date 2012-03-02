print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print ""
        print "Your body survives powered by a mind of jello.  Good job!"
        print ""
        print "Type c to continue"
        next = raw_input("> ")
        if next=="c":
           print "You find yourself in an ornate hallway with portraits of old men on either side.     At the end is the final door..    1.enter, 2.leave or 3.take a closer look?"
           next=raw_input("> ")
           if next=="3":
              print "           Above the door hangs a sign:"
              print "             ~~Wealth and Riches~~"
              print ""
              print "1.enter or 2.leave?"
              next=raw_input("> ")
              if next=="1":
                print "As you step through the door a feeling of absolute dread comes over you as you realize there is no ground beneath your feet!"
                print "You find yourself falling through an endless abyss as a recurring thought flashes through your mind: \"True wealth and riches are within\"."
              else:
                print "As you turn to walk away you suddenly find yourself at home in the midst of an informal gathering."
                print "Surrounded by friends and family you feel relaxed and any regret you may have is alleviated at once by an edifying sense of narrowly escaping some unpleasant fate."
           elif next=="1":
              print "You start to walk toward the door, as you get closer you see a sign above it:"
              print ""
              print "             ~~Wealth and Riches~~"
              print ""
              print "1.enter or 2.leave?"
              next=raw_input("> ")
              if next=="1":
                print "As you step through the door a feeling of absolute dread comes over you as you realize there is no ground beneath your feet!"
                print "You find yourself falling through an endless abyss as a recurring thought flashes through your mind: \"True wealth and riches are within\""
              else:
               print "Are you sure?"
               print "1.yes"
               print "2.no"
               next=raw_input("> ")
               if next=="1":
                print "As you turn to walk away you suddenly find yourself at home in the midst of an informal gathering."
                print "Surrounded by friends and family you feel relaxed and any regret you may have is alleviated at once by an edifying sense of narrowly escaping some unpleasant fate."  
               else:
                print "As you turn to walk away your curiosity gets the better of you and you turn again to walk toward the door but it disappears, the walls close in on you and you die."
           else:
              print "Are you sure?"
              print "1.yes"
              print "2.no"
              next=raw_input("> ")
              if next=="1":
                print "As you turn to walk away you suddenly find yourself at home in the midst of an informal gathering."
                print "Surrounded by friends and family you feel relaxed and any regret you may have is alleviated at once by an edifying sense of narrowly escaping some unpleasant fate."  
              else:
                print "As you turn to walk away your curiosity gets the better of you and you turn again to walk toward the door but it disappears, the walls close in on you and you die."
              
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

else:
    print "You stumble around and fall on a knife and die.  Good job!"
