import unittest
import fnmatch
import os
import random
import string 

folder1 = 'rrrrrr'
folder2 = 'android'
folder3 = 'v4'
folder4 = 'immersion'
folder5 = 'InPlay'
folder6 = 'a'
folder7 = 'bb'
folder8 = 'cf'
class TestProject(unittest.TestCase):
	def setUp(self):
		pass
		
	def test_foldername_rrrrrr(self):
		for i in range(0,len(folder1)):
			self.assertTrue(i+1<=(len(folder1)-1) and folder1[i] == folder1[i+1] and folder1.islower())
			break
	
	def test_foldername_android(self):
		for i in range(0,len(folder2)):
			self.assertFalse(i+1<=(len(folder2)-1) and folder2[i] == folder2[i+1] and folder2.islower())
			break
			
	def test_foldername_v4(self):
		for i in range(0,len(folder3)):
			self.assertFalse(i+1<=(len(folder3)-1) and folder3[i] == folder3[i+1] and folder3.islower())
			break
			
	def test_foldername_immersion(self):
		for i in range(0,len(folder4)):
			self.assertFalse(i+1<=(len(folder4)-1) and folder4[i] == folder4[i+1] and folder4.islower())
			break
			
			
	def test_foldername_InPlay(self):
		for i in range(0,len(folder5)):
			self.assertFalse(i+1<=(len(folder5)-1) and folder5[i] == folder5[i+1] and folder5.islower())
			break
			
	def test_foldername_a(self):
		for i in range(0,len(folder6)):
			self.assertFalse(i+1<=(len(folder6)-1) and folder6[i] == folder6[i+1] and folder6.islower())
			break
	
	def test_foldername_bb(self):
		for i in range(0,len(folder7)):
			self.assertTrue(i+1<=(len(folder7)-1) and folder7[i] == folder7[i+1] and folder7.islower())
			break
			
	def test_foldername_cf(self):
		for i in range(0,len(folder8)):
			self.assertFalse(i+1<=(len(folder8)-1) and folder8[i] == folder8[i+1] and folder8.islower())
			break
		
if __name__ == '__main__':
    unittest.main()