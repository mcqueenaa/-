#http://web-corpora.net/Test3/ex2017_var2.html
import re
import os
import shutil

#1
def number(folder):
    reg = '<se>'
    for i in os.listdir(folder):
        arr = []
        with open(os.path.join(folder, i), 'r', encoding = 'utf-8') as t: ##поменяла кодировку во всех файлах
            text = t.read()
        for t in re.findall(reg, text):
            arr.append(t)
        with open('sentences.txt', 'a', encoding = 'utf-8') as f:
            f.write(i+'\t'+str(len(arr))+'\n')
#2
def table(folder):
    with open('info.csv', 'w', encoding = 'utf-8') as f:
        f.write('Файл ; Автор ; Тема \n')
    for i in os.listdir(folder):
        auth = '<meta content="([\w ]*)" name="author">'
        topic = '<meta content="([\w ,]*)" name="topic">'
        with open(os.path.join(folder, i), 'r', encoding = 'utf-8') as t:
            text = t.read()
        for t in re.findall(auth, text):
            for j in re.findall(topic, text):
                with open('info.csv', 'a', encoding = 'utf-8') as f:
                    f.write(i+' ; '+t+' ; '+j+'\n') #нормально открывается в notepad, в экселе что-то не то с кодировкой

#3 не получилось
def bi(folder):
    sen = '<se>((.|\n)*?)</se>'
    pr = '<ana lex="(\w*)" gr="PR">'
    loc = 'gr="S.*?loc"></ana>(\w*)<'
    sentence = ''
    word = '</ana>(\w*)</w>/.'
    for i in os.listdir(folder):
        with open(os.path.join(folder, i), 'r', encoding = 'utf-8') as t: 
            text = t.read()
        for s in re.findall(sen, text):
            print(s)
            for p in re.findall(pr, s):
                for l in re.findall(loc, s):
                    for i in re.findall(word, s):
                        sentence = sentence + i + ' '
                    with open('bigr.txt', 'a', encoding = 'utf-8') as f:
                        f.write(p+' '+l+'\t' + sentence + '\n')
            
def main():
    number('news')
    table('news')
    bi('news')

if __name__ == '__main__':
    main()
