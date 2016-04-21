import subprocess
import fnmatch
import os
#colorama is used for printing a coloured string in command line
from colorama import init
import subprocess
import os.path
import random
import sys
init()
# var represents the android .har file we will work with
var = input("Please enter a jar file: ")
rootdir = './Extract_'+var+'/'
#the rootdirectory in which we will work
print (rootdir)

class isFolderObfuscated:
	def obf_folders(self):
		filename  = open("IsFolderObfuscated.txt",'w')
		sys.stdout = filename
		# number of folders in the rootdirectory
		count = 0
		#number of obfuscated folders
		obfuscated = 0
		#searching for all the folders in th rootdirectory
		for subdir, dirs, files in os.walk(rootdir):
			for name in dirs:
				count+=1 #counting the folders
				if name.islower(): #verifying if the name is lowercase
					for i in range(0,len(name)):
						#verifying if the name contains more of the same letter
						if i+2<=(len(name)-1) and name[i] == name[i+1] == name[i+2]:
							obfuscated+=1 #no. of obfuscated folder name increases
							print ('Obfuscated folder name = ',name)
							break
						elif i ==0==len(name)-1: # verrifying if the name of a folder contains just 1 letter
							obfuscated+=1 #no. of obfuscated folder name increases
							print ('Obfuscated folder name = ',name)
		print('Total number of folders = ',count)
		print('No. of obfuscated folders = ', obfuscated)
		#the percentage of obfuscated folders => number of obfuscated folders divided by the total number of folders
		obfuscation_percentage = obfuscated/count*100
		print ('Obfuscation percentage',obfuscation_percentage, '%')
		#if percentage under 33% => not good
		if obfuscation_percentage < 33:
			print('\033[31m' + 'Folder names are not obfuscated')
		#if percentage over 33% but under 66% => better than nothing
		elif 33<obfuscation_percentage < 66:
			print ('Folder names are not obfuscated enough')
		else:
		#if percentage above 66% => good enough
			print('\033[32m' + 'Folder names are obfuscated')
			
test=isFolderObfuscated()
test.obf_folders()
