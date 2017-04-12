## 3 вариант

import re
import os

def dirs():
    kir = '[А-Яа-яЁё]*'
    stuff = '[A-Za-z\.\?!0-9"@№;%:?*_()-+=#$^&:;\'"><,/\|\\~`]'
    names = []
    for f in os.listdir('.'):
        if os.path.isdir(f) and re.search(kir, f) and re.search(stuff, f) == None:
            names.append(f)
    return names 

def answer():
    names = dirs()
    if names == []:
        print("В текущей папке нет папок, название которых состоит только из кириллических символов.")
    else:
        print("В текущей папке " + str((len(names))) + " папок, название которых состоит только из кириллических символов.")

def allfiles():
    files = []
    name = '.*\.'
    for f in os.listdir('.'):
        if os.path.isdir(f) and f not in files:
            files.append(f)
        elif os.path.isfile(f) and re.search(name, f):
            n = re.search(name, f).group(0)
            n = n.strip('.')
            if n not in files:
                files.append(n)
    print("Вот названия всех найденных в текущей папке файлов и папок: ")
    for f in files:
        print(f)

def main():
    answer()
    allfiles()

if __name__ == '__main__':
    main()
