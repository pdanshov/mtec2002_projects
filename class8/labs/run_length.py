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
def encode(s):
    c = 1
    r = 1
    l = []
    for x in s:
        if x == s[r]:
            c += 1
        else:
            l.append(c)
            l.append(x)
            c = 1
        if r != len(s)-1:
            r += 1
        else:
            l.append(c)
            l.append(x)
            break
    print ''.join(map(str, l))
    
def decode(s):
    import re
    l = []
    r = 1
    for x in s:
        if re.match(r'[\d]*$', x):
            l.append(int(x)*s[r])
            r += 1
        elif r != len(s)-1:
            r += 1
        else:
            break
    print ''.join(map(str, l))
