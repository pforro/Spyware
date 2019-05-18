import os, getpass
from glob import glob
from zipfile import ZipFile

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
        return resultSet


    @staticmethod
    def archive(files_to_archive):
        with ZipFile("D:\\hello.zip", "w") as archive:
            for file in files_to_archive:
                archive.write(file)

#-------------------------------------------------------

if __name__ == "__main__":
    path_with_pattern = input("Path with pattern?: ")
    files_to_archive = FileExplorer.SearchForFile(path_with_pattern)
    FileExplorer.archive(files_to_archive)