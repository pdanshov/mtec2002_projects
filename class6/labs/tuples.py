"""
tuples.py
===
1. Tuples are lists that cannot be changed
2. Just like lists they are comma separated values
3. However, instead of square brackets, tuples are enclosed by parentheses
4. This means that:
	a. Elements can be accessed like regular lists (0 based start index, using brackets to index into an element)
	b. However, you can't assign any new values
	c. They don't have an append or extend method
	d. They don't have a remove method
	e. They don't have an index method

Examples:
(3, 7)
("hello", "how", "are", "you")

Where you've seen them before / why would you use one:
1. When creating constant set of values - for example, one could represent the origin of a two dimensional plane as: origin = (0, 0)
2. When you need to make sure your set of values cannot be changed or overridden
3. In string formatting/string interpolation
"""
# create a tuple with 2 strings
animals=('cat','dog')

# print out the tuple
print animals

# define a tuple with 5 numbers
numbers=(5,4,3,2,1)

# print out the tuple
print numbers

# print out the 2nd element in the tuple
print numbers[1]

# try to change the value of the second element
#numbers[1]=222222

# what happened?  comment out the line you just wrote to continue....
# try using append() on a tuple to add another element
#numbers.append(222222)

# what happened?  comment out the line you just wrote to continue....
# let's compare to lists: try creating a list and changing a value, it should work
my_list=[1,2,3]
my_list[1]=22222
print my_list

# try appending an element to a list
my_list.append(33333)
print my_list

# try using the tuple you created above in string formatting
print'%s %s'%animals

# let's do another... without using a variable
print'%s %s'%('hi','hello')

# tuples can also be items in a list!
crazy_list=[(1,2),(4,5),(4,4)]
print crazy_list

# let's iterate through them
for x in crazy_list:
	print x