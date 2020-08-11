from threading import Thread
from time import sleep
from utility import *
import os

from menu import *


class Receiver(Thread):
    def __init__(self, socket, server=False):
        Thread.__init__(self)
        self.setDaemon(True)
        self.server = server
        self.socket = socket

    def run(self):
        try:
            while True:
                s = self.socket.recv(2048)
                if len(s) == 0:
                    finish()
                    return
                message = s.decode()
                print("<<")
                print(message)
                print(">>")
                #If is server:
                if self.server:
                     # Check if (handle_command); check if "!file"
                    handle_command(message)
                    store_message(message)

                

        except:
            finish()

class Sender(Thread):
    def __init__(self, socket, server=False):
        Thread.__init__(self)
        self.setDaemon(True)
        self.socket = socket

    def run(self):
        try: 
            while True:
                print('>> ')
                s = input()

                sent = self.socket.send(s.encode())
                if sent == 0:
                    finish()
                    return
        except:
            finish()


def finish():
    print("Connection terminated")
    os._exit(0)

def start_receiver_loop(socket, server=False):
    thread = Receiver(socket, server)
    thread.start()
    return thread

def start_send_loop(socket):
    thread = Sender(socket)
    thread.start()
    return thread

def handle_connection(socket):
    receiver = start_receiver_loop(socket)
    send = start_send_loop(socket)
    receiver.join()
    send.join()

def handle_server(socket):
    receiver = start_receiver_loop(socket, True)
    send = start_send_loop(socket)
    
    receiver.join()
    send.join()

def handle_command(msg):

    # Check if Message is *actually* a command!
    # if it starts with "!"
    if msg.startswith("!file"):
        file_path = dialog_query_file()
        print("[Opening File] ... ", end="")
        print(f"|{file_path}|")

class Server:

    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver

        
    
def print_server_diagnostics(server):

    senderThread = server.sender
    print("#"*40)
    print()
    print(f"Thread-Name: {senderThread.getName()}")
    print(f"Is-Daemon: senderThread.isDaemon()")
    print(f"Is-Alive: senderThread.is_alive()")
    print()
    print("#"*40)

    

def store_message(text):
    path = "private/conversation.txt"
    storage_append_to_file(path, create_session_banner(0) )
    storage_append_to_file(path, text)

