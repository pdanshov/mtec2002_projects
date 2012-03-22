"""
character_count.py
===
1. Create a function called character_count that takes one parameter called s 
2. Use a for loop to  iterate through all of the characters in the string s
3. Keep track of the number of times a letter appears in the string by using a dictionary
4. The keys of the dictionary should be the letter, the values should be the number of times the letter appears
5. Use the get method so that you can initialize the value to 0 when you first see a letter; assign it to that new key and increment
6. Return the resulting dictionary
7. See section 12.7 in http://openbookproject.net/thinkcs/python/english2e/ch12.html for a big hint!
8. Call character count on a few strings at the end of your program: "tutt", "It's peanut butter jelly time", and "Ecstatic elephants eat easily"
9. Print out the string itself, along with the dictionary of character counts
	For example:
	print "It's peanut butter jelly time"
	print character_count("It's peanut butter jelly time")

Example Output:
tutt
{'u': 1, 't': 3}
It's peanut butter jelly time
{'a': 1, ' ': 4, 'b': 1, 'e': 4, 'i': 1, "'": 1, 'I': 1, 'j': 1, 'm': 1, 'l': 2, 'n': 1, 'p': 1, 's': 1, 'r': 1, 'u': 2, 't': 5, 'y': 1}
Ecstatic elephants eat easily
{'a': 4, ' ': 3, 'c': 2, 'E': 1, 'i': 2, 'h': 1, 'l': 2, 'n': 1, 'p': 1, 's': 3, 't': 4, 'y': 1, 'e': 4}
"""
