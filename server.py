from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from common import handle_server
from utility import * 

print_banner('SERVER STARTED')

PORT = 31415

server = socket(AF_INET, SOCK_STREAM)


# Bind Address, and listen
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('0.0.0.0', PORT))
server.listen(5)

print("Waiting for client ... ", end='')
(connection, addr) = server.accept()
print("Client connected")

handle_server(connection)

