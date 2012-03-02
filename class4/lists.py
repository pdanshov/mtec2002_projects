"""
List operations
"""
# use range to create a list of ints; assign to a variable called list_of_numbers
list_of_numbers=range(10)

# create a list of strings with list literals (let's say simpson's characters); assign to a variable called list_of_strings
list_of_strings=['bart','marge','lisa']

# create an empty list; assign to a variable called my_list
my_list=[]

# find the length of all three of the above lists; print each out
print len(list_of_strings)
print len(my_list)
print len(list_of_numbers)

# append an item to every list; print out the new lists
my_list.append(3)
list_of_strings.append(3)
list_of_numbers.append(3)

# add every element of one list to another list using extend
my_list.extend(list_of_strings)
print my_list

# try to find an existing element in one of the lists using index; print out the index
print list_of_strings.index('bart')

# try to find a non-existing element in one of the lists using index; comment out when you're done

#my_list.index('bart')

#Don't use index to check if something is in a list b/c the first position will return 0 and will equal false

# try to find an existing element in one of the lists using "in", print out the boolean
print 'bart' in list_of_strings

# remove an element from one of the lists using del
del list_of_strings[1]
print list of strings

# remove the first occurrence of an element in one of the lists using the "remove" function
list_of_strings.remove('bart')

# pop off the last element and save it into a variable; print out the variable
variable=list_of_strings.pop()
print variable

# get a new list with only the first 4 elements of the original list using slicing
a=list_of_numbers[0:4]
print a

# sort the new list using sort
a.sort()
print a

# convert the list to a string
d=','.join(['1','2','3'])
print d

# make the string "ow, ouch, ack" into a list
e='cat,dog,human'.split(',')
print e