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

class isObfuscated:
	def obf_files(self):
		filename  = open("IsObfuscated.txt",'w')
		sys.stdout = filename
		count = 0 #total number of java files
		obfuscated = 0 #total number of obfuscated files
		not_obfuscated = 0 #total number of non-obfuscated files
		#searching in all subfolders
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				if(fnmatch.fnmatch(file, '*.java')):
					#counting the number of java files
					count+=1
					# if the filename is lowercase and has just one letter or a random combination of lowercase letters
					if (fnmatch.fnmatch(file, '[a-z].java') and file.islower()) or fnmatch.fnmatch(file,'[a-z][a-z]*.java') and file.islower():
						#number of obfuscated elements increases
						obfuscated+=1
					#if the filename contains lowercase and uppercase letters
					elif file.islower()==False and file.isupper()==False:
						#number of non obfuscated files increases
						not_obfuscated+=1
		print('Total number of java files = ',count)
		print('No. of obfuscated java files = ', obfuscated)
		print('No. of not obfuscated java files = ', not_obfuscated)
		#the percentage of obfuscated files => number of obfuscated files divided by the total number of java files
		obfuscation_percentage = obfuscated/count*100
		print ('Obfuscation percentage',obfuscation_percentage, '%')
		#if percentage under 33% => not good
		if obfuscation_percentage < 33:
			print('\033[31m' + 'Filenames are not obfuscated')
		#if percentage over 33% but under 66% => better than nothing
		elif 33<obfuscation_percentage < 66:
			print ('Filenames are not obfuscated enough')
		else:
		#if percentage above 66% => good enough
			print('\033[32m' + 'Filenames are obfuscated')
			
test=isObfuscated()
test.obf_files()
