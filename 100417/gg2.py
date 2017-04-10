import os
import shutil

n = int(input('Введите число: '))
for i in range(1, n+1):
    os.mkdir(str(i))
    for j in range(1, i+1):
        with open(str(i)+'\\'+str(j) + '.txt', 'w', encoding="utf-8") as f:
            f.write(' ')
