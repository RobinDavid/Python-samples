#! /usr/bin/env python
# -*- coding: utf-8 -*-

HOST = '127.0.0.1'
PORT = 40000

import socket, sys, threading

class ClientThread(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connection = conn
        self.name = self.getName()

    def run(self):
        while 1:
            msgClient = self.connection.recv(1024)
            if msgClient.upper() == "EXIT" or msgClient =="":
                break
            message = "%s> %s" % (self.name, msgClient)
            print message

            for cle in conn_client:
                if cle != self.name:   # do not send the message back
                    conn_client[cle][0].send(message)

        self.connection.close()      # Close socket from server side
        del conn_client[self.name]        # Delete entry in dictionnary
        print "Client %s disconnected." % self.name



# ----- Main thread
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket creation
try:
    mySocket.bind((HOST, PORT)) #Bind of the socket
except socket.error:
    print "Bind of the socket to the address failed."
    sys.exit()
print "Server ready, waiting for requests..."
mySocket.listen(5)

conn_client = {} #creation of the client dictionnary as global var
while 1:
    try:
        connection, address = mySocket.accept() #Wait for an incoming connection

        th = ClientThread(connection) 	#Creation of the client thread
        th.start() 			#Start the thread
        identif = th.getName()		#
        conn_client[identif] = [connection, th]
        print "Client %s connected, IP address %s, port %s." % (identif, address[0], address[1])
        connection.send("You are now connected. Please send your messages") # Welcome message
    except KeyboardInterrupt:
        print "Keyboard Interrupt received !"
        for key in conn_client:
            conn_client[key][1]._Thread__stop()
        mySocket.close()
        sys.exit(0)
