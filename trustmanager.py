import os
import subprocess
import os.path
import random
import string
#var represents the jar file we want to use
var = input("Please enter a jar file: ")
#the rootdirectory will be Extract_var
rootdir = './Extract_'+var+'/'
print (rootdir)


class trustManager:
	def trust_manager(self):
		filename  = open("Security.txt",'w')
		sys.stdout = filename
		#trustmanager_dict. txt contains the words we will be searching for in the code related to security
		with open('trustmanager_dict.txt') as f:
			for line in f:
				word=line
				#the words are saved in parameter word
				print(word)
				#searching in every java file
				for subdir, dirs, files in os.walk(rootdir):
					for file in files:
						p=os.path.join(subdir,file)
						my_file = open(p, "r")
						for line in my_file:
							#if the word is find in the line it will print the line and the path
							if word in line:
								print('The part of code in which the string was found',line)
								print('The path of the file in which the string was found',p)
								break
						my_file.close()
				
test=trustManager()
test.trust_manager()
