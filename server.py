#!/usr/bin/python2.7
#@author: Aadeshnpn
#encoding : UTF-8
import socket,sys,threading,time
import subprocess,codecs

filename="/usr/lib/cgi-bin/tts/run_male.sh"
HOST = "127.0.0.1"# Symbolic name meaning the local host
PORT = 4444    # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
i=0
print 'Socket created'
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error code: ' + str(msg[0]) + 'Error message: ' + msg[1]
    sys.exit()
print 'Socket bind complete'

def startThreads(s):
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    stored_data = ' '
    while True:
        # RECEIVE DATA
        data = conn.recv(2048)
        i=i+1
        # PROCESS DATA
        tokens = data.split(' ',1) # Split by space at most once
        print data
        command = tokens[0]                   # The first token is the command
        if command=='HELO':                    # The client requests the data
            #reply = stored_data
            reply='100'               # Return the stored data
        elif command=='STORE':                # The client want to store data
            stored_data = tokens[1]           # Get the data as second token, save it
            reply = '101'                      # Acknowledge that we have stored the data# Reply with the converted data
        elif command=='QUIT':                 # Client is done
            conn.send('Quit')                 # Acknowledge
            break                             # Quit the loop
        else:
            reply = '505'

        # SEND REPLY
        conn.send(reply)
    conn.close() # When we are out of the loop, we're done, close
    
    if i>=1000:
        i=0
    if len(stored_data) >=0:
        file_name="text"+str(i)+".txt"
        f=codecs.open(file_name,"w")
        f.write(stored_data)
        f.close()
        p = subprocess.Popen(filename, shell=True)
    else:
        print "Data not given\n"
        
s.listen(1)
print 'Socket now listening'
(conn, addr) = s.accept()
while conn is not None:
    # Accept the connection once (for starter)
    threading.Thread(startThreads(s)).start()
    s.listen(1)
    print 'Socket now listening'
    (conn, addr) = s.accept()


