import os
import hashlib
import logging
from ftplib import FTP
from filelock import Timeout, FileLock
from constants import FILESYSTEM

class FtpManager:

    __ftp = 'pureftpd'
    __login = 'kev'
    __password = '123456'

    def __init__(self):
        ftp = FTP(self.__ftp)
        ftp.login(self.__login, self.__password)
        self.ftp = ftp

    def serve2Ftp(self, source):
        source = FILESYSTEM()+source

        if not os.path.exists(source):
            raise Exception('O arquivo não existe')
        try:
            fp = open(source, 'rb')
            self.ftp.storbinary('STOR %s' % os.path.basename(source), fp, 1024)
            fp.close()
            return source
        except:
            raise Exception('Não foi possível mover o arquivo no ftp')
        finally:
            self.ftp.close()