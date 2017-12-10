# Ross Moriwaki
# Last Updated: 12/9/17
# ThreadedPortScannerTool.py version:1.0
# This tool will scan an IP/domain for open ports and implements threading for faster scans

import socket
import threading
from queue import Queue
from datetime import datetime
import sys

def checkSocket(jobs):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create the socket object for accessing ports
        s.settimeout(0.25)
        result = s.connect_ex((remoteIP, jobs))
        if result == 0:  # For each port, print if port is open
            print("Port {}: OPEN".format(jobs))
        s.close()
    except socket.error:
        print("Error: Could not connect to %s.  Please run and try again." % remoteDomain)
        sys.exit()


def threader():
    while True:
        jobs = q.get()
        checkSocket(jobs)
        q.task_done()


print_lock = threading.Lock()   # Puts lock on the print so that all output is thread-safe
q = Queue()     # Queue for storing threads

# Creating thread objects
for x in range(50):
    t = threading.Thread(target=threader)   # Creates thread object 't'
    t.daemon = True     # Specifies that the thread is a daemon, will die when main dies
    t.start()       # Begins thread


print("Enter the IP/domain to scan: ")
remoteDomain = input()
try:
    remoteIP = socket.gethostbyname(remoteDomain)   # Converts the domain/IP to definitely be an IP
except socket.gaierror:
    print("Error: No such domain/IP exists!  Please check the domain and try again!")
    quit()


print("You will now specify what range of ports you want to scan between 0 - 65535")
print("Note: The default well-known ports range from 0 - 1023")
# Long error check for input of ports
while True:
    while True:
        try:
            print("Starting port:")
            startPort = int(input())
            break
        except ValueError:
            print("Error: Value entered was not an integer!")
    while True:
        try:
            print("Ending port:")
            endPort = int(input())
            break
        except ValueError:
            print("Error: Value entered was not an integer!")
    if endPort < startPort:
        print("Error: Starting port must be less than ending port")
    if startPort < 0:
        print("Error: Starting port must be 0 or greater")
    if endPort > 65535:
        print("Error: Ending port must be 65535 or less")
    else:
        break

print("#" * 40)
print("Scanning host for open ports, please wait...")
print("#" * 40)

startTime = datetime.now()  # Begin script timer

# For loop to create the job queue for threads to work on
for jobs in range(startPort, endPort+1):
    q.put(jobs)

q.join()

endTime = datetime.now() # Script finished successfully, log end time of scan
totalTime = endTime-startTime

print("Scanned %s ports %s to %s" %(remoteDomain, startPort, endPort))
print("Scan start time: %s. Scan end time: %s." %(startTime, endTime))
print("Scan completed in: %s" %totalTime)


