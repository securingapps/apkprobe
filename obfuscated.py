import fnmatch
import os
import glob
from colorama import init
import subprocess
import os.path
import random

init()
not_obfuscated = 0
obfuscated = 0
filesize = len(fnmatch.filter(os.listdir('./Extract/com/jirbo/adcolony/'), '*.java'))
print (filesize)
for file in os.listdir('./Extract/com/jirbo/adcolony/'):
	
	if fnmatch.fnmatch(file, '[a-z].java') or fnmatch.fnmatch(file,'*[a-z]*[!@#$%^&*]*[a-z]*.java') or fnmatch.fnmatch(file,'[a-z][a-z].java'):
		print('Obfuscated file',file)
		obfuscated+=1	
	if file != file.lower() and file != file.upper() or fnmatch.fnmatch(file, '*[0-9]*.java'):
		print ('Not Obfuscated file',file)
		not_obfuscated+=1

obfuscation_percentage = obfuscated/filesize*100
print ('Obfuscation percentage',obfuscation_percentage, '%')

if obfuscation_percentage < 33:
	print('\033[31m' + 'Filenames are not obfuscated')
elif 33<obfuscation_percentage < 66:
	print ('Filenames are not obfuscated enough')
else:
	print('\033[32m' + 'Filenames are obfuscated')