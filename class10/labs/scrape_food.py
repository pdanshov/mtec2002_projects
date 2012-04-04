"""
scrape_food.py
=====
Open a web page that has a list of restaurants.  Print out the list of all of the restaurants on that page.  Use the either of the following urls - zagat or yelp...

Thai restaurants in New York City from Zagat:

http://www.zagat.com/search?text=thai&where%5Bname%5D=New+York+City+&where%5Bid%5D=4294610065&where%5Blat%5D=&where%5Blon%5D=&where%5Blocale%5D=New+York+City&where%5Bradius%5D=

Food near 300 Jay st from yelp:

http://www.yelp.com/search?find_desc=&find_loc=300+jay+st&cflt=food

SETUP
1. You may want to install Firebug:
	http://getfirebug.com/
2. Read the docs again:
	http://docs.python-requests.org/en/latest/user/quickstart/
	http://www.crummy.com/software/BeautifulSoup/bs4/doc/

PROGRAM
1. bring in the requests and beautiful soup modules using import statements
2. create a variable named url... set it equal to the zagat's url or the yelp url
3. use the get method of the requests module to get the url; assign it to a variable named req
4. create a beautiful soup object from the text of the request; assign it to a variable named soup
5. use what you learned in the previous labs to find all of the names of the restaurants
	a. you'll probably need to use firebug to look at the code of the page
	b. you can use find_all on your soup object
	c. iterate through the results...
"""
