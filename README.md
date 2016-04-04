### Introduction

This will be a tool to verify the how secure is an android application using the apk. It is being built based on OWASP top 10 Mobile Risks 

### Usage

The scripts are written in python and can be used from Power Shell. I am using Python 3.3.
After obtaining the apk file I used the enjarify tool which can be found online at https://github.com/google/enjarify to obtain the jar file for my application.
This is done in extract.py so simply writing 'python extract.py' will ask for an apk file that should be in the folder with the script. The script afterwards will use the enjarified file to extract the folder and java classes. This for the moment is hardcoded and extract.py must be edited to extract the files from the desired jar.

The first tests were conducted on how obfuscated the folders and java files are. For this you can type 'python IsObfuscated.py' and 'python isFolderObfuscated.py' to obtain the percentage of obfuscated elements. The test1.py and test2.py contain unit tests for the obfuscation checks.

TODO: Check for native code in the java files and for the lib library with .so files

TODO: Check that method names belong to the English dictionary

The second tests were conducted on  the Secure Socket Layer and at the moment we are just verifying the content of the java files to see wheter they contain strings such as : trustmanager, getPeerCertificates, checkServerTrusted etc.

To be continued...

