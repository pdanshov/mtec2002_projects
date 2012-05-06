"""
echo_client.py
===
1.  Import the socket module
2.  Define two variables that hold host and port
3.  Create a socket by using the socket method in the socket module, pass in socket.AF_INET and socket.SOCK_STREAM (SOCK_STREAM means a TCP socket):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
4.  Use the connect method on your socket object... pass in a tuple with the specified host and port.
5.  Send data by calling the send method on the socket object - send a string terminated by a new line.
6.  Receive data by calling the recv method, and passing in the max size of the data to be read.
7.  Print the data received.
8.  Close the socket object by calling close on it.
"""
import socket
host = "localhost"
port = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send("String terminated by newline\n")
print client.recv(150)
client.close()