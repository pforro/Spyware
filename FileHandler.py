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
        result = check_output(command)
        return result



if __name__ == "__main__":
    command = 'cd c:\ && mkdir apacukafundaluka && dir'
    print(FileHandler.executeShellCommand(command))

