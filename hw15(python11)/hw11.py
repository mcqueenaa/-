##3 вариант

import re

def opentext(fname):
    with open (fname, 'r', encoding = 'utf-8') as t:
        text = t.read()
    return text

def sublanguage(fname):
    text = opentext(fname)
    lang = '(язык)(и|а(ми?|х)?|у|о[мв]|е)?(\s|\.| |\?|\'|,|-|"|»|!|\(|\)|;|:)'
    Lang = '(Язык)(и|а(ми?|х)?|у|о[мв]|е)?(\s|\.| |\?|\'|,|-|"|»|!|\(|\)|;|:)'
    l = re.search(lang, text)
    L = re.search(Lang, text)
    if re.search(lang, text):
        text = re.sub(l.group(1), 'шашлык', text)
    if re.search(Lang, text):
        text = re.sub(L.group(1), 'Шашлык', text)
    return text

def savenew(fname):
    text = sublanguage(fname)
    with open ('newlingua.html', 'w', encoding = 'utf-8') as t:
        t.write(text)
    
def main():
    savenew('lingua.html')

if __name__ == '__main__':
    main()
