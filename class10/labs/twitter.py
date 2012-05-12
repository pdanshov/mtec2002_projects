"""
twitter.py
=====
json docs: http://docs.python.org/library/json.html
Twitter search api docs: https://dev.twitter.com/docs/using-search
The url to perform the search: http://search.twitter.com/search.json?q=%40python
1. import requests and json
2. use requests.get
3. use json.loads to create a dictionary
4. print out the tweets
"""
#geocode for geographic location
#include_entity=true to have tweat entities included for mentions, links, media, and hashtags.
"""
in_reply_to_status_id and in_reply_to_status_id_str are now included
with @replies, allowing you to knowthe replied-to status ID,
which can be looked up using GET statuses/show/:id.
%20geocode=40.77,73.98,50mi (within 50 miles of new york)
"""
import requests
import json

req = requests.get("http://search.twitter.com/search.json?q=%40python")
#print req
#print req.text
data = req.text
tweets = json.loads(data)
#print tweets
print json.dumps(tweets, sort_keys=True, indent=4)