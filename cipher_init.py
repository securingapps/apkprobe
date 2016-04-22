import fnmatch
import os
import glob
import subprocess
import os.path
import random
import string
import re

# var represents the android .har file we will work with
var = input("Please enter a jar file: ")
rootdir = './Extract_'+var+'/'
#the rootdirectory in which we will work
print (rootdir)
class cipherInit:
	def cypher_init(self):
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file = open(p, "r")
				for line in my_file:
					if ',' in line:
						for part in line.split():
							#searching for cipher.init function
							if 'Cipher' in part and '.<init>' in part or 'cipher.init' in part or 'Cipher.init' in part:
								print('*'*100)
								print('The line of code in which the string was found',line)
								print('The path of the file in which the string was found',p)
								#if found , the second parameter (the name of the public key) will be saved in Output.txt
								str = line
								secret = str[str.find(", ")+2:str.find(")" or ",")]
								with open("Output.txt", "w") as text_file:
									text_file.write(format(secret))
								break
				my_file.close()
					
class keySpec:
	def key_spec(self):
	#reading the public key name
		secret=open("Output.txt").readline().rstrip()
		print ('The name of the public key parameter is: ',secret)
		#searching for it in the java files to check if it is defined as a plain string
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file = open(p, "r")
				for line in my_file:
					#print(line)
					for part in line.split():
						if (secret) in part:
							print('*'*100)
							print('The line of code in which the string was found',line)
							print('The path of the file in which the string was found',p)
				my_file.close()
	
test=cipherInit()
test.cypher_init()
test=keySpec()
test.key_spec()