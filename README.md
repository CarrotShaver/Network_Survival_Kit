# Network_Survival_Kit
- This repo contains several python scripts for Python 3+
- These scripts serve as various standalone tools for networking

1. **System Info Tool** - This tool will grab the hostname of the currently used machine
    - Output will be the domain name of the current machine
2. **IP Mapping Tool** - This tool will return the corresponding IP address of any domain entered
    - This tool asks for user input of a domain name
    - Will output all known IPs associated to that domain name
    - Contains error handling
3. **Port Scanner Tool** - This tool will scan for open ports on any domain or IP and return a report when completed.
    - This tool asks for a domain or IP as input, as well as the range of ports to be scanned
    - Scans the ports with a 1/4 second timeout for connections
        - Output list is in the form of "Port ###: OPEN"
    - Contains error handling
4. **Threaded Port Scanner Tool** - This tool is identical to the Port Scanner Tool, but implements threading
    - Scans are approximately 50x faster
    - Can edit to allow for a longer timeout for more accurate port scans
5. **Mac Address Lookup Tool** - This tool will return information on mac addresses
    - This tool will ask the user for a mac address
    - Makes a call to the macvendors api to return a list of information
    - Will not work on Python 2
