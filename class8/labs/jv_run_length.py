"""
This module contains naive implementations of run length encoding and
decoding. These implementations will work for uppercase and lowercase
letter a through z. The decode function will definitely not work for
numeric characters that are encoded since there are no escape characters
to deal with ambiguity.

The decode function will let ValueErrors bubble up in case of a malformed
encoding.

>>> encode('tutt')
'1t1u2t'
>>> encode('wwwwhhhhhhhaaaaaaaaaaaaaaaaaaaat')
'4w7h20a1t'
>>> decode(encode('wwwwhhhhhhhaaaaaaaaaaaaaaaaaaaat'))
'wwwwhhhhhhhaaaaaaaaaaaaaaaaaaaat'
>>> decode('1t1u2t')
'tutt'
>>> decode('')
''
>>> decode('a2b')
Traceback (most recent call last):
File "<stdin>", line 1, in ?
ValueError: invalid literal for int() with base 10: ''
>>> decode('2a2bc')
Traceback (most recent call last):
File "<stdin>", line 1, in ?
ValueError: invalid literal for int() with base 10: ''
"""
def encode(s):
    cur_letter = None
    cur_letter_count = 0
    letter_list = []
    for letter in s:
        if letter != cur_letter:
            if cur_letter is not None:
                letter_list.append((cur_letter_count, cur_letter))
            cur_letter = letter
            cur_letter_count = 1
        else:
            cur_letter_count = cur_letter_count + 1
    letter_list.append((cur_letter_count, cur_letter))
    # yikes... uh... probably not the most maintainable/understandable code
    return "".join([str(letter[0]) + letter[1] for letter in letter_list])

def decode(s):
    cur_number = ''
    decoded = ''
    for c in s:
        if c.isdigit():
            cur_number += c
        else:
            decoded += c * int(cur_number)
            cur_number = ''
    return decoded

if __name__ == "__main__":
    import doctest
    doctest.testmod()

