# Ross Moriwaki
# PortScannerTool.py
# This tool will scan the target IP's open ports

import socket
from datetime import datetime     # Will be used to track runtime of scan
import subprocess       # Will be used to put processes on a thread
import sys

def PortScannerTool():
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


    try:
        for ports in range(startPort, endPort+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create the socket object for accessing ports
            s.settimeout(0.25)
            result = s.connect_ex((remoteIP, ports))
            if result == 0:     # For each port, print if port is open
                print("Port {}: OPEN".format(ports))
            s.close()
    except socket.error:
        print("Error: Could not connect to %s.  Please run and try again." %remoteDomain)
        sys.exit()

    endTime = datetime.now() # Script finished successfully, log end time of scan
    totalTime = endTime-startTime

    print("Scanned %s ports %s to %s" %(remoteDomain, startPort, endPort))
    print("Scan start time: %s. Scan end time: %s." %(startTime, endTime))
    print("Scan completed in: %s" %totalTime)

if __name__ == "__main__":
    PortScannerTool()