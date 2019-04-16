from subprocess import check_output


class Util:
  
    @staticmethod
    def fileOut(file, data:str):
        with open(file=file, mode='a', encoding='UTF-8') as FILE:
            FILE.write(str(data))


    @staticmethod
    def fileIn():
        pass


    @staticmethod
    def executeShellCommand(command:str):
        result = ''
        try:
            result = check_output(command, shell=True, encoding='437')
        except Exception:
            result = 'Shell command execution failed!'
        return result
