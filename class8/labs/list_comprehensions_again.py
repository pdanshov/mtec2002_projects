"""
list_comprehensions_again.py
===
1. Create two dictionaries, book1 and book2,  that contain information about a book: title, author, pages
    Dune, Frank Herbert, 500
    Frankenstein, Mary Shelley, 278
2. Iterate through each dictionary and create a list of strings with the key and value in a sentence - ex: title is Dune.
3. Use list comprehensions to do this
4. Print out the resulting lists

Example Output:
['author is Frank Herbert.', 'pages is 500.', 'title is Dune.']
['author is Mary Shelley.', 'pages is 278.', 'title is Frankenstein.']
"""
book1 = {'author': 'Frank Herbert', 'pages': 500, 'title': 'Dune'}
book2 = {'author': 'Mary Shelley', 'pages': 278, 'title': 'Frankenstein'}
list1 = [("%s is %s" % (k, v)) for k,v in book1.items()]
list2 = [("%s is %s" % (k, v)) for k,v in book2.items()]
print "%s\n%s" % (list1, list2)