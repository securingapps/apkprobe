import fnmatch
import os
import glob
from colorama import init
import subprocess

init()

var = input("Please enter an apk: ")

for file in os.listdir('.'):
	if fnmatch.fnmatch(file, var):
		print (file)
		p = subprocess.Popen('7z x '+ var +' "-oC:/Users/iua713/Desktop/TestProject_ObsucationScripts/Unzip"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		for line in p.stdout.readlines():
			print (line)
			retval = p.wait()