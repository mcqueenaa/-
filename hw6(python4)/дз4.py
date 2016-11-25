## 3 вариант
word = input('Введите слово: ')
for i in range(len(word)):
    newword = (word[i:] + word[:i])
    print(newword)
