# Ross Moriwaki
# IPMappingTool.py
# This tool will retrieve a domain input from a user and attempt to retrieve the corresponding IP


import socket

def IPMapppingTool():
    print("Enter domain to retrieve domain's IP: ")
    try:
        targetDomain = input()  # Prompt user for the hostname and save as variable
        print("The IPs of %s are: "%targetDomain)  #use socket to retrieve IP
        ipv4 = socket.gethostbyname_ex(targetDomain)
        for items in ipv4:
            print(items)
    except socket.gaierror:
        print("Error: No such domain exists!  Please check the domain and try again!")

if __name__ == "__main__":
    IPMapppingTool()
