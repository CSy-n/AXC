from socket import socket, AF_INET, SOCK_STREAM
from common import bidirectional
from utility import * 

print_banner('SERVER STARTED')

PORT = 31411

server = socket(AF_INET, SOCK_STREAM)
server.bind(('0.0.0.0', PORT))
server.listen(5)

print("Waiting for client ... ", end='')
(sock, addr) = server.accept()
print("Client connected")

bidirectional(sock)

