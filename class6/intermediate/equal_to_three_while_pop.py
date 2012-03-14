"""
equal_to_three_while_pop.py
===
1. Create a list of strings called animals...  "dog", "zebra", "giraffe", "elephant", "cat", "lion", "bear"
2. Create an empty list called three_letter_words
3. Use a while loop to append all of the three letter words from animals to three_letter_words 
4. Don't use a count variable; instead, test for an empty list and the list method, pop()
5. Print out the original animals list and the three_letter_words list
6. Notice what happened to the original list!


Example Output:
Original list: []
Three letter words: ['cat', 'dog']
"""
animals=['dog','zebra','giraffe','elephant','cat','lion','bear']
three_letter_words=[]
while len(animals)!=0:
	if len(animals[len(animals)-1])==3:
		three_letter_words.append(animals.pop(len(animals)-1))
	else:
		animals.pop(len(animals)-1)
print animals
print three_letter_words

# while animals:
#	a = animals.pop()
#	if (a)==3:
#		three_letter_words.append(a)
#return three_letter_words

"""
animals=['dog','zebra','giraffe','elephant','cat','lion','bear']
three_letter_words=[]
while len(animals)!=0:
	if len(animals[0])==3:
		three_letter_words.append(animals.pop(0))
	else:
		animals.pop(0)
print animals
print three_letter_words
"""