## вариант 3
import re

def opentext(text):
    sentences = []
    with open (text, 'r', encoding = 'utf-8') as t:
        newtext = t.read()
    newtext = re.sub('\n', ' ', newtext)
    sentences = re.split('\?|!|\?!|\.\.\.|\.|…', newtext)
    sentences = [re.sub('[”“"–«»:;(),]', '', i) for i in sentences]
    return sentences

def makewordlen(text):
    sentences = opentext(text)
    wordlen = [[i, len(i)] for s in sentences for i in s.split()]
    return wordlen

def form(text):
    wordlen = makewordlen(text)
    template = '{}_{}'
    for w in range(len(wordlen)):
        print(template.format(wordlen[w][0], wordlen[w][1]))

def main():
    form('телеграмма.txt')
    
if __name__ == '__main__':
    main()
