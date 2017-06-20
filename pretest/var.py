import re

def opentext(text):
    with open (text, 'r', encoding = 'utf-8') as t:
        text = t.read()
    return(text)
        
def anawords(text):
    t = opentext(text)
    nwords = re.findall(r'<w>', t)
    nana = re.findall(r'<ana', t)
    k = len(nana)/len(nwords)
    print('Среднее количество разборов на слово =', str(k), '.')

def dictionary(text):
    t = opentext(text)
    d = {}
    part = 'gr="(\w+)'
    strings = t.split('\n')
    for s in strings:
        sd = {}
        for i in re.findall(part, s):
            sd[i] = ''
        for key in sd:
            if key not in d:
                d[key] = '1'
            else:
                d[key] = str(int(d[key]) + 1)
    return(d)

def makefreq(text):
    d = dictionary(text)
    with open ('freqtext.txt', 'w', encoding = 'utf-8') as f:
        for key in d:
            f.write('{}\t{}\n'.format(key, d[key]))

def SIns(text):
    t = opentext(text)
    strings = re.findall('<w>(.*?)</w>', t) 
    reg = '<.*=ins.*>'
    com = '(\w+)<'
    cont = []
    words = []
    for s in range(len(strings)):
        if re.search(reg, strings[s]):
            word = strings[s-3]+strings[s-2]+strings[s-1]+strings[s]+strings[s+1]+strings[s+2]+strings[s+3]
            cont.append(word)
    for i in cont:
        three = ''
        for j in re.findall(com, i):
            three = three+j+' '
        words.append(three)
    return words

def makeins(text):
    words = SIns(text)
    with open ('ins.txt', 'w', encoding = 'utf-8') as f:
        for w in words:
            seven = w.split()
            f.write(seven[0]+' '+seven[1]+' '+seven[2]+'\t'+seven[3]+'\t'+seven[4]+' '+seven[5]+' '+seven[6]+'\n')
    
def main():
    anawords('text.xml')
    makefreq('text.xml')
    makeins('text.xml')

if __name__ == '__main__':
    main()
