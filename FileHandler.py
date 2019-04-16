import getpass


class FileHandler:
  
    @staticmethod
    def fileOut(file, data:str):
        with open(file=file, mode='a', encoding='UTF-8') as FILE:
            FILE.write(str(data))


    @staticmethod
    def fileIn():
        pass