import os
import glob
import shutil
import string
import random


def randomFilename(saveDir):
    filenameSize = 10
    letters = string.ascii_lowercase + string.ascii_uppercase
    name = ''.join(random.choice(letters) for _ in range(filenameSize))
    return f'{saveDir}/{name}'

def purgeAloneFiles():
    for dir in dirs:
        for i in os.listdir(dir):
            file = os.path.join(dir, i)
            name = file.split('.')[0]
            if name.split(file)[-1] == 'classes.txt':
                continue
            img, txt = f"{name}.jpg", f"{name}.txt"
            if not os.path.exists(img) or not os.path.exists(txt):
                if os.path.exists(img):
                    os.remove(img)
                    print(f'Delete file {img}')
                else:
                    os.remove(txt)
                    print(f'Delete file {txt}')

def join():
    for dir in dirs:
        txts = glob.glob(os.path.join(dir, "*.txt"))
        for txt in txts:
            name = txt.split('.')[0]
            img = f'{name}.jpg'
            name = os.path.split(name)[-1]
            if os.path.exists(img):
                newPathTxt = os.path.join(newDir, f'{name}.txt')
                newPathImg = os.path.join(newDir, f'{name}.jpg')
                if os.path.exists(newPathImg) or os.path.exists(newPathTxt):
                    newName = randomFilename(newDir)
                    while os.path.exists(f'{newName}.jpg'):
                        newName = randomFilename()
                    print(f'rename {name} {newName}')
                    shutil.copy(txt, f'{newName}.txt')
                    shutil.copy(img, f'{newName}.jpg')
                else:
                    shutil.copy(txt, newDir)
                    shutil.copy(img, newDir)

if __name__ == '__main__':
    dirs = ['D:/dts','D:/dts1']
    newDir = "newdataset"
    if not os.path.exists(newDir):
        os.mkdir(newDir)
    purgeAloneFiles()
    join()