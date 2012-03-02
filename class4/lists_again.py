"""
Write a line of code under each comment.  Run your code after each line to make sure there are no errors.
"""

# use range to create a list of numbers from 0-9; assign it to a variable called numbers

numbers=range(10)

# print the list called numbers; you should see [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print numbers

# create a list called names with the words "Alice" and "Bob"

names=['Alice','Bob']

# print the list called names; you should see ['Alice', 'Bob']

print names

# print the length of the names list; you should see 2

print len(names)

# add "Carol" to the list of names using append

names.append('Carol')

# print the names list; you should see ['Alice', 'Bob', 'Carol']

print names

# print the length of the names list again; you should see 3

print len(names)

# find where Bob is in the list by using index; assign it to a variable called bob_index 

bob_index=names.index('Bob')

# print out the variable that contains that index, bob_index; you should see 1

print bob_index

# remove Bob by using the "remove" function

names.remove('Bob')

# print the names list; you should see ['Alice', 'Carol']

print names

# try to find Bob again by using "index"; run your program, you should see an error

#names.index('Bob')
# comment out the line above so that the error does not occur

# find where Carol is in the list by using "index"; assign it to a variable called carol_index

carol_index=names.index('Carol')

# print out the variable that contains that index, carol_index; you should see 1 

print carol_index

# using that index, delete Carol from the list using the del() function

del names[carol_index]

# print out the names list; you should see ['Alice']

print names

# create another list called colors with the words "red", "yellow", and "blue" 

colors=['red','yellow','blue']

# print out both the list of names and the list of colors; you should see ['Alice'] ['red', 'yellow', 'blue']

print names,colors

# add the list of colors to the list of names using "append"

names.append(colors)

# print the names list; you should see ['Alice', ['red', 'yellow', 'blue']]

print names

# add each element of the list of colors to the list of names using extend

names.extend(colors)

# print the names list; you should see ['Alice', ['red', 'yellow', 'blue'], 'red', 'yellow', 'blue']

print names

# pop off the last element and assign it to a variable called last_color

last_color=names.pop()

# print last_color; you should see blue

print last_color

# print the names list; you should see ['Alice', ['red', 'yellow', 'blue'], 'red', 'yellow']

print names

# NOW WE'RE WORKING ON THE COLORS LIST....

# going back to the colors list... add "green" to the colors list by using append

colors.append('green')

# print the colors list; you should see ['red', 'yellow', 'blue', 'green']

print colors

# add "orange" to the colors list by using append

colors.append('orange')

# print the colors list; you should see ['red', 'yellow', 'blue', 'green', 'orange']

print colors

# create a new list with the first 4 elements of the colors list using slicing; assign it to a variable called first_four

first_four=colors[:4]

# print the first_four list; you should see ['red', 'yellow', 'blue', 'green']

print first_four

# sort the values in the colors list using the sort method

colors.sort()

# print the colors list; you should see ['blue', 'green', 'orange', 'red', 'yellow'] 

print colors

# use the join method on a string to create a string for the sorted list of colors; assign it to a variable called colors_string

colors_string=','.join(colors)

# print colors_string; you should see blue,green,orange,red,yellow

print colors_string

# use a string's split method to turn "foo,bar,baz" into a list of 3 strings; assign the list to a variable called nonsense_words

nonsense_words='foo,bar,baz'.split(',')

# print nonsense_words; you should see ['foo', 'bar', 'baz']

print nonsense_words

# in the end, the output of your script should be:
"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
['Alice', 'Bob']
2
['Alice', 'Bob', 'Carol']
3
1
['Alice', 'Carol']
1
['Alice']
['Alice'] ['red', 'yellow', 'blue']
['Alice', ['red', 'yellow', 'blue']]
['Alice', ['red', 'yellow', 'blue'], 'red', 'yellow', 'blue']
blue
['Alice', ['red', 'yellow', 'blue'], 'red', 'yellow']
['red', 'yellow', 'blue', 'green']
['red', 'yellow', 'blue', 'green', 'orange']
['red', 'yellow', 'blue', 'green']
['blue', 'green', 'orange', 'red', 'yellow']
blue,green,orange,red,yellow
['foo', 'bar', 'baz']
"""

# INTERMEDIATE

# create a list called "a" and set it equal to [1, 2, 3]

a=range(1,4)

# create a list called "b" and set it equal to "a"

b=a

# print a and b to verify that they're both equal to [1, 2, 3]

print a,b

# append a value to the list, "a"

a.append(4)

# print a and verify that the list now has another value appended to it

print a

# in a comment, write down what you think the value of b will be

# b will be [1, 2, 3]

# print out b

print b

# Read http://openbookproject.net/thinkcs/python/english2e/ch09.html - sections 9.10, 9.11, 9.12

# if you wanted to make a copy or clone of a rather than an alias, how would you do it?

c=a[:]

print c