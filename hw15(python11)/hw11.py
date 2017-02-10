##3 вариант
import re

def opentext(fname):
    with open (fname, 'r', encoding = 'utf-8') as t:
        text = t.read()
    return text

def sublanguage(fname):
    text = opentext(fname)
    m = re.sub(r'\bязык\b', r'шашлык', text)
    text = re.sub(r'\bЯзык\b', r'Шашлык', m)
    return text

def savenew(fname):
    text = sublanguage(fname)
    with open ('newlingua.html', 'a', encoding = 'utf-8') as t:
        t.write(text)
    
def main():
    savenew('lingua.html')

if __name__ == '__main__':
    main()
