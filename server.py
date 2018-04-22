import socket

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #make address reusable immediately XD

tcpsocket.bind(("0.0.0.0",1337))
tcpsocket.listen(2)  #two clients concurrently

print("Waiting for a client")
(client, (ip,port)) = tcpsocket.accept()
print("Received connection from {}:{}".format(ip,port))
print("Starting echo server")

data = b'test'
while data.decode("utf-8") != '\n':
    data = client.recv(2048)
    print("Client sent {}".format(data.decode("utf-8")))
    client.send(data)

print("Closing Connection")
client.close()

print("Shutting down the server too ")
tcpsocket.close()