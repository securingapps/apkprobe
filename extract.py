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
		p = subprocess.Popen('python -O -m enjarify.main ' + file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		for line in p.stdout.readlines():
			print (line)
			retval = p.wait()
count = 0
for file in os.listdir('.'):
	if fnmatch.fnmatch(file, 'Momondo-enjarify.jar') :
		print (file)
		count+=1
		p = subprocess.Popen('java -jar jd-core.jar ' + file +' ./Extract', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		for line in p.stdout.readlines():
			print (line)
			retval = p.wait()