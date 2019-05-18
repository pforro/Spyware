import os, getpass
from glob import glob

class FileExplorer:
    
    
    @staticmethod
    def WriteToFile(result):
        with open("result.txt","w") as file:
            for element in result:
                print(element)
                file.write(element + "\n")

    
    @staticmethod
    def DiscoverDirectory(path):
        content = os.listdir(path)
        FileExplorer.WriteToFile(content)


    @staticmethod
    def SearchForFile(pattern):
        resultSet = glob(pattern,recursive=True)
        FileExplorer.WriteToFile(resultSet)

#-------------------------------------------------------

if __name__ == "__main__":
    path_with_pattern = input("Path with pattern?: ")
    FileExplorer.SearchForFile(path_with_pattern)