#using enjarify on an apk file, afterwards extracting the java files in a designated folder
# establishing if the majority of the filenames and folder names are obfuscated
import fnmatch
import sys
import os
import subprocess
import timing
#colorama is used for printing a coloured string
from colorama import init
init()

# var represents the android apk we will work with
var = input("Please enter an apk: ")
var2= input("Please enter a jar file: ")
rootdir = './Extract_'+var2+'/'
#the rootdirectory in which we will work
print (rootdir)

# searching for files that match 'var' in the current folder
class extractJavaFiles:
	def extract(self):
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
		print(var2)
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
		
class isObfuscated:
	def obf_files(self):
		filename  = open("IsFileFolderObfuscated_"+var2+".txt",'w')
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
					if (fnmatch.fnmatch(file, '[a-z].java') and file.islower()) or fnmatch.fnmatch(file,'[a-z][a-z]*.java') and file.islower() or fnmatch.fnmatch(file,'[a-z][A-Z].java'):
						#number of obfuscated elements increases
						obfuscated+=1
						#print(file)
					elif len(file[0:-5])==3 and file.islower()==False and file.isupper()==False:
						obfuscated+=1
						#print(file)
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
			

class isFolderObfuscated:
	def obf_folders(self):
		
		# number of folders in the rootdirectory
		count = 0
		#number of obfuscated folders
		obfuscated = 0
		#searching for all the folders in th rootdirectory
		for subdir, dirs, files in os.walk(rootdir):
			for name in dirs:
				count+=1 #counting the folders
				if name.islower(): #verifying if the name is lowercase
					for i in range(0,len(name)):
						#verifying if the name contains more of the same letter
						if i+2<=(len(name)-1) and name[i] == name[i+1] == name[i+2]:
							obfuscated+=1 #no. of obfuscated folder name increases
							#print ('Obfuscated folder name = ',name)
							break
						elif i ==0==len(name)-1: # verrifying if the name of a folder contains just 1 letter
							obfuscated+=1 #no. of obfuscated folder name increases
							#print ('Obfuscated folder name = ',name)
				elif len(name)==2 and name.islower()==False and name.isupper()==False:
					obfuscated+=1 #no. of obfuscated folder name increases
					#print ('Obfuscated folder name = ',name)
				elif len(name)==1 and name.isupper():
					obfuscated+=1 #no. of obfuscated folder name increases
					#print ('Obfuscated folder name = ',name)
				elif '[a,e,i,o,u]' not in name:
					obfuscated+=1 #no. of obfuscated folder name increases
					#print ('Obfuscated folder name = ',name)
		print('Total number of folders = ',count)
		print('No. of obfuscated folders = ', obfuscated)
		#the percentage of obfuscated folders => number of obfuscated folders divided by the total number of folders
		obfuscation_percentage = obfuscated/count*100
		print ('Obfuscation percentage',obfuscation_percentage, '%')
		#if percentage under 33% => not good
		if obfuscation_percentage < 33:
			print('\033[31m' + 'Folder names are not obfuscated')
		#if percentage over 33% but under 66% => better than nothing
		elif 33<obfuscation_percentage < 66:
			print ('Folder names are not obfuscated enough')
		else:
		#if percentage above 66% => good enough
			print('\033[32m' + 'Folder names are obfuscated')
			

		
test=extractJavaFiles()
test.extract()
test=isObfuscated()
test.obf_files()
test=isFolderObfuscated()
test.obf_folders()
		

