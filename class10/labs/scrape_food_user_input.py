"""
scrape_food_user_input.py
=====
Get user input to interface with zagat or yelp.  For example... using the short form of the zagat url:

http://www.zagat.com/search?text=thai&where[name]=Chicago

...we can substitute any value for the city.  Use user input and string interpolation to construct a new URL.  List the restaurants as you did in the scrape_food exercise.

1. Import the modules that you'll need (requests, bs4)
1. Loop forever
2. Ask for a city
3. Construct a url using that city
4. Use the requests module to get the url
5. Create a beautiful soup object using the text from the result of the request
6. Find all of the names of the restaurants and print them out
7. (OPTIONAL) change the search so that you can enter a different cuisine
8. (OPTIONAL) what other info can you scrape?... output that as well!

Expected Output:
What city plz?
>New York City
Chao Thai
Pure Thai Cookhouse
.
.
.
Beyond Thai Kitchen

What city plz?
>Chicago
Thai Grill & Noodle Bar
Butterfly Sushi Bar & Thai Cuisine
Butterfly Sushi Bar & Thai Cuisine
.
.
.

"""
