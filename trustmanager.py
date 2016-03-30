import fnmatch
import os
import glob
import subprocess
import os.path
import random
import string

rootdir = './Extract/'

for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		p=os.path.join(subdir,file)
		my_file = open(p, "r")
		for line in my_file:
			#print(line)
			for part in line.split():
				if 'trustmanager' in part or 'sslsocket' in part or ' checkServerTrusted' in part or 'getPeerCertificates' in part or 'certificate' in part or 'sslcontext' in part:
					print(part)
					print(p)
					break
		my_file.close()