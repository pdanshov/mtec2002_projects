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
import requests
import bs4
import re

url = "http://www.yelp.com"

#fullpath = url + path

req = requests.get("http://www.yelp.com/search?find_desc=&find_loc=581+ovington+ave&cflt=food")
soup = bs4.BeautifulSoup(req.text)
rests = soup.find_all('a', id = re.compile("bizTitleLink.*"))
print ''

for r in rests:
    print r.string
    #if r.has_key("href"):
    #    print r["href"]
    h = bs4.BeautifulSoup(requests.get((url+r["href"])).text).find_all('p', "hours")
    a = bs4.BeautifulSoup(requests.get((url+r["href"])).text).find_all("span", "street-address")
    for x in h:
        print "   "+x.string
    for x in a:
        print "   "+x.string
    """
    for h in bs4.BeautifulSoup(requests.get((url+r["href"])).text).find_all('p', "hours"):
        print "   "+h.string
    for a in bs4.BeautifulSoup(requests.get((url+r["href"])).text).find_all("span", "street-address"):
        print "   "+a.string
    """
    #print "".join(str(t) for t in ((bs4.BeautifulSoup(requests.get((url+r["href"])).text).find_all("p", "hours")))
    #print l.string
    print ''
    