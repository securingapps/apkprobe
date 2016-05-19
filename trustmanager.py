import os
import subprocess
import os.path
import random
import string
import timing
import sys
#var represents the jar file we want to use
var = input("Please enter a jar file: ")
#the rootdirectory will be Extract_var
rootdir = './Extract_'+var+'/'
print (rootdir)


class trustManager:
	def trust_manager(self):
		filename  = open("Security_"+var+".txt",'w')
		sys.stdout = filename
		with open('trustmanager_dict.txt') as f:
			l = f.read()
			words = l.split()
			for word in words: 
				print(word)
				#the words are saved in parameter word
				for subdir, dirs, files in os.walk(rootdir):
					for file in files:
						p=os.path.join(subdir,file)
						my_file = open(p, "r")
						for line in my_file:
							#if the word is find in the line it will print the line and the path
							for part in line.split():
								if word in part:
									print('The part of code in which ',word,' was found',line)
									print('The path of the file in which ',word,' was found',p)
									break
						my_file.close()
				
				
				
				

test=trustManager()
test.trust_manager()
