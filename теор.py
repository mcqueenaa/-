##Comprehensions
a = [1,2,3,4,5,6,7,8,9]
b = []
for i in a:
    b.append(i**2)

МОжем сделать то же самое в одну строчку
new_b = [i**2 for i in a]

words = ['Mary', 'John', 'Jack', 'Tim', 'Kate', 'Tom', 'Moses', 'Jesus']
new_words = [w.upper() for w in words]
на выходе - MARY JOHN JAKE TIM...

b = []
for i in a:
    if i < 10 and i%2 == 0:
        b.append(i**2)

new_b = [i**2 for i in a if i < 10 and i%2 == 0]

other_words = [w.upper() for w in words if re.search('[aAjJ]', w)]

##Dict Comprehension
вместо массивов собираем словари

d = {"корова": "му", "собака": "гав", "кот": "мяу", "свинюга": "хрю"}
sounds = {d[key]: key for key in d}

sounds = {d[key]: key for key in d if len(key) > 4}

##Массив массивов
big = [a, new_b, words]
flat = []
for arr in big:
    for item in arr:
        flat.append(item)

или:
flat = [item for arr in big for item in arr]

##КОНЕЦ

##Форматирование строк
s = 'Hello, world! That\'s all folks!'
s.upper()
s.lower()
s.capitalize()
s.title()

template = 'Hello, {}!'
template.format('John')
name = 'Mary'
template.format(name)

template.format(input('Введите имя!!!!!!!12!1111: '))

template = 'Привет, {1} {0}! Вы, {0}, наш самый ценный клиент. ТОлько вам, {0} {1}, и только сегодня мы предлагаем шкурку от бананов!!!'.format('ПЕтя', 'Иванов')

arr = [21, 45, 100, 4, 5, 6, 6, 99]
template = 'Возраст: {:>10}' стрелочки - это выравнивание. < справа, > слева, ^ посередине. число - минимальное окно, в котором текст.
через двоеточие вводим изменения в форматировании 
for i in arr:
    print(template.format(i))



'{:+>10}'.format('text')
при выравнивании текст заполнится плюсиками вместо пробелов

pi = 3.14159265358979323
'Ваше число {:.2f}'.format(pi)
f означает что число дробное и берем два знака после запятой, а не просто два знака

'{:+>10}'.format('эйяфладлайяокудль')

