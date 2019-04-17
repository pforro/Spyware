from Configuration import Configuration
from threading import Thread
from time import sleep
from requests import get
from json import loads

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
        response = get(url=self.__config.baseURL, params={'username':self.__config.userName})
        data = response.json()
        print(data)



if __name__ == "__main__":
    configuration = Configuration()
    communication = Communication(configuration)
    communication.start()