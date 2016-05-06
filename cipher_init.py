import fnmatch
import os
import glob
import subprocess
import os.path
import random
import string
import re
import timing
import sys
# var represents the android .har file we will work with
var = input("Please enter a jar file: ")
rootdir = './Extract_'+var+'/'
#the rootdirectory in which we will work
print (rootdir)
class cipherInit:
	def cypher_init(self):
		filename  = open("CipherInit_"+var+".txt",'w')
		sys.stdout = filename
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file = open(p, "r")
				for line in my_file:
					if ',' in line:
						for part in line.split():
							#searching for cipher.init function
							with open("Output.txt", "w") as text_file:
								if 'Cipher' in part and '.<init>' in part or 'cipher.init' in part or 'Cipher.init' in part:
									print('*'*100)
									print('The line of code in which the string was found',line)
									print('The path of the file in which the string was found',p)
								#if found , the second parameter (the name of the public key) will be saved in Output.txt
								#str = line
								#secret = re.search('((.*)(,|\))(.*)(,|\)))',str)
								#TODO: split and special if for (key) cases
								
								#if secret and secret.group(4).isnumeric()==False:
								#	print ('Match found: ', secret.group(4))
								#	with open("Output.txt", "w") as text_file:
								#		text_file.write(format(secret.group(4)+'\n'))
								#secret2 = line.split(',')[1].lstrip()
									i = line.find(",") + 1
									j = line.find(",",i)
									if i and j:
										print ('Key found: ', line[i:j])
										text_file.write(format(line[i:j])+'\n')
									
									break
				my_file.close()
					
class keySpec:
	def key_spec(self):
	#reading the public key name
		if os.stat("Output.txt").st_size !=0:
			secret=open("Output.txt").readline().rstrip()
			print ('The name of the public key parameter is: >>>> ',secret,'<<<<<')
			#searching for it in the java files to check if it is defined as a plain string
			for subdir, dirs, files in os.walk(rootdir):
				for file in files:
					p=os.path.join(subdir,file)
					my_file = open(p, "r")
					for line in my_file:
						m =re.search('(.*)( |=)("|\')(.*)("|\')',line)
						if (secret[1:]) in line and m:
							print('*'*100)
							print('The line of code in which ',secret,' was found',line)
							print('The path of the file in which ',secret,' was found',p)
					my_file.close()
			else:
				print(secret,' is not a plain string')
					
		else:
			print('No public key parameter found')
test=cipherInit()
test.cypher_init()
#test=keySpec()
#test.key_spec()
