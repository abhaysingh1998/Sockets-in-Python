import SocketServer
import SimpleHTTPServer

class RequestHandlerClass(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/admin':
            self.wfile.write("This is only for admins !\n")
            self.wfile.write(self.headers)
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpserver = SocketServer.TCPServer(('',10000), RequestHandlerClass)
httpserver.serve_forever()