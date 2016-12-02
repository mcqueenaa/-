## 3 вариант

arr = []
with open('text.txt','r', encoding = 'utf-8') as t:
    text = t.read()
    text = text.replace('\n', ' ')
    arr = text.split(' ')
len1 = 0
len3 = 0
for word in arr:
    if len(word) == 1:
        len1 += 1
    elif len(word) == 3:
        len3 += 1
if len1 == 0:
    print('В тексте нет слов длиной в 1 символ')
elif len3 == 0:
    print('В тексте нет слов длиной в 3 символа')
else:
    dif = str(len3/len1)
    print('В тексте в ' + dif + ' раз больше слов длиной в 3 символа, чем слов длиной в 1 символ')
