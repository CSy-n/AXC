from socket import socket, AF_INET, SOCK_STREAM
from common import bidirectional
from utility import * 

print_banner('SERVER STARTED')



server = socket(AF_INET, SOCK_STREAM)
server.bind(('0.0.0.0', 31415))
server.listen(5)

print("Waiting for client ... ", end='')
(sock, addr) = server.accept()
print("Client connected")

bidirectional(sock)

