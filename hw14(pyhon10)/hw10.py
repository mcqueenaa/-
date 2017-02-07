import re

def opentext(fname):
    with open (fname, 'r', encoding = 'utf-8') as t:
        text = t.read()
    return text

def finddata(fname):
    text = opentext(fname)
    reg = '<table class="infobox vcard"(.|\n)+?</table>'
    if re.search(reg, text):
        card = re.search(reg, text).group()
        profreg = 'Преподаватели(.|\n)*?<p>(.+?)<'
        if re.search(profreg, card):
            number = re.search(profreg, card).group(2)
            with open ('data.txt', 'a', encoding = 'utf-8') as t:
                t.write(number)
        else:
            print('Информации о преподавателях нет')
            with open ('data.txt', 'a', encoding = 'utf-8') as t:
                t.write('Информации о преподавателях нет')
    else:
        print('В данной статье нет карточки')
        with open ('data.txt', 'a', encoding = 'utf-8') as t:
                t.write('В данной статье нет карточки')

def main():
    opentext('HSE.html')
    finddata('HSE.html')
    
if __name__ == '__main__':
    main()
