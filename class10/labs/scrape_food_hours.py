"""
scrape_food_hours.py
=====
Print out restaurant names. Follow the link to the detail page, and print out the hours.

1. Get all of the restaurants on this page and print out the title: 'http://www.yelp.com/search?find_desc=&find_loc=300+jay+st&cflt=food'
2. Print out the restaurant name
3. Follow the link to the next page by taking the url from the a tags and making a new request
4. Extract the hours from the next page and print them out

Expected Output:
1. Los Paisanos
Mon-Sat 8 am - 7 pm
Sun 9 am - 5:30 pm
2. Staubitz Market Meats
3. Sahadi's
Mon-Sat 9 am - 7 pm
4. Jesse & Co. Market Place
Mon-Thu 6 am - 2 am
Fri-Sat 6 am - 3 am
Sun 6 am - 1 am
5. Wright & Goebel Wine & Spirits
Mon 5 pm - 10 pm
Tue-Sat 12 pm - 10 pm
Sun 12 pm - 8 pm
"""
