### Introduction

This will be used to assess how security elements are implemented in Android applications. The project is based on OWASP top 10 Mobile Risks 

### Usage

The programming language used is Python 3.3 which can be downloaded from this site: https://www.python.org/download/releases/3.3.0/.
In order to verify the security related implementation, the APK of the Android application is needed.

Open PowerShell and verify if Python is correctly istalled and functional by simply typing python:

Something similar to this should appear:
Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
Afterwards type exit() so that you can run the script.

Also to be sure everything will run accordingly add to the Path variable the following:
This is an example: C:\Python33\;C:\ProgramFiles\7-Zip\;C:\Program Files\Java\jdk1.7.0_51\bin;

Also on the root directory make sure you have the jd-core.jar provided.

The script we are using is called extract.py. In PowerShell just change the directory to the directory in which this script is along with the dependecies and the APK file(s). Afterwards write 'python extract.py'.
The first thing the script does is obtaining the JAR file from the APK file. For this we used the enjarify tool which can be found online at https://github.com/google/enjarify. In this moment it will search the rootdirectory for all the APK files.

After you have the JAR file, it will extract the java classes contained in this JAR file to a folder called 'Extract_nameofjar'.

The first 2 classes will verify the percentage of obfuscated files and folders contained in the Extract_ folders. It will print the outcome in 2 different text files, 1 for the file obfuscation percentage and one for the folder obfuscation percentage.

The next class will unzip the APK file and the content will be saved in 'Unzip_nameoffile' folders. It will verify afterwards if the folder contains the lib folder with '.so' files and also if the java classes contain native code. 

The next class will conduct a search in the java class for Secure Socket Layer related terms that can be found in trustmanager_dict.txt. As an output we will have the line in which the term was found and the path for further analyzing the content. The output is printed in 'Security_nameofjar' folders.

The next 3 classes are related to encryption methods. A search is performed in the java classes of the jar to find symmetric encryption methods (AES), hash functions (SHA1,SHA256,MD5), functions related to cryptography (cipher.init, doFinal) and the path in which these terms were found.

Update: The new version will print the outcome of every analysis to Analyzefile_'name of jar'
