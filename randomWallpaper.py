'''
    randomWallpaper
'''
from os import listdir,system
from os.path import realpath,join,exists,dirname
from sys import executable
from random import choice
import argparse,json


# Wallpaper List,set it when read Wallpaper Folder
WallpaperList = []

version = '0.0.1'
info = """\tA sample Wallpaper.Writed by Python. run in
gnome. Use command gsettings when it run.
Open Source in Github with MIT License:
https://github.com/ruxia-TJY/randomWallpaper

Thanks for use!"""

class Config():
    '''
    about config.json
    '''
    def __init__(self):
        self.configPath = join(dirname(executable),'config.json')
        self.config = {"WallpaperDir":[]}
        if not exists(self.configPath):
            self.saveConfig()
        self.readConfig()

    def readConfig(self):
        with open(self.configPath,'r',encoding='utf-8') as f:
            self.config = json.loads(f.read())

    def saveConfig(self):
        with open(self.configPath,'w',encoding='utf-8') as f:
            f.write(json.dumps(self.config))

    def addFolder(self,FolderList:list):
        self.config['WallpaperDir'].extend(FolderList)
        self.saveConfig()

    def deleteFolder(self,FolderList:list):
        wrong_list = []
        for folder in FolderList:
            try:
                self.config['WallpaperDir'].remove(folder)
            except ValueError:
                wrong_list.append(folder)
        self.saveConfig()
        return wrong_list

    def cleanFolder(self):
        self.config['WallpaperDir'] = []
        self.saveConfig()

    def getFolderList(self):
        return self.config['WallpaperDir']


class ConsoleConfig():
    def __init__(self,config):
        self.config = config

    def showCommand(self):
        print('-' * 51)
        print('{: ^51s}'.format('randomWallpaper'))
        print('-' * 51)
        print('a. add random folder')
        print('c. clean folder')
        print('d. delete random folder')
        print('i. show info')
        print('l. show folder list')
        print('r. run')
        print('rc. reshow command list')
        print('rr. reread config.json')
        print('q. quit')

    def run(self):
        self.showCommand()
        while True:
            mode = input('Your command：')
            if mode == 'i':
                self.showInfo()
            elif mode == 'q':
                print('quit!')
                break
            elif mode == 'a':
                self.addFolder()
            elif mode == 'd':
                self.deleteFolder()
            elif mode == 'l':
                self.showFolderList()
            elif mode == 'r':
                setWallpaperByWallpaperLst()
            elif mode == 'rr':
                config.readConfig()
            elif mode == 'rc':
                self.showCommand()
            elif mode == 'c':
                config.cleanFolder()
            else:
                print(f' {mode} not support!try again!')

    def addFolder(self):
        path = input('folder path:')
        self.config.addFolder(path.split(','))

    def deleteFolder(self):
        path = input('delete path:')
        lst = self.config.deleteFolder(path.split(','))
        if len(lst):
            for i in lst:
                print(f'{i} delete failed!')

    def showFolderList(self):
        for folder in self.config.getFolderList():
            print(folder)

    def showInfo(self):
        print('\n')
        print('-' * 51)
        print('{: ^51s}'.format('randomWallpaper'))
        print('{: ^51s}'.format(version))
        print('-' * 51)
        print(info)
        print('-' * 51)


def setWallpaperByDir(dirPath):
    img = choice(dirPath)           # random.choice
    print(f'set Wallpaper path:{img}')
    # os.system
    system(f"DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-uri  'file://{img}'")

def setWallpaperByWallpaperLst():
    global WallpaperList
    readWallpaperList()
    if len(WallpaperList):
        setWallpaperByDir(WallpaperList)
    else:
        print('no images!add any image to Folders')

def readWallpaperList():
    global WallpaperList
    global config
    if not len(config.getFolderList()):
        print('no folders,use -c to config')
        return

    for dirPath in config.getFolderList():
        if not exists(dirPath):
            continue
        for filePath in listdir(dirPath):
            WallpaperList.append(realpath(join(dirPath, filePath)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=info)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', '--run', action='store_true', dest='run', default=False, help='run as config.json')
    group.add_argument('-c', '--config', action='store_true', dest='config', default=False, help='config by console')
    group.add_argument('-a','--add',dest='add',nargs='+',help='add folders')
    group.add_argument('-d', '--delete', nargs='+', dest='delete', help='delete folders')
    group.add_argument('-n', '--clean', action='store_true', dest='clean', default=False, help='clean Folders')
    group.add_argument('-v', '--version', action='store_true', dest='version', default=False, help='Version')
    group.add_argument('-l', '--list', action='store_true', dest='list', default=False, help='show folder list')

    args = parser.parse_args()
    config = Config()
    CC = ConsoleConfig(config)

    if not any(i for i in [args.config,args.add,args.delete,args.clean,args.version,args.list]):
        args.run = True

    if args.run:
        setWallpaperByWallpaperLst()

    if args.config:
        CC.run()

    if args.add:
        folderLst = ','.join(args.add).split(',')
        config.addFolder(folderLst)

    if args.delete:
        folderLst = ','.join(args.delete).split(',')
        wrong_lst = config.deleteFolder(folderLst)
        for f in wrong_lst:
            print(f'{f} delete false!')

    if args.list:
        for f in config.getFolderList():
            print(f)

    if args.clean:
        config.cleanFolder()

    if args.version:
        print(version)