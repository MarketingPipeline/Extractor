# What does Extractor do
This is a command line based Python tool that help you extract the following;

- Extract existing TAR.GZ files to your specified folder path. 
- Downloading a TAR.GZ from a URL & extract it to your specified folder path.
- Extract existing ZIP files to your specified folder path. 
- Download a ZIP file from a URL & extract it to your specified folder path.

This script requires <b>Python 3</b>

# Table Of Contents 
- [What does Extractor do](#what-does-extractor-do)
    + [Why was this made](#why-was-this-made)
  * [How to use](#how-to-use)
      * [Extract Existing Tar.GZ File](#extract-existing-targz-file)
      * [Download and Extract Tar.GZ File](#download-and-extract-targz-file)
      * [Extract Existing ZIP File](#extract-existing-zip-file)
      * [Download and Extract ZIP File](#download-and-extract-zip-file)
  * [Add the path to the script on your server](#add-the-path-to-the-script-on-your-server)
    + [Example](#example)





### Why was this made
Originally unable to extract TAR.GZ files normally on a server. And wanted a friendly work around to make life easier & in hopes that this helps someone else with the same or a familar problem. 

## How to use

1. Run script using Python 3. 
(python extractor.py)

2. You will be prompted with five options
 - 1. Extract Existing Tar.GZ File
 - 2. Download & Extract Tar.GZ File
 - 3. Extract Existing ZIP file
 - 4. Download & Extract ZIP file
 - 3. Exit the program


##  Extract Existing Tar.GZ File 

Provide the tar.gz file path to extract tar.gz like the examples below

<b>(/home/username/example/test/geoPHP.tar.gz) </b> < if on Linux

<b>(C:\Users\ExampleUser\Folder\AreYouStillReadingThis\geoPHP.tar.gz) </b> < if on Windows 



##  Download and Extract Tar.GZ File 

Provide a Download URL for the TAR.GZ file. Insert direct link to file like example below. 
(https://phayes.github.io/bin/current/geoPHP/geoPHP.tar.gz)

Provide the folder path you would like to extract  the tar.gz file to as shown in the examples below

<b>(/home/username/extract-folder) </b> < if on Linux

<b>(C:\Users\ExampleUser\Folder\AreYouStillReadingThis) </b> < if on Windows 

## Extract Existing ZIP File 

Provide the .zip file path to extract .zip like the examples below

<b>(/home/username/example/test/Extractor.zip) </b> < if on Linux

<b>(C:\Users\ExampleUser\Folder\AreYouStillReadingThis\Extractor.zip) </b> < if on Windows 




## Download and Extract ZIP File 

Provide a Download URL for the .zip file. Insert direct link to file like example below. 
(https://github.com/MarketingPipeline/Extractor/archive/refs/heads/main.zip)

Provide the folder path you would like to extract  the .zip file to as shown in the examples below

<b>(/home/username/extract-folder) </b> < if on Linux

<b>(C:\Users\ExampleUser\Folder\AreYouStillReadingThis) </b> < if on Windows 





## Add the path to the script on your server

In your .profile etc. add the script to your path to use it whenever you need it!

### Example

     alias extractor='python /home/username/extractor.py'
     
<b> "extractor" </b> is the name you want to use to call the script directly. 

<b> "python" </b> is whatever command you use to call Python3.

<b> "/home/username/extractor.py" is the path to the extractor script
