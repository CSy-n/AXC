from socket import socket, AF_INET, SOCK_STREAM
from common import bidirectional

REMOTE_IP = '0.0.0.0'
#REMOTE_IP = '180.150.115.162'
PORT = 31411

sock = socket(AF_INET, SOCK_STREAM)
print("Connecting to server ... ", end='')
sock.connect((REMOTE_IP, PORT))
print("Connected")

bidirectional(sock)

print("Sesssion ended")
