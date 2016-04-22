import fnmatch
import os
import glob
import subprocess
import os.path
import random
import string

# var represents the android .har file we will work with
var = input("Please enter a jar file: ")
rootdir = './Extract_'+var+'/'
#the rootdirectory in which we will work
print (rootdir)
#searching in all the java classes
class encryptAES:
	def encrypt_aes(self):
		filename  = open("EncryptAES.txt",'w')
		sys.stdout = filename
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file = open(p, "r")
				for line in my_file:
					for part in line.split():
						#if the encryption algorithm AES is used the line and th path is printed
						if 'AES' in part:
							print('*'*100)
							print('The line of code in which the string was found',line)
							print('The path of the file in which the string was found',p)
							break
				my_file.close()
				
test=encryptAES()
test.encrypt_aes()