from PIL import ImageGrab
from os import system, path
from Configuration import Configuration


class Screenshot():

    def __init__(self, config: Configuration):
        self.__config = config
        self.__screenshotCounter = 0



    def takeScreenshot(self) -> None: 
        pic = ImageGrab.grab()
        self.__screenshotCounter += 1
        pic.save(self.__config.screenshotPath + f'\\{self.__screenshotCounter}.jpg')
        if self.__config.debug:
            print(f'Screenshot-{self.__screenshotCounter} taken')
