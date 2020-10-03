from threading import Thread
from time import sleep
from utility import *
import os

import system

from menu import *

MAX_CONFIRMATIONS = 5
DIAGNOSTIC = False


class Receiver(Thread):
    def __init__(self, socket, server=False):
        Thread.__init__(self)
        self.setDaemon(True)
        self.server = server
        self.socket = socket

    def run(self):
        store_session_banner()

        try:
            while True:
                data = self.socket.recv(2048)
                if len(data) == 0:
                    exit_application()

                text = data.decode()
                print("<<")
                print(text)
                print(">>")
                #If is server:
                if self.server:
                    pass

                     # Check if (handle_command); check if "!file"
                store_message(text)
                response = handle_command(text)

                
                

        except:
            exit_application()

class Sender(Thread):
    def __init__(self, socket, server=False):
        Thread.__init__(self)
        self.setDaemon(True)
        self.socket = socket

    def run(self):
        while True:

            print('>> ')
            text = ''

            try:
                text = input()
            except KeyboardInterrupt:
                exit_application()
            except EOFError:  
                confirm_exit_application()
                print("Continuing...")

            # text = self.socket.send(s.encode())
            if DIAGNOSTIC:
                print('~' + text)
                print('len() => ' + str(len(text)))
                
            if text == ':quit':
                exit_application()

            sent = self.socket.send(text.encode())
            if sent == 0:
                print("SENT 0")
                exit_application()
                #     return


def confirm_exit_application():
  iteration = 0

  while iteration < MAX_CONFIRMATIONS: 
    try:
        system.instrument()
                
        confirm = input('Would you like to Exit? [y\\n]: ')
        if confirm.lower() in {"y", "yes"}:
            exit_application()
    except KeyboardInterrupt:
        exit_application()
    except EOFError:
        print('')
    iteration+=1

def exit_application():
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

"""Handles Commands:                           
    - file :: opens a file-dialog               
    - exec :: allows execution of arbitrary-code"""
def handle_command(msg):

    # Check if Message is *actually* a command!
    # if it starts with "!"
    if msg.startswith("!file"):
        file_path = dialog_query_file()
        print("[Opening File] ... ", end="")
        print(f"|{file_path}|")
        return handle_file_dialog(file_path)


class Server:

    def __init__(self, sender, receiver):
        self.sender = start_send_loop()
        self.receiver = start_receiver_loop()

    def run(self):
        try: 
            while True:
                print('>> ')
                s = input()

                sent = self.socket.send(s.encode())
                if sent == 0:
                    exit_application()
                    return
        except:
            exit_application()        
    
def print_server_diagnostics(server):

    senderThread = server.sender
    print("#"*40)
    print()
    print(f"Thread-Name: {senderThread.getName()}")
    print(f"Is-Daemon: senderThread.isDaemon()")
    print(f"Is-Alive: senderThread.is_alive()")
    print()
    print("#"*40)

    

def store_session_banner():    
    path = "private/conversation.txt"
    storage_append_to_file(path, create_session_banner(0) )

def store_message(text):
    path = "private/conversation.txt"
    storage_append_to_file(path, text)

