# Ross Moriwaki
# MacAddressLookup.py
# This file will take a mac address as input and use the macvendors api to find information on the address
import urllib.request

def MacAddressLookup():
    print("Please input the mac address:")
    macAdd = input()
    url = ("http://macvendors.co/api/%s/csv" %macAdd)
    request = urllib.request.Request(url, headers={'User-Agent' : "API Browser"})
    response = urllib.request.urlopen(request)
    data = (response.read().decode()).split("\"")
    print("Information for mac address %s:" %macAdd)
    print("Company: %s" %data[1])
    print("Mac Prefix: %s" %data[3])
    print("Address: %s" %data[5])
    print("Start Hex: %s" %data[7])
    print("End Hex: %s" %data[9])
    print("Country: %s" %data[11])
    print("Type: %s" %data[13])

if __name__ == "__main__":
    MacAddressLookup()