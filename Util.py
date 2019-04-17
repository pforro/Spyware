from subprocess import check_output


class Util:
  
    @staticmethod
    def fileOut(file:str, data:str) -> None:
        with open(file=file, mode='a', encoding='UTF-8') as FILE:
            FILE.write(str(data))


    @staticmethod
    def fileIn() -> str:
        pass


    @staticmethod
    def executeShellCommand(command:str) -> str:
        result = ''
        try:
            result = check_output(command, shell=True, encoding='437')
        except Exception:
            result = 'Shell command execution failed!'
        return result
