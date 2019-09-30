import unittest
import random
import os
from random import randint
from shutil import copyfile, move
from random import randrange
from models.FileManager import FileManager
from models.FtpManager import FtpManager
from constants import FILESYSTEM

class modelTest(unittest.TestCase):

	def setUp(self):
		self.testRoot = '/teste/'
		self.testFullPath = FILESYSTEM()+'teste/'
		self.fileManager = FileManager()
		self.existentFile = '1.txt'
		self.inexistentFile = 'arquivo_nao_existe.abc'
		self.checksumExistentFile = 'd0d9f6b975b43818c98739ce17c8ef82'


	def testCopyFileToExistentFolder(self):
		self.fileManager.manage_file(self.existentFile, self.testRoot)
		self.assertEqual(os.path.exists(self.testFullPath+self.existentFile), True)

	def testCopyFileToInexistentFolder(self):
		randomNumber = randint(0,1000)
		self.fileManager.manage_file(self.existentFile, self.testRoot+str(randomNumber))
		self.assertEqual(os.path.exists(self.testFullPath+self.existentFile), True)

	def testMoveFileToExistentFolder(self):
		copyfile('/app/filesystem/1.txt', self.testFullPath+'2.txt')
		self.fileManager.manage_file('/teste/2.txt', self.testRoot+'1/', True)
		self.assertEqual(os.path.exists(self.testFullPath+'1/2.txt'), True)

	def testMoveFileToInexistentFolder(self):
		copyfile('/app/filesystem/1.txt', self.testFullPath+'2.txt')
		self.fileManager.manage_file('/teste/2.txt', self.testRoot+'2/', True)
		self.assertEqual(os.path.exists(self.testFullPath+'2/2.txt'), True)

	def testChecksumExistentFile(self):
		checksum = self.fileManager.get_checksum(self.existentFile)
		self.assertEqual(checksum, self.checksumExistentFile)

	def testRemoveFile(self):
		copyfile('/app/filesystem/1.txt', self.testFullPath+'2.txt')
		self.fileManager.remove_file('/teste/2.txt')
		self.assertEqual(os.path.exists(self.testFullPath+'2.txt'), False)

	def testRemoveInexistentFile(self):
		with self.assertRaises(Exception):
			self.fileManager.remove_file(self.inexistentFile)

	def testChecksumInexistentFile(self):
		with self.assertRaises(Exception):
			self.fileManager.get_checksum(self.inexistentFile)

	def testCopyInvalidFile(self):
		with self.assertRaises(Exception):
			self.fileManager.manage_file('inexistent_file.abc', self.testRoot+'/primeiro/segundo/terceiro')

	def testMoveInvalidFile(self):
		with self.assertRaises(Exception):
			self.fileManager.manage_file('inexistent_file.abc', self.testRoot+'/primeiro/segundo/terceiro', True)

if __name__ == '__main__':
	unittest.main()