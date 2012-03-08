"""
binary_search.py
===
1. Write a function named search that takes two arguments, a *sorted* list and a value to search for
2. If the value is in the list, return the index of the value
3. If the value is not in the list, return -1
4. Do not use the index() function or in
5. Instead, implement binary search - read the first paragraph on wikipedia: 
	http://en.wikipedia.org/wiki/Binary_search_algorithm
6. See an example in action (enter a state name): 
	http://www.dave-reed.com/book/Chapter8/search.html
7. Don't hesitate to look up the pseudocode: 
	http://www.computingstudents.com/notes/computation_and_algorithms/binary_search.php

Some test output follows!
"""
def search(sorted_list, value):
	# implement your algorithm here
	# defaulting to not found
	return -1
		
# some tests (we'll learn about automated testing later...)
my_sorted_list =[7, 32, 65]
value = 7
print "result: %s, value: %s, list: %s" % (search(my_sorted_list, value), value, my_sorted_list)
value = 32
print "result: %s, value: %s, list: %s" % (search(my_sorted_list, value), value, my_sorted_list)
value = 65
print "result: %s, value: %s, list: %s" % (search(my_sorted_list, value), value, my_sorted_list)
value = 2
print "result: %s, value: %s, list: %s" % (search(my_sorted_list, value), value, my_sorted_list)
value = 8
print "result: %s, value: %s, list: %s" % (search(my_sorted_list, value), value, my_sorted_list)

my_sorted_list =[7, 32, 65, 65]
value = 65
print "result: %s, value: %s, list: %s" % (search(my_sorted_list, value), value, my_sorted_list)

my_sorted_list = [7, 32, 65, 70, 100]
value = 65
print "result: %s, value: %s, list: %s" % (search(my_sorted_list, value), value, my_sorted_list)
value = 70
print "result: %s, value: %s, list: %s" % (search(my_sorted_list, value), value, my_sorted_list)

my_sorted_list = [7, 32, 65, 70, 100, 102]
value = 65
print "result: %s, value: %s, list: %s" % (search(my_sorted_list, value), value, my_sorted_list)
value = 70
print "result: %s, value: %s, list: %s" % (search(my_sorted_list, value), value, my_sorted_list)

my_sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
value = 9
print "result: %s, value: %s, list: %s" % (search(my_sorted_list, value), value, my_sorted_list)
value = 20
print "result: %s, value: %s, list: %s" % (search(my_sorted_list, value), value, my_sorted_list)
