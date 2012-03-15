"""
dictionaries_again.py
===
Some methods and statements that you can use on dictionaries:
1. {}                               	# an empty dictionary
2. d = {"shape":"square", "sides":4}	# create a dictionary
3. d["shape"]							# retrieve value at key "shape"
4. d["new_key"] = "some value"			# create a new key with some value
5. d.get("area", 0) 					# retrieve value at key "area", but default to value if key doesn't exist
6. d.keys() 							# returns list of all keys in dictionary
7. d.values() 							# returns a list of all values in a dictionary
8. d.items() 							# returns a list of all items in a dictionary
9. del d["sides"]						# deletes the item at key "sides"

Example Output:
35
0
['bob', 'sally']
[21, 35]
[('bob', 21), ('sally', 35)]
{'eve': 23, 'sam': 39}
"""
# create an empty dictionary named scores (#1)

# add a key called "bob" to it, and set it equal to 21 (#4)

# add a key called "sally" to it, and set it equal to 35 (#4)

# print the value at the key named sally (#3)

# use the get method to retrieve the value for a non-existent key named alice, default it to 0 (#5); assign to a variable named alice_score

# print out alice_score

# print out all of the keys in the dictionary (#6)

# print out all of the values in the dictionary (#7)

# print out all of the key/value pairs in the dictionary as a list of tuples (#8)

# create a dictionary called more_scores, this time with the following key/value pairs... "eve" - 23, "sam" - 39 (#2)

# print out more_scores
