import os
import promptlib


# choose folder via prompter
def chooseFolder():
    prompter = promptlib.Files()
    dir = prompter.dir()
    return dir


# create folder
def createFolder(folderName):
    cwd = os.getcwd()
    dir = os.path.join(cwd, folderName)
    print(dir)
    # virgin create
    if not (os.path.exists(dir)):
        print('folder unexistent')
        os.mkdir(dir)
        os.chdir(dir)
        return True
    else:
        print('folder existed')
        os.chdir(dir)
        return False


def goMainFolder():
    os.chdir(os.pardir)