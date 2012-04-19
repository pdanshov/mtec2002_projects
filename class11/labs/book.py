"""
book.py
=====
Create a class named book that represent a book that can be checked out or 
checked in from a library.

1. Create a class named Book
2. Create a constructor (__init__) method that takes two arguments: self and title)
3. The constructor should set the attributes of the instance:
	self.title should equal title
	self.author should be an empty string
	self.available should be True by default
4. Create a method called check_out that only takes one argument: self, it should change the available attribute to False
5. Create a method called check_in that only takes one argument: self, it should change the available attribute to True
6. Test your class by creating an instance of Book after your class definition
7. Set the author of your book (your_variable.author = "Frank Herbert"; print it out and run your program
8. Run the check_out method on your book; print it out and run your program
9. Run the check_in method on your book; print it out and run your program

=====
Dune by  - True
Dune by Frank Herbert - True
Dune by Frank Herbert - False
Dune by Frank Herbert - True
(INTERMEDIATE) Turn authors into a list, add an add_author method, default to empty list
(INTERMEDIATE) Raise an exception if a book is not available, and someone tries to check it out
	
"""

#This adds BookError to the Exception class
class BookError(Exception):
	pass

class Book:
	def __init__(self, title):
		self.title = title
		#self.author = ""
		self.authors = []
		self.available = True

	def __str__(self):
		return "%s by %s - Available: %s" % (self.title, self.authors, self.available)

	def check_out(self):
		if self.available == False:
			raise BooleanError, BookError("Book already taken")
		else:
			self.available = False

	def check_in(self):
		self.available = True

	def add_author(self, name):
		self.authors.append(name)