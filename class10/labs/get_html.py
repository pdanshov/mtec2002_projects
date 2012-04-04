"""
get_html.py
=====
Use the requests module to download the contents of a url into a string in your program.

READING
1. HTTP Methods - http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html
3. HTTP Response Codes - http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
3. HTTP Status Cats- http://httpcats.herokuapp.com/

SETUP
1. Read the documentation about the requests module: 
	http://docs.python-requests.org/en/latest/user/quickstart/
2. Install the requests module:
	pip install requests

USAGE
1. req = requests.get("http://foo.bar") # sends a get request using the specified url
2. req.status_code                      # the response status code returned from the server
3. req.text                             # the actual text of the response

PROGRAM
1. import the requests module
2. create a variable called url, assign a valid url to it, including the http:// part - try http://google.com to begin with
3. using the requests module, call the get(url) function in that module with the url specified in the previous step; assign the result to a variable called req 
4. print out the text and status_code attributes of the req object (see USAGE #2 and #3)
5. do the same thing for http://isitchristmas.com
6. do the same thing for http://emerging-media.info/class/
7. try a url that you know is missing; what status code do you get?
8. notice all of the repeated code?  how could we reduce the redundant code?
"""
