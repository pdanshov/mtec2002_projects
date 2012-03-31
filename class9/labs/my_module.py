"""
my_module.py
===
1. Define a function called f1 and have it print "ONE!"
2. Define a function called f2 and have it print "TWO!"
3. Try running this module...
4. (INTERMEDIATE) call f1 and f2 only when running this module, not when importing (see: http://docs.python.org/tutorial/modules.html#executing-modules-as-scripts)
"""
def  f1():
    print "ONE!"
def f2():
    print "TWO!"
if __name__ == "__main__":
    import sys
    #f1(int(sys.argv[1]))
    print ""
    f1()
    f2()