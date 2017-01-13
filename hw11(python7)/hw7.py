def opentext(text):
    words = []
    with open (text, 'r', encoding = 'utf-8') as t:
        newtext = t.read()
    newtext = newtext.lower()
    words = newtext.split()
    for i in range(len(words)): 
        words[i] = words[i].strip('”“".,!?')
    return words

def numbhood(text):
    words = opentext(text)
    hood = []
    for i in range(len(words)):
        if len(words[i])>4:
            if words[i].endswith('hood'):
                if words[i] not in hood:
                    hood.append(words[i])
    return hood

def frequency(text, word):
    words = opentext(text)
    freq = 0
    for i in range(len(words)):
        if words[i] == word:
            freq += 1
    return freq

text = input('Введите имя файла с английским текстом: ')
hood = numbhood(text)
print('В тексте нашлось', len(hood), 'существительных с суффиксом -hood.')
hfreq = []
for i in range(len(hood)):
    hfreq.append(frequency(text, hood[i]))
minfreq = []
for i in range(len(hood)):
    if hfreq[i] == min(hfreq):
        minfreq.append(hood[i])
    forms = []
for i in range(len(minfreq)):
    forms.append(minfreq[i][0:-4])
', '.join(forms)
', '.join(minfreq)
print('Существительные с суффиксом -hood, имеющие наименьшую частотность в тексте: ' + str(minfreq))
print('Они образованы от слов: ' + str(forms))
