def only_three(los):
    for x in los[:]:# x is a variable in the list los and also the amount of times the loop iterates
        l=len(x)# the length of the current variable being processed/tested is stored in l
        if l>3 or 3>l:los.remove(x)# can also write if l!=3
    print los