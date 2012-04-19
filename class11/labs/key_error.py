"""
key_error.py
=====
In this program, we'll revisit the translation program we created earlier.  
However, instead of if-statements, we'll use a dictionary and a try/except
block to implement our program.

Hint: this exercise is similar to class10/labs/ascii_times.py 

1. Create a dictionary named d with the following key/value pairs - "dog":"perro","cat":"gato"
2. Loop forever
3. Get input from the user
4. Use the user input to retrieve the translated value out of the dictionary
5. Run your program - check that it works with cat and dog
6. Try a word that is not a key in your dictionary - like giraffe
7. What exception occurs?
8. Use a try/except block to catch the error and print out "I don't know how to translate that"

Example output:
word to translate, please
>dog
perro
word to translate, please
>cat
gato
word to translate, please
>giraffe
I don't know how to translate that
word to translate, please
>
"""
d = {"dog":"perro", "cat":"gato"}
while True:
	word = raw_input("Enter a word to translate\n> ").lower()
	try:
		print d[word]
	except KeyError:
		print "I don't know how to say that."