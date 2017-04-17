import os
import shutil

def remove(folder):
    for root, dirs, files in os.walk(folder):
        for f in files:
            os.remove(f)
        for d in dirs:
            os.rmdir(d)
    os.rmdir(folder)

remove('C:\\Users\\student\\Desktop\\papka\\pp')
нужно как-тр делать через os.path.join
