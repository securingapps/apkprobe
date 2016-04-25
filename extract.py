#using enjarify on an apk file, afterwards extracting the java files in a designated folder

import fnmatch
import sys
import os
import subprocess
#colorama is used for printing a coloured string
from colorama import init
init()

# var represents the android apk we will work with
var = input("Please enter an apk: ")

# searching for files that match 'var' in the current folder
class extractJavaFiles:
	def extract(self):
		filename  = open("Extract.txt",'w')
		sys.stdout = filename
		for file in os.listdir('.'):
			if fnmatch.fnmatch(file, var):
				# the 'p' process will enjarify the apk file (the output file will be 'nameofapk'+'-enjarify.jar')
				p = subprocess.Popen('python -O -m enjarify.main ' + file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				print('Enjarifying...')
				for line in p.stdout.readlines():
					#print (line)
					retval = p.wait()

		#var2 is the name of the file without the type
		var2 = var[0:-4]
		#print(var2)
		#searching for the .jar file in the current folder
		for file in os.listdir('.'):
			if fnmatch.fnmatch(file, var2+'-enjarify.jar') :
				print (file)
				# the 'p' process will extract the java files from the jar file (the files and folder will be saved in ./Extract_(name of the file)/ folder)
				p = subprocess.Popen('java -jar jd-core.jar ' + file +' ./Extract_'+var2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				print('Extracting java files...')
				for line in p.stdout.readlines():
					#print (line)
					retval = p.wait()
			
		print('Java files have been extracted to ./Extract_',var2,'/ folder')
		
test=extractJavaFiles()
test.extract()
		
