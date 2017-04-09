## вариант 3
import re

def opentext(text):
    sentences = []
    with open (text, 'r', encoding = 'utf-8') as t:
        newtext = t.read()
    newtext = re.sub('\n', ' ', newtext)
    sentences = re.split('\?|!|\?!|\.\.\.|\.|…', newtext)
    for i in range(len(sentences)):
        sentences[i] = re.sub('[”“"–«»:;(),]', ' ', sentences[i])
    return sentences

def makewords(text):
    sentences = opentext(text)
    words = [i for s in sentences for i in s.split()]
    return words

def numb(text):
    word = makewords(text)
    wordlen = [[w, len(w)] for w in word]
    template = '{}_{}'
    for w in range(len(wordlen)):
        print(template.format(wordlen[w][0], wordlen[w][1]))

def main():
    numb('телеграмма.txt')
    
if __name__ == '__main__':
    main()
