import socketserver

class EchoHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("Got a connection from: {}".format(self.client_address))
        data = b'test'
        while data.decode("utf-8") != '\n':
            data = self.request.recv(2048)
            print("Client sent: {}".format(data.decode("utf-8")))
            self.request.send(data)

server_address = ("0.0.0.0",1337)
server = socketserver.TCPServer(server_address,EchoHandler)
server.serve_forever()