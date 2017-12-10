# Ross Moriwaki
# SystemInfoTool.py
# This tool will grab the hostname of a machine and output to console

import socket

def systemInfoTool():
    print("The hostname is: " + socket.gethostbyaddr(socket.gethostname())[0])  #Works on all machines?

if __name__ == "__main__" :
    systemInfoTool()