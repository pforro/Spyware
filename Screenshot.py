from PIL import ImageGrab
from threading import Thread
from os import system, path
import time



class Screenshot(Thread):

    def __init__(self):
        Thread.__init__(self, name='screenshots')
        self.__screenshotFrequency = 5
        self.__screenshotNumber = 0
        self.__active = True
        self.__filePath = path.dirname(path.abspath(__file__))



    @property
    def isActive(self):
        return self.__active


    @isActive.setter
    def isActive(self, active:bool):
        if self.__active != active:
            print(f'Screenshot active: {active}')
        self.__active = active


    def run(self):
        while True:
            if self.__active: 
                time.sleep(self.__screenshotFrequency)
                pic = ImageGrab.grab()
                self.__screenshotNumber += 1
                pic.save(self.__filePath + f'\\{self.__screenshotNumber}.jpg')
                print(f'Screenshot-{self.__screenshotNumber} taken')




if __name__ == "__main__":
    system('cls')
    screenshot = Screenshot()
    screenshot.start()