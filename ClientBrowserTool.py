# Ross Moriwaki
# ClientBrowserTool.py
# This tool will fetch the html of a domain and save the file to be viewed as a .txt
# This tool will only work with Python 3.4 and above due to the urllib changes from 2.7

import urllib.request
import sys

def ClientBrowserTool():
    try:
        print("Please enter url in the http:// format:")
        url = input()
        urlRead = urllib.request.urlopen(url).read()
    except ValueError:
        print("Error: Invalid url type.  Please run again.")
        sys.exit()


    print("Writing html to file htmlFile.txt:...")
    print("Html: %s" %urlRead)

    htmlFile = open("htmlFile", 'w')
    htmlFile.write("%s" %urlRead)
    htmlFile.close()

if __name__ == "__main__":
    ClientBrowserTool()
