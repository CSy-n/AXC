from socket import socket, AF_INET, SOCK_STREAM
from common import bidirectional


REMOTE_IP = 'localhost'

PORT = 31415



sock = socket(AF_INET, SOCK_STREAM)

print("Connecting to server ... ", end='')

# Connect to server
sock.connect((REMOTE_IP, PORT))

print("Connected")

bidirectional(sock)

print("Sesssion ended")
