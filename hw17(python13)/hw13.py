## 3 вариант

import re
import os

def dirs():
    kir = '[А-Яа-я]*'
    stuff = '[A-Za-z\.\?!0-9"@№;%:?*_()-+=#$^&:;\'"><,/\|\\~`]'
    names = []
    for f in os.listdir('.'):
        if os.path.isdir(f) and re.search(kir, f) and f not in names and re.search(stuff, f) == None:
            names.append(f)
    return names 

def answer():
    names = dirs()
    print("В текущей папке " + str((len(names))) + " папок, название которых состоит только из кириллических символов. Вот их названия: ")
    for i in names:
        print(i)

def main():
    answer()


if __name__ == '__main__':
    main()
