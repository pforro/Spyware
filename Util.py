from subprocess import check_output
from json import loads


class Util:
  
    @staticmethod
    def fileOut(file:str, data:str, mode='a') -> None:
        with open(file=file, mode=mode, encoding='UTF-8') as FILE:
            FILE.write(str(data))


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


