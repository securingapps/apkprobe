import fnmatch
import os
import glob
from colorama import init
import subprocess
import os.path
import random
import string

init()

rootdir = './Extract/'

class isFolderObfuscated:
	def obf_folders(self):
		count = 0
		obfuscated = 0
		for subdir, dirs, files in os.walk(rootdir):
			for name in dirs:
				count+=1
				#print (os.path.join(rootdir, name))
				if name.islower():
					for i in range(0,len(name)):
						if i+2<=(len(name)-1) and name[i] == name[i+1] == name[i+2]:
							obfuscated+=1
							print (name)
							break
						elif i ==0==len(name)-1:
							obfuscated+=1
							print (name)
		print(count)
		print('No. of obfuscated folders = ', obfuscated)
		obfuscation_percentage = obfuscated/count*100
		print ('Obfuscation percentage',obfuscation_percentage, '%')
		if obfuscation_percentage < 33:
			print('\033[31m' + 'Filenames are not obfuscated')
		elif 33<obfuscation_percentage < 66:
			print ('Filenames are not obfuscated enough')
		else:
			print('\033[32m' + 'Filenames are obfuscated')
			
test2=isFolderObfuscated()
test2.obf_folders()