from threading import Thread
from time import sleep
from os import _exit

class ReceiveLoop(Thread):
    def __init__(self, sock):
        Thread.__init__(self)
        self.setDaemon(True)
        self.sock = sock

    def run(self):
        try:
            while True:
                s = self.sock.recv(2048)
                if len(s) == 0:
                    finish()
                    return
                print(">: " + s.decode())
        except:
            finish()

class SendLoop(Thread):
    def __init__(self, sock):
        Thread.__init__(self)
        self.setDaemon(True)
        self.sock = sock

    def run(self):
        try: 
            while True:
                print('> ')
                s = input()
                sent = self.sock.send(s.encode())
                if sent == 0:
                    finish()
                    return
        except:
            finish()

def finish():
    print("Connection terminated")
    _exit(0)

def start_receive_loop(sock):
    thr = ReceiveLoop(sock)
    thr.start()
    return thr

def start_send_loop(sock):
    thr = SendLoop(sock)
    thr.start()
    return thr

def bidirectional(sock):
    receive = start_receive_loop(sock)
    send = start_send_loop(sock)
    receive.join()
    send.join()

