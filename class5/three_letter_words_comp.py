"""
Three Letter Words
=====
* Create a list of strings called words that contains "dog","lizard","cat","hawk","pig", and "ibek" 
* Create an empty list called three_letter_words
* Use a for loop to iterate through your words list...
* If the length of your word is greater than 3, append it to your three_letter_words list
* Print "Words: [your words list]"
* Print "Three letter words: [your three_letter_words list]"

Example Output:
Words: ['dog', 'lizard', 'cat', 'hawk', 'pig', 'ibek']
Three letter words: ['dog', 'cat', 'pig']
"""
words=['dog','lizard','cat','hawk','pig','ibek']
three_letter_words=[x for x in words if len(x)>3]
"""
for x in words:
    if len(x)>3:
        three_letter_words.append(x)
"""
""" three_letter_words+=x # This returns the following output:
Three letter words: ['l', 'i', 'z', 'a', 'r', 'd', 'h', 'a', 'w', 'k', 'i', 'b', 'e', 'k']
and so does three_letter_words.extend(x)"""
print 'Words: %r\nThree letter words: %r'%(words,three_letter_words)