from PIL import ImageGrab
from os import system, path
import time, getpass



class Screenshot():

    def __init__(self):
        self.__active = True
        self.__screenshotFrequency = 5
        self.__screenshotCounter = 0
        self.__filePath = f'c:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\tempData\\pics\\'



    def takeScreenshot(self): 
        pic = ImageGrab.grab()
        self.__screenshotCounter += 1
        print(self.__filePath + f'\\{self.__screenshotCounter}.jpg')
        pic.save(self.__filePath + f'\\{self.__screenshotCounter}.jpg')
        print(f'Screenshot-{self.__screenshotCounter} taken')




if __name__ == "__main__":
    system('cls')
    screenshot = Screenshot()