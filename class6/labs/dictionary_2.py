"""
dictionary_2.py
===
Some methods and statements that you can use on dictionaries:
1. d = {"shape":"square", "sides":4}	# create a dictionary
2. d["shape"]						# retrieve value at key "shape"
3. d.get("area", 0) 				# retrieve value at key "area", but default to value if key doesn't exist
4. d.keys() 						# returns list of all keys in dictionary
5. d.values() 						# returns a list of all values in a dictionary
6. d.items() 						# returns a list of all items in a dictionary
7. del d["sides"]					# deletes the item at key "sides"
8. {}								# an empty dictionary

You should see something similar to this output after you run the program:
{'number_of_teeth': 100, 'first_name': 'joe', 'last_name': 'versoza', 'eye_color': 'black', 'favorite_food': 'ice cream'}
ice cream
joe has 100 teeth
{'number_of_teeth': 100, 'first_name': 'joe', 'last_name': 'versoza', 'eye_color': 'black', 'favorite_food': 'chocolate'}
{'number_of_teeth': 100, 'first_name': 'joe', 'last_name': 'versoza', 'favorite_food': 'chocolate'}
['number_of_teeth', 'first_name', 'last_name', 'favorite_food']
number_of_teeth
first_name
last_name
favorite_food
[100, 'joe', 'versoza', 'chocolate']
[('number_of_teeth', 100), ('first_name', 'joe'), ('last_name', 'versoza'), ('favorite_food', 'chocolate')]
{'number_of_teeth': 100, 'first_name': 'joe', 'last_name': 'versoza', 'favorite_food': 'chocolate', 'hours_of_sleep': 4}
"""
# create an empty dictionary, set it to a variable named empty

# print out the empty dictionary

# create a dictionary about yourself with the follow keys: first_name, last_name, favorite_food, eye_color, and number_of_teeth; assign it to a variable called person 

# print out the dictionary

# print out your favorite_food

# print out your your first_name and your number_of_teeth using the dictionary you created in a sentence... example: "Joe has 100 teeth"

# change your favorite food

# print out your dictionary

# try printing an item with a key that doesn't exist, like "hair_color"

# what happened?  comment out your previous line to continue

# use the get method to get "hair_color", but default to "green" as the value; assign to a variable called hair

# just like a list, you can use the del statement to delete a dictionary item; delete the key and value at "eye_color"

# print out the dictionary after deleting an element

# get the list of keys in your dictionary using the keys method, set it to a variable named my_keys

# print out the keys

# loop through the keys using a for loop, print out each element

# get the list of values in your dictionary using the values method, set it to a variable named my_values

# print out the values

# get all of the key, value pairs of your dictionary as a list of tuples using the items method; set it to a variable called tuples

# print out this list

# create a new key called hours_of_sleep by using the new key and setting it equal to a value

# print out the person dictionary again
