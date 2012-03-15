"""
pattern.py
===
Print out a pattern of vertical lines using multiline strings and for loops.
* Create a variable called pattern, set it equal to a multiline string.
* Multiline strings are flexible when it comes to indentation... as long as you're within the multiline string, indentation is treated as part of the string itself, rather than as indented code!
* The pattern should look like this (remember to "escape" the backslashes):
 |||||||||||||||||
 |||||||||||||||||
/////////////////
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 |||||||||||||||||
* Use a for loop to loop 3 times (Hint: generate a list of 3 numbers)
* For each iteration of the loop, print out the pattern variable

Example Output:
 |||||||||||||||||
 |||||||||||||||||
/////////////////
\\\\\\\\\\\\\\\\\
 |||||||||||||||||
 |||||||||||||||||
 |||||||||||||||||
/////////////////
\\\\\\\\\\\\\\\\\
 |||||||||||||||||
 |||||||||||||||||
 |||||||||||||||||
/////////////////
\\\\\\\\\\\\\\\\\
 |||||||||||||||||
"""
pattern = """ |||||||||||||||||
 |||||||||||||||||
/////////////////
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 |||||||||||||||||"""
for x in range(3):
	print pattern