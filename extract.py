import fnmatch
import sys
import os
import subprocess
import timing

# var represents the android apk we will work with
#var = input("Please enter an apk: ")
#var2 is the name of the file without the type
#var2= var[0:-4]
#rootdir = './Extract_'+var2+'/'
#the rootdirectory in which we will work
#print (rootdir)

# searching for files that match 'var' in the current folder
class extractJavaFiles:
	def extract(self):
		# the 'p' process will enjarify the apk file (the output file will be 'nameofapk'+'-enjarify.jar')
		p = subprocess.Popen('python -O -m enjarify.main ' + var, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		print('Enjarifying...')
		for line in p.stdout.readlines():
			#print (line)
			retval = p.wait()
		#searching for the .jar file in the current folder
		for file in os.listdir('.'):
			if fnmatch.fnmatch(file, var2+'-enjarify.jar') :
				print (file)
				# the 'p' process will extract the java files from the jar file (the files and folder will be saved in ./Extract_(name of the file)/ folder)
				p = subprocess.Popen('java -jar jd-core.jar ' + file +' ./Extract_'+var2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				#print('Extracting java files...')
				for line in p.stdout.readlines():
					#print (line)
					retval = p.wait()
			
		print('Java files have been extracted to ./Extract_',var2,'/ folder')
		
class isObfuscated:
	def obf_files(self):
		#print('File "IsFileObfuscated_'+var2+'.txt" was created in the rootdirectory' )
		filename1  = open("IsFileObfuscated_"+var2+".txt",'w')
		sys.stdout = filename1
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
			print('Filenames are not obfuscated')
		#if percentage over 33% but under 66% => better than nothing
		elif 33<obfuscation_percentage < 66:
			print ('Filenames are not obfuscated enough')
		else:
		#if percentage above 66% => good enough
			print('Filenames are obfuscated')
		#filename1.close()

class isFolderObfuscated:
	def obf_folders(self):
		#print('File "IsFolderObfuscated_'+var2+'.txt" was created in the rootdirectory' )
		filename2  = open("IsFolderObfuscated_"+var2+".txt",'w')
		sys.stdout = filename2
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
			print('Folder names are not obfuscated')
		#if percentage over 33% but under 66% => better than nothing
		elif 33<obfuscation_percentage < 66:
			print ('Folder names are not obfuscated enough')
		else:
		#if percentage above 66% => good enough
			print('Folder names are obfuscated')
		
		#filename2.close()

		#searching in all java files
class nativeCode:
	def native_code(self):
		#print('File "NativeCode_"'+var2+'".txt" was created in the rootdirectory' )
		filename3  = open("NativeCode_"+var2+".txt",'w')
		sys.stdout = filename3
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				my_file1 = open(p, "r")
				for line in my_file1:
					#for part in line.split():
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
		#filename3.close()
				

class unzipApk:
	def unzip_apk(self):
		for file in os.listdir('.'):
			if fnmatch.fnmatch(file, var):
				#p runs the unzip command
				p = subprocess.Popen('7z x '+ var +' "-o./Unzip'+ var+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				for line in p.stdout.readlines():
					retval = p.wait()
					
class isSo:
	def so_files(self):
		#print('SoLibraries_"'+var2+'".txt" was created in the rootdirectory' )
		#the output of the script will be saved to SoLibraries.txt
		filename4  = open("SoLibraries_"+var+".txt",'w')
		sys.stdout = filename4
		#this method check for.so files in the Unzip_name_of_apk folder
		for subdir, dirs, files in os.walk(rootdir3):
			for file in files:
				p=os.path.join(subdir,file)
				if(fnmatch.fnmatch(file, '*.so')):
					print (file,' found in ',p)
		#filename4.close()
class trustManager:
	def trust_manager(self):
		#print('Security_"'+var2+'".txt" was created in the rootdirectory' )
		filename5  = open("Security_"+var2+".txt",'w')
		sys.stdout = filename5
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
		#filename5.close()
				
class encryptAES:
	def encrypt_aes(self):
		#print('EncryptAES_"'+var2+'".txt" was created in the rootdirectory' )
		filename6  = open("EncryptAES_"+var2+".txt",'w')
		sys.stdout = filename6
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
		#filename6.close()
class doFinal:
	def do_final(self):
		#print('DoFinal_"'+var2+'".txt" was created in the rootdirectory' )
		filename7  = open("DoFinal_"+var2+".txt",'w')
		sys.stdout = filename7
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
		#filename7.close()
class cipherInit:
	def cypher_init(self):
		#print('CipherInit_"'+var2+'".txt" was created in the rootdirectory' )
		filename8  = open("CipherInit_"+var2+".txt",'w')
		sys.stdout = filename8
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
								#if found , the second parameter (the name of the public key) will be saved in Output.txt
								#str = line
								#secret = re.search('((.*)(,|\))(.*)(,|\)))',str)
								#TODO: split and special if for (key) cases
								
								#if secret and secret.group(4).isnumeric()==False:
								#	print ('Match found: ', secret.group(4))
								#	with open("Output.txt", "w") as text_file:
								#		text_file.write(format(secret.group(4)+'\n'))
								#secret2 = line.split(',')[1].lstrip()
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
							elif 'cipher.init' in part:
								print('*'*100)
								print('The line of code in which the string was found',line)
								print('The path of the file in which the string was found',p)
								#if found , the second parameter (the name of the public key) will be saved in Output.txt
								#str = line
								#secret = re.search('((.*)(,|\))(.*)(,|\)))',str)
								#TODO: split and special if for (key) cases
								
								#if secret and secret.group(4).isnumeric()==False:
								#	print ('Match found: ', secret.group(4))
								#	with open("Output.txt", "w") as text_file:
								#		text_file.write(format(secret.group(4)+'\n'))
								#secret2 = line.split(',')[1].lstrip()
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
								#if found , the second parameter (the name of the public key) will be saved in Output.txt
								#str = line
								#secret = re.search('((.*)(,|\))(.*)(,|\)))',str)
								#TODO: split and special if for (key) cases
								
								#if secret and secret.group(4).isnumeric()==False:
								#	print ('Match found: ', secret.group(4))
								#	with open("Output.txt", "w") as text_file:
								#		text_file.write(format(secret.group(4)+'\n'))
								#secret2 = line.split(',')[1].lstrip()
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
		#filename8.close()
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
			

class hashfunctions:
	def hash_functions(self):
		#print('Hash_functions_"'+var2+'".txt" was created in the rootdirectory' )
		filename9  = open("Hash_functions_"+var2+".txt",'w')
		sys.stdout = filename9
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
		#filename9.close()
for file in os.listdir('.'):
			if fnmatch.fnmatch(file, '*.apk'):
				# var represents the android apk we will work with
				var = file
				print(var)
				#var2 is the name of the file without the type
				var2= var[0:-4]
				rootdir = './Extract_'+var2+'/'
				#the rootdirectory in which we will work
				print (rootdir)			
				#rootdirectory will be the folder with the unzipped files of the apk
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
