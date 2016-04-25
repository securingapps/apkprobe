import os
import subprocess
import os.path
import string

# var represents the android .har file we will work with
var = input("Please enter a jar file: ")
rootdir = './Extract_'+var+'/'
#the rootdirectory in which we will work
print (rootdir)
#searching in all the java classes
class doFinal:
	def do_final(self):
		filename  = open("DoFinal.txt",'w')
		sys.stdout = filename
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file = open(p, "r")
				for line in my_file:
					for part in line.split():
						#searching for the doFinal function
						if 'doFinal' in part:
							print('*'*100)
							print('The line of code in which the string was found',line)
							print('The path of the file in which the string was found',p)
							break
				my_file.close()
				
test=doFinal()
test.do_final()