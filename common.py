from threading import Thread
from time import sleep
from utility import *
import os

class Receiver(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.setDaemon(True)
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
                store_message(message)

        except:
            finish()

class Sender(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.setDaemon(True)
        self.socket = socket

    def run(self):
        try: 
            while True:
                print('>> ')
                s = input()
                store_message(s)
                sent = self.socket.send(s.encode())
                if sent == 0:
                    finish()
                    return
        except:
            finish()

def finish():
    print("Connection terminated")
    os._exit(0)

def start_receive_loop(socket):
    thread = Receiver(socket)
    thread.start()
    return thread

def start_send_loop(socket):
    thread = Sender(socket)
    thread.start()
    return thread

def handle_connection(socket):
    receive = start_receive_loop(socket)
    send = start_send_loop(socket)
    receive.join()
    send.join()


def store_message(text):
    storage_append_to_file("private/conversation.txt", text)

    

