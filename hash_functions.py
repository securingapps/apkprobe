import fnmatch
import os
import glob
import subprocess
import os.path
import random
import string
import timing
import sys
# var represents the android .har file we will work with
var = input("Please enter a jar file: ")
rootdir = './Extract_'+var+'/'
#the rootdirectory in which we will work
print (rootdir)
filename  = open("Hash_functions_"+var+".txt",'w')
sys.stdout = filename
class hashfunctions:
	def sha256(self):
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file = open(p, "r")
				for line in my_file:
					for part in line.split():
						if 'sha256' in part:
							print('*'*100)
							print('The line of code in which sha256 was found',line)
							print('The path of the file in which sha256 was found',p)
							break
				my_file.close()
	def sha1(self):
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file = open(p, "r")
				for line in my_file:
					for part in line.split():
						if 'sha1' in part:
							print('*'*100)
							print('The line of code in which sha1 was found',line)
							print('The path of the file in which sha1 was found',p)
							break
				my_file.close()
	def md5(self):
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file = open(p, "r")
				for line in my_file:
					for part in line.split():
						if 'md5' in part:
							print('*'*100)
							print('The line of code in which md5 was found',line)
							print('The path of the file in which md5 was found',p)
							break
				my_file.close()
	def digest(self):
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file = open(p, "r")
				for line in my_file:
					for part in line.split():
						if 'digest' in part:
							print('*'*100)
							print('The line of code in which digest function was found',line)
							print('The path of the file in which digest function was found',p)
							break
				my_file.close()
		
test=hashfunctions()
test.sha256()
test.sha1()
test.md5()
test.digest()
