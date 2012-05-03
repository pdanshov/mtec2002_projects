"""
shout.py
===
1. Import your myutils module.
2. Import the sys module.
3. Use the sys module to get arguments form the commandline (sys.argv[1], etc).
4. Call shout (remember to use the module name as the prefix) using the commandline arguments.
5. (Intermediate)... Hint: you'll need to get two commandline arguments separated by space if your shout function takes two paramters
"""
import myutils
import sys
try:
	print myutils.shout(sys.argv[1], int(sys.argv[2]))
except IndexError:
	print myutils.shout(sys.argv[1], 1)