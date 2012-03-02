def only_three(los):
    def f(x):return len(x)%3==0
    l=filter(f,los)
    print l # params are immutable, must store calculations in a new var