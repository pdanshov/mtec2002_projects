"""
get_html.py
=====
Use beautiful soup 4 to parse html strings.

SETUP
1. Read the documentation about the requests module: 
	http://www.crummy.com/software/BeautifulSoup/bs4/doc/
2. Install the requests module:
	pip install beautifulsoup4

USAGE
1.  import bs4												# the beautiful soup module is called bs4
2a. html = "<ul><li class='a'>one</li><li>two</li></ul>" 
2b. soup = bs4.BeautifulSoup() 								# create a beautiful soup object using the html string that was passed in
3.  soup.prettify()                      					# print a formatted version of the string
4.  soup.ul                             					# use the tag name to get that element... in this case, the ul
5.  soup.ul.li												# use the dot operator to descend into nested elements... in this case, li
6.  soup.find_all('li')										# get a list of all the li's
7.  soup.find_all('li', 'class_name')						# get a list of all the li's with class called 'class_name'
8.  soup.ul.li.a.get('href') 								# get the href attribute of the anchor tag

PROGRAM
1. import the requests module
2. create a variable called url, assign a valid url to it, including the http:// part - try http://google.com to begin with
3. using the requests module, call the get(url) function in that module with the url specified in the previous step; assign the result to a variable called req 
4. print out the text and status_code attributes of the req object
5. do the same thing for http://isitchristmas.com
6. do the same thing for http://emerging-media.info/class/
7. try a url that you know is missing; what status code do you get?
8. notice all of the repeated code?  how could we reduce the redundant code?
"""
# import the bs4 module

# create the following html string and assign it to a variable named unordered_list
unordered_list = """
<ul>
<li>one</li>
<li>two</li>
</ul>
""" 
# create a beautiful soup object using the html above

# print out a formatted version of the soup object

# print out the ul tag

# print out the first li in the ul

# print out the string that's between the first li tags

# create the following html string and assign it to a variable named paragraphs
paragraphs = """
<div>
<p>This is a paragraph.</p>
<p>So is <strong>this</strong>.</p>
<p class="foo">This has a <strong>class</strong> attribute!</p>
<p class="foo">This has a class too</p>
</div>
<div>
<p>Nothing to see here!</p>
</div>
"""
# create a beautiful soup object using the html above

# get a list of all of the paragraph tags and assign it to p_tags

# iterate through the list of paragraphs and print them out

# iterate through the list of paragraphs and print out only the part of the paragraph that's a strong tag

# find all of the strong tags; assign to variable named strong_tags

# iterate through the list of strong tags and print out the *string* that's in the strong tags

# find all of the paragraphs that have a class named foo; assign it to a variable named foos

# iterate through the list of paragraphs and print them out

# create the following html string and assign it to a variable named links
links = """
<p>
<a href="http://unicodesnowmanforyou.com">unicode snowman</a>
<a href="http://isitchristmas.com">is it christmas?</a>
</p>
"""

# create a beautiful soup object using the html above

# find all of the a tags and assign it to a variable named a_tags

# iterate through all of the a tags and print out the string representing each link

# iterate through all of the a tags and print out the url by using get on the href attribute


# create the following html and assign it to a variable named mixed
mixed = """
<h1>This is a heading</div>
<div>
	<p>Hello</p>
	<h1>This is another heading</h1>
</div>
<p>
	<a href="http://yahoo.com">yahooz</a>
</p>
<p class="bar">
	<a href="http://google.com">googlez</a>
</p>
<p class="bar">
	<a href="http://duckduckgo.com">duckz</a>
</p>
"""
# create a beautiful soup object using the html above

# only print out the string that's in the h1 that's nested in the div

# print out all of the urls and the *string* associated with them using find_all and a for loop

# print out only the urls that are in links inside paragraph tags with a class bar using find_all and a for loop
