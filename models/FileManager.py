import os
import hashlib
import logging
from shutil import copyfile, move
from filelock import Timeout, FileLock
from constants import FILESYSTEM

class FileManager:

    #root = '/app/filesystem/'

    def __init__(self):
        logging.basicConfig(filename='log.log', 
        filemode='w', format='%(name)s - %(levelname)s - %(message)s', 
        level=logging.INFO)

    def manage_file(self, source, destination, move_file = False):

        if not os.path.exists(FILESYSTEM()+source):
            raise Exception('O arquivo não existe')

        if destination.count('.') > 0:
            raise Exception('O diretório destino é inválido')

        file_name = source.split('/')[-1] 
        where_am_i = FILESYSTEM()

        destination = destination.split('/')
        for directory in destination:

            if not directory:
                continue

            where_am_i += directory+'/'

            if not os.path.isdir(where_am_i):
                os.mkdir(where_am_i)

            file_path = FILESYSTEM()+source
            final_path = where_am_i+file_name

        checksum = self.get_checksum(source)

        if move_file:
            move(file_path, final_path)
        else:
            copyfile(file_path, final_path)

        logging.info('Source: '+file_path+' ----- Destiny: '+final_path+' ----- Checksum: '+checksum)

        return checksum


    def remove_file(self, source):
        file_path = FILESYSTEM()+source

        if not os.path.exists(file_path):
            raise Exception('O arquivo não existe')

        checksum = self.get_checksum(source)

        os.remove(file_path)

        logging.info('Removed: '+file_path)
        
        return checksum

    def get_checksum(self, source):
        if not os.path.exists(FILESYSTEM()+source):
            raise Exception('O arquivo não existe')

        #Chunkando em partes para não ter um memory overflow
        hash_md5 = hashlib.md5()
        with open(FILESYSTEM()+source, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)

        return hash_md5.hexdigest()