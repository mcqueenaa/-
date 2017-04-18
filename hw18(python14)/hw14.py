##вариант 3

import os
import shutil
import re

def findext():
    d = {}
    ext = '(.*\.)(.*)'
    for root, dirs, files in os.walk('.'):
        for f in files:
            if re.search(ext, f).group(2) not in d:
                d[re.search(ext, f).group(2)]= '1'
            else:
                d[re.search(ext, f).group(2)] = str(int(d[re.search(ext, f).group(2)]) + 1)
    return d


def findmax():
    d = findext()
    k = 0
    extm = ''
    for key in d:
        if int(d[key]) > k:
            k = int(d[key])
            extm = key
        elif int(d[key]) == k:
            extm = extm + ', ' + key
    print('В текущей папке и в папках, лежащих в ней, наиболее часто встречаются файлы с расширениями: ' + extm + '. Они встречаются ' + str(k) + ' раз.')

def main():
    findmax()

if __name__ == '__main__':
    main()
