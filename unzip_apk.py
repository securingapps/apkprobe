import fnmatch
import os
import subprocess
import sys

# var represents the apk used
var = input("Please enter an apk: ")
#rootdirectory will be the folder with the unzipped files of the apk
rootdir = './Unzip'+var+'/'
class unzipApk:
	def unzip_apk(self):
		#the output of the script will be saved to SoLibraries.txt
		filename  = open("SoLibraries.txt",'w')
		sys.stdout = filename
		for file in os.listdir('.'):
			if fnmatch.fnmatch(file, var):
				#p runs the unzip command
				p = subprocess.Popen('7z x '+ var +' "-o./Unzip'+ var+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				for line in p.stdout.readlines():
					retval = p.wait()
					
class isSo:
	def so_files(self):
		#this method check for.so files in the Unzip_name_of_apk folder
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				if(fnmatch.fnmatch(file, '*.so')):
					print (file,' found in ',p)


test=unzipApk()
test.unzip_apk()						
test=isSo()
test.so_files()
