"""
Pluralize
=====
Create a function that naively pluralizes words; it just adds an s!   Write a function called pluralize.  It takes one parameter - a string called word.  The function declaration should be pluralize(word).  It should return the word with an "s" appended to it.

Example Output (after importing into Python interactive shell):

>>> from pluralize import *
>>> pluralize("cake")
'cakes'

Extra Credit #1 - if the word passed in ends in o, pluralize it by adding an "es" instead of just s.

Extra Credit #2 - look up a list of nouns that have the same singular and plural form.  Put a few of those nouns in a Python list.  Use that list to determine if anything needs to be appended to the input word in order to pluralize it.  
"""

def pluralize(word):
	suffix='o'
	spnouns=['moose','fish','deer','aircraft','you','pants','shorts','eyeglasses','scissors','species','offspring','sheep','shrimp','series','means','panties','underwear','buffalo','trout','pike','swine','bison']
	special={'mouse':'mice','foot':'feet','man':'men','woman':'women','tooth':'teeth','mailman':'mailmen','child':'children','ox':'oxen','secratary':'secrataries'}
	wtwo=word.lower()
	if wtwo in spnouns:
		print word.capitalize()
	elif wtwo in special:
		print special[word].capitalize()
	elif wtwo.endswith(suffix):
		print (word+'es').capitalize()
	else:
		print (word+'s').capitalize()