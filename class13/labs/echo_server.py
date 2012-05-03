"""
echo_server.py
===
Subclassing BaseRequestHandler gives your a request attribute... that allows you to receive and send data using the request.recv and request.send methods.  There is also a self.client_address list that comes with subclassing BaseRequetHandler.  You must override the handle method to deal with request data.  The handle method gets called when a request is received.

For More info on socket programming:

http://docs.python.org/howto/sockets.html

1.  Import the SocketServer module
2.  Create a class that subclasses (extends/inherits from) SocketServer.BaseRequetHandler, and call it EchoServer.
3.  Override the handle method by defining your own.
4.  In your handle method, get data by calling the recv method on the inherited attribute, self.request.  It takes one argument that specifies the amount of data to read off of the buffer.
5.  Print out this data.
6.  You can also print out the client address: self.client_address 
7.  Call the send method on the inherited request; just send back what's in the data variable.
8.  Check if you script is "__main__".  
9.  If it is, then define host and port variables...
10. Create a new instance of TCPServer as follows - pass in the host and port as a tuple, and the name of your class:
	server = SocketServer.TCPServer((HOST, PORT), EchoServer)
11. Start the server by calling serve_forever on the instance of TCPServer that you just created
"""
import SocketServer
class EchoServer(SocketServer.BaseRequestHandler):
	def handle(self):
		data = self.request.recv(1024)
		print data
		self.request.send(data.upper())
if __name__ == "__main__":
	HOST = "localhost"
	PORT = 9999
	server = SocketServer.TCPServer((HOST, PORT), EchoServer)
	server.serve_forever()
"""
in console

# nc www.google.com 80

# nc localhost 9999
# foo

"""