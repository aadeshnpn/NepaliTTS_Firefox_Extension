#!/usr/bin/python2.7
#@author: Aadeshnpn

import socket,sys

HOST = "127.0.0.1"# Symbolic name meaning the local host
PORT = 80    # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error code: ' + str(msg[0]) + 'Error message: ' + msg[1]
    sys.exit()
print 'Socket bind complete'
s.listen(1)
print 'Socket now listening'
# Accept the connection once (for starter)
(conn, addr) = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])
stored_data = ' '
while True:
    # RECEIVE DATA
    data = conn.recv(1024)

    # PROCESS DATA
    tokens = data.split(' ',1)            # Split by space at most once
    command = tokens[0]                   # The first token is the command
    if command=='GET':                    # The client requests the data
        reply = stored_data               # Return the stored data
    elif command=='STORE':                # The client want to store data
        stored_data = tokens[1]           # Get the data as second token, save it
        reply = 'OK'                      # Acknowledge that we have stored the data
    elif command=='TRANSLATE':            # Client wants to translate
        stored_data = stored_data.upper() # Convert to upper case
        reply = stored_data               # Reply with the converted data
    elif command=='QUIT':                 # Client is done
        conn.send('Quit')                 # Acknowledge
        break                             # Quit the loop
    else:
        reply = 'Unknown command'

    # SEND REPLY
    conn.send(reply)
conn.close() # When we are out of the loop, we're done, close