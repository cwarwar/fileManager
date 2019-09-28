import unittest
import random
import os
from random import randrange
from models.FileManager import FileManager

class modelTest(unittest.TestCase):

	def setUp(self):
		self.fileManager = FileManager()

	def testInvalidFile(self):
		with self.assertRaises(Exception):
			self.fileManager.manage_file('inexistent_file.abc', '/primeiro/segundo/terceiro')

if __name__ == '__main__':
	unittest.main()