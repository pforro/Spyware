from subprocess import check_output
import getpass


class FileHandler:
  
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



if __name__ == "__main__":
    command = 'cd c:\ && rmdir apacukafundaluka && dir'
    print(FileHandler.executeShellCommand(command))

