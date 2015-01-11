 #!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#@author: Aadeshnpn
import socket,sys
import subprocess
import threading
import time

# Set up the server:
HOST = "192.168.1.19" # Symbolic name meaning the local host
PORT = 4444 # Arbitrary non-privileged port

def ttsLoop():

 # Accept the connection once (for starter)
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    stored_data = ' '
    while True:
        # RECEIVE DATA
        data = conn.recv(1024)
        # PROCESS DATA
        tokens = data.split(' ',1)            # Split by space at most once
        #print tokens
        command = tokens[0]                   # The first token is the command
        #print command
        #reply='Quit'
        if command=='HELO':                    # The client requests the data
            reply = '101'               # Return the stored data
            print reply + "--HELO Command Replied"
            conn.send(reply)
        elif command=='FNAME':                # The client want to store data
            fname = tokens[1]           # Get the data as second token, save it
            if len(fname)==0:
                print "--File name problem. Setting default filename"
                fname="007.txt"
            reply = '102'                      # Acknowledge that we have stored the data
            print reply + "--File name successfuly received"
            conn.send(reply)
        elif command=='DATA':            # Client wants to translate
            stored_data = tokens[1]     # Convert to upper case
            filename=fname+".txt"
            filepath="/usr/lib/cgi-bin/tts/"+filename
            wfile=open(filepath,"w")
            wfile.write(stored_data)
            wfile.close()
            print "--Text data written to file. Calling Nepali TTS Engine for conversion"
            cmd="./runtts.sh "+fname
            p = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # and you can block util the cmd execute finish
            p.wait()
            reply = '103'               # Reply with the converted data
            print reply + "--TTS Conversion successful. Sending the converted sound info"
            conn.send(reply)
        elif command=='QUIT':                 # Client is done
            conn.send('Quit')                 # Acknowledge
            print "--Sound info completed. Quiting the session.."
            #conn.close()
            break                             # Quit the loop
        else:
            reply = 'Unknown command'
            #print reply
            #conn.send('Quit')
            break
            #conn.send(reply)
            # SEND REPLY
        #conn.send(reply)
    #conn.close() # When we are out of the loop, we're done, close
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
(conn, addr) = s.accept()

# Accept the connection once (for starter)
print 'Connected with ' + addr[0] + ':' + str(addr[1])
stored_data = ' '
ttsLoop()
## Have the server serve “forever”:
while True:
    (conn, addr) = s.accept()
    threading.Thread.daemon=True
    threading.Thread(target=ttsLoop).start()
    #ClientThread.start()

