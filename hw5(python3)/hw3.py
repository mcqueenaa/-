##3 вариант
word = input('Введите слово ')
array = []
while word:
    array.append(word)
    word = input('Введите слово ')
for i in range(len(array)):
    newword = array[i]
    newword = newword[i+1 : ]
    print(newword)
