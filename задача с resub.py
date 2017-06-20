import re

def opentext(fname):
    with open (fname, 'r', encoding = 'utf-8') as t:
        text = t.read()
    return text

def deltag(fname):
    text = opentext(fname)
    m = re.sub(r'<.*?>', r' ', text)
    text = re.sub(r'\s+', r' ', m)
    return text

def byeSteve(fname):
    text = deltag(fname)
    m = re.sub(r'Стив Джобс', r'Сабрина Маленькая Ведьма', text)
    print(m)
    
def syllable(fname):
    opentext()
    
