import os
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
#searching in all java files
class nativeCode:
	def native_code(self):
		filename  = open("NativeCode.txt",'w')
		sys.stdout = filename
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file = open(p, "r")
				for line in my_file:
					for part in line.split():
						#searching in the lines of the java code and if the line ends with a semicolon
						#and has the word native we print it
						if part == 'native'and line[-2]==';':
							print (line," - contains native code")
							print('*'*100)
				my_file.close()
				
test=nativeCode()
test.native_code()
