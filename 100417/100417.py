##Работа с файлами и папками
модули

import os
import shutil

Windows C:\\Users\\student\\Downloads - экранируем слэши
(на маке и линуксе слеши наоборот)

os.path.abspath('.') - абсолютный путь к папке, в которой я нахожусь ссейчас(точка - текущая папка)
os.getcwd - то же самое

os.path.join('texts','1.txt') соединяет название файла и папки

os.path.exists('texts') - проверяет, есть ли такая папка или файл

os.listdir('.') - возвращает массив со строками-именами файлов в папке

s = 'приветки!'
i = 1
for f in os.listdir('.'):
    if f.endswith('.txt'):
        with open(f, 'a', encoding = 'utf-8') as w:
            w.write(s*i)
            i += 1
Если в папке есть файлы txt, то в них записывается слово приветки i раз

os.mkdr('folder1') - создать папку
os.makedirs('a\\long\\volk\\kot') - создать папки в папке

os.rename('Староеимя', 'новоеимя') - переименовать файл или папку

os.path.isfile(r'texts\corpus1.txt') - проверяет, является ли то, что задано файлом (r для  неэкранирования)
os.path.isdir(r'texts\lalala.txt') - проверяет, является ли папкой


shutil.copy('texts\\corpus1.txt', 'newcorpus\\corpus1.txt') - копирует файл из папки в другую папку
shutil.copytree('texts', 'corpus') - копирует все из одной папки в новую которая создается

shutil.move('texts\\lala.txt', 'corpus\\lala.txt') - перемещает файл из папки в другую папку

os.remove(r'corpus\corpus2.txt') - удаляет файл
shutil.rmtree('texts') - удаляет папку

