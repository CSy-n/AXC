from socket import socket, AF_INET, SOCK_STREAM
from common import bidirectional

REMOTE_IP = 'localhost'

sock = socket(AF_INET, SOCK_STREAM)
print("Connecting to server ... ", end='')
sock.connect((REMOTE_IP, 31415))
print("Connected")

bidirectional(sock)

print("Sesssion ended")
