from socket import socket, AF_INET, SOCK_STREAM
from common import handle_connection


REMOTE_IP = 'localhost'
#REMOTE_IP = '180.150.115.162'

PORT = 31415


client = socket(AF_INET, SOCK_STREAM)

print("Connecting to server ... ", end='')

# Connect to server
client.connect((REMOTE_IP, PORT))

print("Connected")

handle_connection(client)

print("Sesssion ended")
