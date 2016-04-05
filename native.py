import enchant
import fnmatch
import os
import glob
import subprocess
import os.path
import random
import string
import re

rootdir = './Extract/'

for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		p=os.path.join(subdir,file)
		my_file = open(p, "r")
		for line in my_file:
			for part in line.split():
				if part == 'native':
					print (line," - contains native code")
		my_file.close()