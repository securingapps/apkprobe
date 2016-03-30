import unittest
import fnmatch
import os
import random
import string 

file1 = 'GoogleMap.java'
file2 = 'aaaaa.java'
file3 = 'rcrcrr.java'
file4 = 'd.java'
file5 = 'FB.java'
file6 = 'cf.java'
file7 = 'ghg%jjh.java'
file8 = 'R.java'
class TestProject(unittest.TestCase):
	def setUp(self):
		pass
		
	def test_filename_oneChar_GoogleMap(self):
		self.assertFalse(fnmatch.fnmatch(file1,'[a-z].java'))
		
	def test_filename_oneChar_aaaaa(self):
		self.assertFalse(fnmatch.fnmatch(file2,'[a-z].java'))
		
	def test_filename_oneChar_rcrcrr(self):
		self.assertFalse(fnmatch.fnmatch(file3,'[a-z].java'))
		
	def test_filename_oneChar_d(self):
		self.assertTrue(fnmatch.fnmatch(file4,'[a-z].java'))
		
	def test_filename_oneChar_FB(self):
		self.assertFalse(fnmatch.fnmatch(file5,'[a-z].java'))
		
	def test_filename_oneChar_cf(self):
		self.assertFalse(fnmatch.fnmatch(file6,'[a-z].java'))
		
	def test_filename_oneChar_ghg_jjh(self):
		self.assertFalse(fnmatch.fnmatch(file7,'[a-z].java'))
		
	def test_filename_oneChar_R(self):
		self.assertFalse(fnmatch.fnmatch(file8,'[a-z].java'))
	
	def test_filename_upper_GoogleMap(self):
		self.assertFalse(file1.isupper())
		
	def test_filename_upper_aaaaa(self):
		self.assertFalse(file2.isupper())
		
	def test_filename_upper_rcrcrr(self):
		self.assertFalse(file3.isupper())
		
	def test_filename_upper_d(self):
		self.assertFalse(file4.isupper())
		
	def test_filename_upper_FB(self):
		self.assertFalse(file5.isupper())
		
	def test_filename_upper_cf(self):
		self.assertFalse(file6.isupper())
		
	def test_filename_upper_ghg_jjh(self):
		self.assertFalse(file7.isupper())
		
	def test_filename_upper_R(self):
		self.assertFalse(file8.isupper())
		
	def test_filename_lower_GoogleMap(self):
		self.assertFalse(file1.islower())
		
	def test_filename_lower_aaaaa(self):
		self.assertTrue(file2.islower())
		
	def test_filename_lower_rcrcrr(self):
		self.assertTrue(file3.islower())
		
	def test_filename_lower_d(self):
		self.assertTrue(file4.islower())
		
	def test_filename_lower_FB(self):
		self.assertFalse(file5.islower())
		
	def test_filename_lower_cf(self):
		self.assertTrue(file6.islower())
		
	def test_filename_lower_ghg_jjh(self):
		self.assertTrue(file7.islower())
		
	def test_filename_lower_R(self):
		self.assertFalse(file8.islower())
		
	def test_filename_randomletters_GoogleMap(self):
		self.assertFalse(fnmatch.fnmatch(file1,'[a-z][a-z]*.java') and file1.islower())
	
	def test_filename_randomletters_aaaaa(self):
		self.assertTrue(fnmatch.fnmatch(file2,'[a-z][a-z]*.java') and file2.islower())
		
	def test_filename_randomletters_rcrcrr(self):
		self.assertTrue(fnmatch.fnmatch(file3,'[a-z][a-z]*.java') and file3.islower())
		
	def test_filename_randomletters_d(self):
		self.assertFalse(fnmatch.fnmatch(file4,'[a-z][a-z]*.java') and file4.islower())
		
	def test_filename_randomletters_FB(self):
		self.assertFalse(fnmatch.fnmatch(file5,'[a-z][a-z]*.java') and file5.islower())
		
	def test_filename_randomletters_cf(self):
		self.assertTrue(fnmatch.fnmatch(file6,'[a-z][a-z]*.java') and file6.islower())
		
	def test_filename_randomletters_ghg_jjh(self):
		self.assertTrue(fnmatch.fnmatch(file7,'[a-z][a-z]*.java') and file7.islower())
		
	def test_filename_randomletters_R(self):
		self.assertFalse(fnmatch.fnmatch(file8,'[a-z][a-z]*.java') and file8.islower())
		
	def test_filename_notlowerorupper_GoogleMap(self):
		self.assertTrue(file1.islower()==False and file1.isupper()==False)
		
	def test_filename_notlowerorupper_aaaaa(self):
		self.assertFalse(file2.islower()==False and file2.isupper()==False)
		
	def test_filename_notlowerorupper_rcrcrr(self):
		self.assertFalse(file3.islower()==False and file3.isupper()==False)
		
	def test_filename_notlowerorupper_d(self):
		self.assertFalse(file4.islower()==False and file4.isupper()==False)
		
	def test_filename_notlowerorupper_FB(self):
		self.assertTrue(file5.islower()==False and file5.isupper()==False)
		
	def test_filename_notlowerorupper_cf(self):
		self.assertFalse(file6.islower()==False and file6.isupper()==False)
		
	def test_filename_notlowerorupper_ghg_jjh(self):
		self.assertFalse(file7.islower()==False and file7.isupper()==False)
		
	def test_filename_notlowerorupper_R(self):
		self.assertTrue(file8.islower()==False and file8.isupper()==False)
		
if __name__ == '__main__':
    unittest.main()