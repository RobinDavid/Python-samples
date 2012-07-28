#! /usr/bin/env python
# -*- coding: utf-8 -*-

HOST = '127.0.0.1'
PORT = 40000

import socket, sys, threading, time

class ThreadReception(threading.Thread):
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.connection = conn

    def run(self):
        while 1:
            r_mess = self.connection.recv(1024)
            print "*" + r_mess + "*"
            if r_mess == '' or r_mess.upper() == "EXIT": #if the user recieve exit then quit
                break
        #Thread terminate here + kill send thread
        th_E._Thread__stop()
        self.connection.close()
        print "Client stopped, Connection interrupted."


class ThreadEmission(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connection = conn

    def run(self):
        while 1:
            s_mess = raw_input()	#stuck here will the user haven't write something
            self.connection.send(s_mess)
            if s_mess.upper() == "EXIT": #if the user type exit then quit the client
                break
        th_R._Thread__stop()
        self.connection.close()
        print("Connection terminated")


# Main thread
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
count = 0
while 1:
    try:
        connexion.connect((HOST, PORT))
        print "Connection establishd with the server."
        break
    except socket.error:
        count += 1
        if count <= 5:
            print "Connection failure. Next attempt 5 secondes"
            time.sleep(5)
        else:
            sys.exit()

th_E = ThreadEmission(connexion) #Create thread
th_R = ThreadReception(connexion)
th_E.start() #start them
th_R.start()
import time
while th_E.isAlive() and th_R.isAlive():
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print "Client stopped. Ctrl+C pressed !"
        th_E._Thread__stop()
        th_R._Thread__stop()
        sys.exit(0)
