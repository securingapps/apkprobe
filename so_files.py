import fnmatch
import os
import glob
from colorama import init
import subprocess
import os.path
import random

init()

rootdir = './Unzip/'


class isSo:
	def so_files(self):
		for subdir, dirs, files in os.walk(rootdir):
			for file in files:
				p=os.path.join(subdir,file)
				if(fnmatch.fnmatch(file, '*.so')):
					print (file,' found in ',p)
				
test1=isSo()
test1.so_files()