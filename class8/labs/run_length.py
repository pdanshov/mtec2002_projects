"""
run_length.py
===
1. Read http://en.wikipedia.org/wiki/Run-length_encoding#Example
2. Create a function called encode that takes one argument, s
3. Encode the string s using the algorithm above
4. Run the function on the following strings: "tutt", "razzamtazz", "wwwwhhhhhhhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaat the what??"

Expected Output:
tutt encoded is 1t1u2t
razzamtazz encoded is 1r1a2z1a1m1t1a2z
wwwwhhhhhhhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaat the what?? encoded is 4w7h36a1t1 1t1h1e1 1w1h1a1t2?

5. (OPTIONAL) Try writing a decode function!

Expected Output:
1t1u2t decoded is tutt
(etc)
"""
from operator import itemgetter
import sys
def encode(s):
    d = {}
    l = []
    c = 0
    for x in s:
        if d.get(x, 0) == 0 and c != (map(itemgetter(0), l).index(x)):
            d[x] = 1
            l = d[x]
            c += 1
        else:
            d[x] += 1
    print "Encoding:"
    for k,v in d.items():
        sys.stdout.write(("%s%s" % (v,k)))
    print ""
    """
    for k,v in d.items():
        print "%s%s\b" % (v,k)
    print ""
    """
"""
def decode(s):
    string = s
        for x in s:
            """