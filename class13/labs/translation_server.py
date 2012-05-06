"""
translation_server.py
===
Using your spanish module, translate the data sent from the client into spanish and send it back
"""
import SocketServer
import spanish
class EchoServer(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        translation = spanish.to_spanish(data.lower().rstrip())
        self.request.send(translation)
if __name__ == "__main__":
    HOST = "localhost"
    PORT = 9999
    server = SocketServer.TCPServer((HOST, PORT), EchoServer)
    server.serve_forever()