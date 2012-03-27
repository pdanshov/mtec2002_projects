"""
loop_dictionary.py
===
1. Create two dictionaries, book1 and book2,  that contain information about a book: title, author, pages
	Dune, Frank Herbert, 500
	Frankenstein, Mary Shelley, 278
2. Iterate through each dictionary and print out both the key and value in a sentence - ex: title is Dune.
3. Put the dictionaries in a list called list of books
4. Iterate over the list and print each dictionary

Example Output:
author is Frank Herbert
pages is 500
title is Dune
author is Mary Shelley.
pages is 278.
title is Frankenstein.
{'author': 'Frank Herbert', 'pages': 500, 'title': 'Dune'}
{'author': 'Mary Shelley', 'pages': 278, 'title': 'Frankenstein'}
"""
book1 = {'author': 'Frank Herbert', 'pages': 500, 'title': 'Dune'}
book2 = {'author': 'Mary Shelley', 'pages': 278, 'title': 'Frankenstein'}
for k,v in book1.items():
	print "%s is %s" % (k, v)
for k,v in book2.items():
    print "%s is %s" % (k, v)
list_of_books = [book1, book2]
for x in list_of_books:
    print x