def mod(x,y):
    c=0
    m=x
    err1='Cannot divide by zero'
    if (y==0):
        return err1
    if (x>y):
        while (m>y):
            c+=y
            m-=c
    elif (x==y):
        m=0
    return m