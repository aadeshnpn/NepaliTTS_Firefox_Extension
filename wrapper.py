#/usr/bin/python2.7
import subprocess
from subprocess import call

filename="/usr/lib/cgi-bin/tts/run_male.sh"
#call('/bin/bash ', + filename, shell=True)
filename1="/usr/lib/cgi-bin/tts/run.sh"
#cmd = "xterm -hold -e `ls` "
# no block, it start a sub process.
#subprocess.call("cd /usr/lib/cgi-bin/tts/",shell=True)
p = subprocess.Popen(filename1, shell=True)
#subprocess.call("/bin/bash/ " + filename,shell=True)
# and you can block util the cmd execute finish
#p.wait()
# or stdout, stderr = p.communicate()

#import os
#os.system("xterm -hold -e test.sh")