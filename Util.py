from subprocess import check_output


class Util:
  
    @staticmethod
    def fileOut(file:str, data:str, mode='a') -> None:
        with open(file=file, mode=mode, encoding='UTF-8') as FILE:
            FILE.write(str(data))


    @staticmethod
    def fileIn(file) -> str:
        with open(file=file, mode='r') as FILE:
            return FILE.readlines().join('')



    @staticmethod
    def executeShellCommand(command:str) -> str:
        result = ''
        try:
            result = check_output(command, shell=True, encoding='437')
        except Exception:
            result = 'Shell command execution failed!'
        return result


