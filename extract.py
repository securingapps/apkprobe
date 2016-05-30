import fnmatch
import sys
import os
import subprocess
import timing
# extractJavaFiles class is used for enjarifying the apk files and extracting the java files from the jar
class extractJavaFiles:
	def extract(self):
		# the 'p' process will enjarify the apk file (the output file will be 'nameofapk'+'-enjarify.jar')
		p = subprocess.Popen('python -O -m enjarify.main ' + var, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		print('Searching for APKs...')
		print('Enjarifying...')
		for line in p.stdout.readlines():
			retval = p.wait()
		#searching for the .jar file in the current folder
		for file in os.listdir('.'):
			if fnmatch.fnmatch(file, var2+'-enjarify.jar') :
				#print (file)
				# the 'p' process will extract the java files from the jar file (the files and folder will be saved in ./Extract_(name of the file)/ folder)
				p = subprocess.Popen('java -jar jd-core.jar ' + file +' ./Extract_'+var2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				for line in p.stdout.readlines():
					retval = p.wait()
			
#the output will be printed in 'AnalyzeFile+'jar file name''
# isObfuscated class will check the names of the java files and count which are obfuscated
class isObfuscated:
	def obf_files(self):
		filename  = open("AnalyzeFile_"+var2+".txt",'w')
		sys.stdout = filename
		print('-'*100)
		print('1. Analyze file obfuscation')
		print('-'*100)
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
					elif len(file[0:-5])==3 and file.islower()==False and file.isupper()==False:
						obfuscated+=1
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
			print('Filenames are not obfuscated')
		#if percentage over 33% but under 66% => better than nothing
		elif 33<obfuscation_percentage < 66:
			print ('Filenames are not obfuscated enough')
		else:
		#if percentage above 66% => good enough
			print('Filenames are obfuscated')
# isFolderObfuscated class will check the names of the folders and count which are obfuscated
class isFolderObfuscated:
	def obf_folders(self):
	
		print('-'*100)
		print('2. Analyze folder obfuscation')
		print('-'*100)
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
							break
						elif i ==0==len(name)-1: # verrifying if the name of a folder contains just 1 letter
							obfuscated+=1 #no. of obfuscated folder name increases
				#verifies if the folder name has 2 letters of different cases
				elif len(name)==2 and name.islower()==False and name.isupper()==False:
					obfuscated+=1 #no. of obfuscated folder name increases
				#verifies if the folder name has one letter in upper case
				elif len(name)==1 and name.isupper():
					obfuscated+=1 #no. of obfuscated folder name increases
				#verifies if the folder name does not contain vowels
				elif '[a,e,i,o,u]' not in name:
					obfuscated+=1 #no. of obfuscated folder name increases
		print('Total number of folders = ',count)
		print('No. of obfuscated folders = ', obfuscated)
		#the percentage of obfuscated folders => number of obfuscated folders divided by the total number of folders
		obfuscation_percentage = obfuscated/count*100
		print ('Obfuscation percentage',obfuscation_percentage, '%')
		#if percentage under 33% => not good
		if obfuscation_percentage < 33:
			print('Folder names are not obfuscated')
		#if percentage over 33% but under 66% => better than nothing
		elif 33<obfuscation_percentage < 66:
			print ('Folder names are not obfuscated enough')
		else:
		#if percentage above 66% => good enough
			print('Folder names are obfuscated')
			
			
#nativeCode class verifies if the java files contain native code
class nativeCode:
	def native_code(self):
		print('-'*100)
		print('3. Analyze native code')
		print('-'*100)
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file1 = open(p, "r")
				for line in my_file1:
						#searching in the lines of the java code and if the line ends with a semicolon
						#and has the word native we print it
					if  'public native' in line and line[-2]==';':
						print ('Native code',line)
						print ('The path', p)
						print('*'*100)
					elif 'private native' in line and line[-2]==';':
						print ('Native code',line)
						print ('The path', p)
						print('*'*100)
					elif 'private static native' in line and line[-2]==';':
						print ('Native code',line)
						print ('The path', p)
						print('*'*100)
					elif 'public static native' in line and line[-2]==';':
						print ('Native code',line)
						print ('The path', p)
						print('*'*100)
				my_file1.close()
				
# unzipApk class will unzip the files in the apk archive to a folder
class unzipApk:
	def unzip_apk(self):
		for file in os.listdir('.'):
			if fnmatch.fnmatch(file, var):
				#p runs the unzip command
				p = subprocess.Popen('7z x '+ var +' "-o./Unzip'+ var2+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				for line in p.stdout.readlines():
					retval = p.wait()

#isSo class will verify if there are .so files in the libs folder of the unzipped apk					
class isSo:
	def so_files(self):
		print('-'*100)
		print('4. Search for .so files')
		print('-'*100)
		#this method check for.so files in the Unzip_name_of_apk folder
		for subdir, dirs, files in os.walk(rootdir3):
			for file in files:
				p=os.path.join(subdir,file)
				if(fnmatch.fnmatch(file, '*.so')):
					print (file,' found in ',p)

#trustManager class uses a dictionary (trustmanager_dict.txt) with relevant terms used in SSL validation techniques
class trustManager:
	def trust_manager(self):
		print('-'*100)
		print('5. Search for SSL validation components')
		print('-'*100)
		with open('trustmanager_dict.txt') as f1:
			l = f1.read()
			words = l.split()
			for word in words: 
				print(word)
				#the words are saved in parameter word
				for subdir, dirs, files in os.walk(rootdir):
					for file in files:
						p=os.path.join(subdir,file)
						my_file2 = open(p, "r")
						for line in my_file2:
							#if the word is find in the line it will print the line and the path
							for part in line.split():
								if word in part:
									print('The part of code in which ',word,' was found',line)
									print('The path of the file in which ',word,' was found',p)
									break
						my_file2.close()
		f1.close()				
				
#encryptAES class searches for the AES encryption method in the java files
class encryptAES:
	def encrypt_aes(self):
		#print('EncryptAES_"'+var2+'".txt" was created in the rootdirectory' )
		#filename  = open("EncryptAES_"+var2+".txt",'w')
		#sys.stdout = filename
		print('-'*100)
		print('6. Search for AES encryption method')
		print('-'*100)
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file3 = open(p, "r")
				for line in my_file3:
					for part in line.split():
						#if the encryption algorithm AES is used the line and th path is printed
						if 'AES' in part:
							print('*'*100)
							print('The line of code in which the string was found',line)
							print('The path of the file in which the string was found',p)
							break
				my_file3.close()

#doFinal searches for dofinal function in the java files
class doFinal:
	def do_final(self):
		print('-'*100)
		print('7. Search for doFinal function')
		print('-'*100)
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file4 = open(p, "r")
				for line in my_file4:
					for part in line.split():
						#searching for the doFinal function
						if 'doFinal' in part:
							print('*'*100)
							print('The line of code in which the string was found',line)
							print('The path of the file in which the string was found',p)
							break
				my_file4.close()

#cipherInit class searches for cipher.init function, used for encryption and decryption
class cipherInit:
	def cypher_init(self):
		print('-'*100)
		print('8. Search for Cipher.init function')
		print('-'*100)
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file5 = open(p, "r")
				for line in my_file5:
					if ',' in line:
						for part in line.split():
							#searching for cipher.init function
							
							if 'Cipher' in part and '.<init>' in part:
								print('*'*100)
								print('The line of code in which the string was found',line)
								print('The path of the file in which the string was found',p)
								# i,j,k,l are special characters used to enclose the second parameter of the function, they are used to
								# extract the second parameter and print it in Output.txt
								#TODO: manage to print on different lines
								i = line.find(",") + 2
								j = line.find(",",i)
								k = line.find(");",i)
								l = line.find(")")+ 1
								#in Output.txt the key parameter is printed 
								with open("Output.txt", "w") as text_file:
									if i and j:
										print ('Key found: ', line[i:j])
										text_file.write(format(line[i:j]+'\n'))
									elif i and k:
										print ('Key found: ', line[i:k])
										text_file.write(format(line[i:k]+'\n'))
									elif l and j:
										print ('Key found: ', line[l:j])
										text_file.write(format(line[l:j]+'\n'))
										
								text_file.close()	
								break
							elif 'cipher.init' in part:
								print('*'*100)
								print('The line of code in which the string was found',line)
								print('The path of the file in which the string was found',p)
								i = line.find(",") + 2
								j = line.find(",",i)
								k = line.find(");",i)
								l = line.find(")")+ 1
								with open("Output.txt", "w") as text_file:
									if i and j:
										print ('Key found: ', line[i:j])
										text_file.write(format(line[i:j]+'\n'))
									elif i and k:
										print ('Key found: ', line[i:k])
										text_file.write(format(line[i:k]+'\n'))
									elif l and j:
										print ('Key found: ', line[l:j])
										text_file.write(format(line[l:j]+'\n'))
								text_file.close()	
								break
							elif 'Cipher.init' in part:
								print('*'*100)
								print('The line of code in which the string was found',line)
								print('The path of the file in which the string was found',p)
								i = line.find(",") + 2
								j = line.find(",",i)
								k = line.find(");",i)
								l = line.find(")")+ 1
								with open("Output.txt", "w") as text_file:
									if i and j:
										print ('Key found: ', line[i:j])
										text_file.write(format(line[i:j]+'\n'))
									elif i and k:
										print ('Key found: ', line[i:k])
										text_file.write(format(line[i:k]+'\n'))
									elif l and j:
										print ('Key found: ', line[l:j])
										text_file.write(format(line[l:j]+'\n'))
								text_file.close()
								break
								
				my_file5.close()
#class keySpec is used for extracting the key parameter from Output.txt and search the java files for this key
# TODO: search for all keys to see if they are defined as plain strings
#class keySpec:
	#def key_spec(self):
	#reading the public key name
	#	if os.stat("Output.txt").st_size !=0:
	#		secret=open("Output.txt").readline().rstrip()
			#print ('The name of the public key parameter is: >>>> ',secret,'<<<<<')
			#searching for it in the java files to check if it is defined as a plain string
	#		for subdir, dirs, files in os.walk(rootdir):
	#			for file in files:
	#				p=os.path.join(subdir,file)
	#				my_file = open(p, "r")
	#				for line in my_file:
	#					m =re.search('(.*)( |=)("|\')(.*)("|\')',line)
	#					if (secret[1:]) in line and m:
							#print('*'*100)
							#print('The line of code in which ',secret,' was found',line)
							#print('The path of the file in which ',secret,' was found',p)
	#				my_file.close()
	#		else:
				#print(secret,' is not a plain string')
					
	#	else:
			#print('No public key parameter found')
			
#hashfunctions class used hash_functions_dict.txt to search for usages of sha1,sha256,md5 and the digest function
class hashfunctions:
	def hash_functions(self):
		print('-'*100)
		print('9. Search for Hash functions')
		print('-'*100)
		with open('hash_functions_dict.txt') as f2:
			l = f2.read()
			words = l.split()
			for word in words: 
				print(word)
				for subdir, dirs, files in os.walk(rootdir):
					for file in files:
						p=os.path.join(subdir,file)
						my_file6 = open(p, "r")
						for line in my_file6:
							for part in line.split():
								if word in part:
									print('*'*100)
									print('The line of code in which', word ,' was found',line)
									print('The path of the file in which ',word,' was found',p)
									break
						my_file6.close()
		f2.close()

		
#for every apk file in the rootdirectory, the classes with the required methods will be called
for file in os.listdir('.'):
			if fnmatch.fnmatch(file, '*.apk'):
				# var represents the android apk we will work with
				var = file
				#var2 is the name of the file without the type
				var2= var[0:-4]
				#the rootdirectory in which we will work
				rootdir = './Extract_'+var2+'/'	
				#rootdir3 will be the folder with the unzipped files of the apk
				rootdir3 = './Unzip'+var2+'/'
				test=extractJavaFiles()
				test.extract()
				test=isObfuscated()
				test.obf_files()
				test=isFolderObfuscated()
				test.obf_folders()
				test=nativeCode()
				test.native_code()
				test=unzipApk()
				test.unzip_apk()						
				test=isSo()
				test.so_files()
				test=trustManager()
				test.trust_manager()
				test=encryptAES()
				test.encrypt_aes()	
				test=doFinal()
				test.do_final()
				test=cipherInit()
				test.cypher_init()
				#test=keySpec()
				#test.key_spec()	
				test=hashfunctions()
				test.hash_functions()
