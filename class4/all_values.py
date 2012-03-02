"""
For Loops - Printing Out All Values...
=====
Prep:
Create a list of ints from 0 to 9 called numbers by using the range function.
Create a list of strings called animals with the words "zebra", "lion", and "giraffe"

1. Using a for loop, print out all of the values in the numbers list
"""
numbers=range(10)
animals=['zebra','lion','giraffe']
for x in numbers:
	print x
"""
	Example Output:
		0
		1
		2
		3
		4
		5
		6
		7
		8
		9

2. Using a for loop, print out all of the values in the animals list
"""
for x in animals:
	print x
"""
	Example Output:
		zebra
		lion
		giraffe

3. Using a for loop, print out the lengths of all of the animal names
"""
for x in animals:
	print len(x)
"""
	Example Output:
		5
		4
		7

4. Using a for loop, print out all of the values in the numbers list, but with each number multiplied by 10
"""
for x in numbers:
	print x*10
"""
	Example Output:
		0
		10
		20
		30
		40
		50
		60
		70
		80
		90

5. Using a for loop, print out all of the values in the animals list in a sentence that says "oh noez, a [ANIMAL NAME]!"
"""
for x in animals:
	print 'oh noez, a %s!' %x
"""
	Example Output:
		oh noez, a zebra!
		oh noez, a lion!
		oh noez, a giraffe!

INTERMEDIATE

6. Add "aardvark" and "eagle"  to the list of animals using append.  Loop through the list of animals again and say "oh noez, a [ANIMAL NAME]!".  However, since we would like to be grammatically correct, use the correct article - "a" or "an".  Use "an" if the name of an animal starts with a vowel.
"""
animals.append('aardvark')
animals.append('eagle')
vowels=['a','e','i','o']
for x in animals:
	if x[0] in vowels: # x[0] is the index of the string (position of char in string)
		print 'oh noez, an %s!'%x
	else:
		print 'oh noez, a %s!'%x

# figure out why 
# if x.startswith(vowels):
# doesn't work

"""
	Example Output:
		oh noez, a zebra!
		oh noez, a lion!
		oh noez, a giraffe!
		oh noez, an aardvark!
		oh noez, an eagle!

"""
