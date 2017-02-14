import re

lemma = r'<w.*?</w>'

def openlines(fname):
    lines = []
    with open (fname, 'r', encoding = 'utf-8') as t:
        lines = t.readlines()
    return lines

def writelines(fname, text):
    lines = openlines(fname)
    with open ('lines.txt', 'w', encoding = 'utf-8') as f:
        f.write(str((len(lines))))

def opentext(fname):
    text = []
    with open (fname, 'r', encoding = 'utf-8') as t:
        text = t.read()
    return text

def lemm(fname):
    text = opentext(fname)
    lemmas = re.findall(lemma, text)
    return lemmas

def freq(fname):
    lemmas = lemm(fname)
    d = {}
    for i in range(len(lemmas)):
        if lemmas[i] in d:
                d[lemmas[i]] += 1
        else:
                d[lemmas[i]] = 1
    return d

def writekeys(fname):
    d = freq(fname)
    with open ('keys.txt', 'w', encoding = 'utf-8') as f:
        for key in d:
            f.write(key + '\n')

def main():
    writelines('file.xml', 'lines.txt')
    writekeys('file.xml')


