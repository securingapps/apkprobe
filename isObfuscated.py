import fnmatch
import os
import glob
from colorama import init
import subprocess
import os.path
import random

init()

rootdir = './Extract/'


class isObfuscated:
	def obf_files(self):
		count = 0
		obfuscated = 0
		not_obfuscated = 0
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				if(fnmatch.fnmatch(file, '*.java')):
					count+=1
					#print(file)
					if (fnmatch.fnmatch(file, '[a-z].java') and file.islower()) or fnmatch.fnmatch(file,'[a-z][a-z]*.java') and file.islower():
						print('Obfuscated file',file)
						obfuscated+=1
					elif file.islower()==False and file.isupper()==False:
						print ('Not Obfuscated file',file)
						not_obfuscated+=1
					else:
						alone = file
		print ('Alone',alone)
		print(count)
		print('No. of obfuscated java files = ', obfuscated)
		print('No. of not obfuscated java files = ', not_obfuscated)
		obfuscation_percentage = obfuscated/count*100
		print ('Obfuscation percentage',obfuscation_percentage, '%')
		if obfuscation_percentage < 33:
			print('\033[31m' + 'Filenames are not obfuscated')
		elif 33<obfuscation_percentage < 66:
			print ('Filenames are not obfuscated enough')
		else:
			print('\033[32m' + 'Filenames are obfuscated')
			
test1=isObfuscated()
test1.obf_files()