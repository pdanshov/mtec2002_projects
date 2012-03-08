"""
equal_to_three_while.py
===
1. Create a list of strings called animals...  "dog", "zebra", "giraffe", "elephant", "cat", "lion", "bear"
2. Create an empty list called three_letter_words
3. Use a while loop to append all of the three letter words from animals to three_letter_words 
4. Print out the animals list and the three_letter_words list

Example Output:
All words: ['dog', 'zebra', 'giraffe', 'elephant', 'cat', 'lion', 'bear']
Three letter words: ['dog', 'cat']
"""
animals=['dog','zebra','giraffe','elephant','cat','lion','bear']
three_letter_words=[]
count=0
while count<len(animals):
	if len(animals[count])==3:
		three_letter_words.append(animals[count])
	count+=1
print animals
print three_letter_words