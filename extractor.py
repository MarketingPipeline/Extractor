import requests
import tarfile
import sys
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile


### Check Python Version - Script works in Python3 only.
if sys.version_info < (3,0,0):
    print(__file__ + 'This package requires Python 3, while Python ' + str(sys.version[0] + ' was detected. Terminating. '))
    sys.exit(1)

##### Menu Options
ans=True
while ans:
    print ("""
    1.Extract Existing Tar.GZ File
    2.Download & Extract Tar.GZ File
    3.Extract Existing ZIP file
    4.Download & Extract ZIP file
    5.Exit/Quit
    """)
    ans=input("What would you like to do? ")
    ### Extract Existing Tar.GZ file
    if ans=="1": 
        pathToTAR = str(input('Insert Path To Tar.GZ file'))
        require1 = "tar.gz"
        if pathToTAR.find(require1) != -1:
         path = str(input('Insert Path To Extract Tar.GZ To: '))
         file = tarfile.open(pathToTAR, mode="r|gz")  ####
         file.extractall(path)
         print("TAR.GZ File has been extracted to ", path)
        else:
         print("\n File not found.")
    ### Download & extract Tar.GZ file
    elif ans=="2":
        downloadurl = str(input("Insert Download URL for TAR.GZ file to extract:"))
        require2 = "http"
        if downloadurl.find(require2) != -1:
          response = requests.get(downloadurl, stream=True)
          file = tarfile.open(fileobj=response.raw, mode="r|gz")
          path = str(input('Insert Path To Extract To: '))
          file.extractall(path)
          print("File has been extracted to ", path)
        else:
         print("\n Not a valid URL ; Did you include http:// or https://?")
    elif ans=="3":
        pathToZIP = str(input('Insert Path To ZIP file'))
        require1 = ".zip"
        if pathToZIP.find(require1) != -1:
         path = str(input('Insert Path To Extract ZIP To: '))
         zipfile = ZipFile(pathToZIP)
         zipfile.extractall(path)
         print("ZIP File has been extracted to ", path)
        else:
         print("\n File not found.")
    ### Download & Extract ZIP file
    elif ans=="4":
        downloadurl = str(input("Insert Download URL for ZIP file to extract:"))
        require2 = "http"
        if downloadurl.find(require2) != -1:
          http_response = urlopen(downloadurl)
          zipfile = ZipFile(BytesIO(http_response.read()))
          path = str(input('Insert Path To Extract To: '))
          zipfile.extractall(path)
          print("ZIP File has been extracted to ", path)
        else:
         print("\n Not a valid URL ; Did you include http:// or https://?")
    ### Exit the script
    elif ans == "5":
      print("\n Exiting Program")
      exit()
    ### Invalid Menu Choice
    elif ans !="":
      print("\n Not Valid Choice Try again") 
