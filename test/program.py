##1
freq = []
conj = []
with open('text.txt','r', encoding = 'utf-8') as f:
    text = f.read()
    freq = text.split('\n')
for word in freq:
    conj = word.split(' | ')
    if conj[1] == 'союз':
        print(word)

##2
female = []
string = ' '
words = []
ipm = 0
for word in freq:
    words = word.split(' ')
    if words[4] == 'ед' and words[5] == 'жен':
        female = word.split(' | ')
        strint += female[0] + ','
        ipm += int(female[2])
print(string)
print('Сумма всех ipm слов женского рода единственного числа равна', ipm , '.')

##3
newword = input('Введите слово')
arr = []
r = []
while newword:
    arr.append(newword)
    newword = input('Введите слово')
for word in freq:
    r = word.split(' | ')
    for newword in arr: 
        if r[0] == newword:
            print(word)
        else:
            print('Слова ', i , ' нет в словаре.')
        
