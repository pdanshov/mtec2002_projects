"""
dictionary_1.py
===
1. Dictionaries are lists of key, value pairs (they're like hashes or associative arrays in other languages)
2. The keys and values are separated by colons, the key, value pairs are separated by commas
3. Dictionaries are enclosed by curly braces
4. An empty dictionary is represented by two curly braces with nothing in the middle - {}
5. The most common type of dictionary key is a string, but any immutable type (such as numerical types and tuples) can be keys too!
6. Dictionary keys are case sensitive
7. Dictionary keys are unique; you can't have duplicate keys
8. Values can be accessed by using the dictionary name followed by the key in square brackets
9. Order of the key, value pairs cannot be guaranteed!

Examples:
superstitious_things = {"lucky_charm":"horseshoe", "number":7, "spirit_animal":squid}
superstitious_things["number"]

http://docs.python.org/library/stdtypes.html#mapping-types-dict
"""
# create an empty dictionary, set it to a variable named empty
empty={}

# print out the empty dictionary
print empty

# create a dictionary that describes a pineapple using the keys name, type, and taste
food1={'name':'pinapple','type':'fruit','taste':'sweet'}

# print out the dictionary 
print food1

# create another dictionary that describes a lemon using the keys name, type, and taste
food2={'name':'lemon','type':'fruit','taste':'sour'}

# print out the dictionary 
print food2

# print out the value at key name
print food2['name']
print food2["name"]

# create a new key, color, by  using the new key and assigning it to a variable
food2['color']='yellow'

# print the value at the new key
print food2['color']

# print the dictionary
print food2

# create a dictionary of four of your favorite things using the keys color, food, animal, and number
my_favs={'color':'red','food':'macaroni','animal':'chinchilla','number':923}

# print out the dictionary
print my_favs

# print out your favorite color
print my_favs['color']

# print out your favorite number
print my_favs['number']

# print out your favorite animal
print my_favs['animal']

# print out your favorite animal and color in a sentence
print'my fav animal is %s and my fav color is %s'%(my_favs['animal'],my_favs['color'])

# change your favorite number
my_favs['number']=123

# print out your favorite number
print my_favs['number']	

# try printing an item with a key that doesn't exist
#print my_favs['programming language']

# what happened?  comment out your previous line to continue
# you can also use the get method on a dictionary to retrieve an element, but have a default value if the key doesn't exist
print my_favs.get('programming language','javascript')
my_favs['programming language']='ada'

# just like a list, you can use the del statement to delete a dictionary item
del my_favs['number']

# print out the dictionary after deleting an element
print my_favs

# get the list of keys in your dictionary using the keys method, set it to a variable named my_keys
my_keys=my_favs.keys()

# print out the keys
print my_keys

# loop through the keys using a for loop, print out each element
for k in my_keys:
	print k

# get the list of values in your dictionary using the values method, set it to a variable named my_values
my_values=my_favs.values()

# print out the values
print my_values

# loop through the values using a for loop, print out each element
for x in my_values:
	print x

# get all of the key, value pairs of your dictionary as a list of tuples using the items method; set it to a variable called tuples
tuples=my_favs.items()

# print out this list
print tuples

# loop through the list of tuples using a for loop, print out each tuple
for x in tuples:
	print x