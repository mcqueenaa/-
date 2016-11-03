## 3 вариант
a=input("Введите слово")
a=a[::-1]
i=0
for letter in a:
    if letter!='з'and letter!='я':
        print(letter)
    i+=1
input()
