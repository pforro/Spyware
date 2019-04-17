from Configuration import Configuration
from Util import Util
from threading import Thread
from time import sleep
from requests import get
from json import loads, dumps



class Communication(Thread):

    def __init__(self, config:Configuration):
        Thread.__init__(self, name='communication')
        self.__config = config


    def run(self):
        print('started!')
        while True:
            sleep(self.__config.communicationFrequency)
            self.getConfigFromServer()



    def getConfigFromServer(self):
        try:
            response = get(url=self.__config.baseURL, params={'username':self.__config.userName})
            data = response.json()
            if data:
                jsonData = dumps(data, ensure_ascii=False)
                Util.fileOut(self.__config.filePath + 'config.json', jsonData, 'w')
                if self.__config.debug:
                    print('config file has been created!')
        except Exception:
            print('COMMUNICATION ERROR!')





if __name__ == "__main__":
    configuration = Configuration()
    communication = Communication(configuration)
    communication.start()