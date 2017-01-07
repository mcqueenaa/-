## 3 вариант
import random

def noun(number):
    if number == 's':
        s = []
        with open('snouns.txt','r', encoding = 'utf-8') as n:
            snoun = n.read()
            s = snoun.split(' ')
            return random.choice(s)
    pl = []
    with open('plnouns.txt','r', encoding = 'utf-8') as nn:
        plnoun = nn.read()
        pl = plnoun.split(' ')    
        return random.choice(pl)

def verb(numb):
    if numb == 's':
        sv = []
        with open('sverbs.txt','r', encoding = 'utf-8') as v:
            sverb = v.read()
            sv = sverb.split(' ')
            return random.choice(sv)
    plv = []
    with open('plverbs.txt','r', encoding = 'utf-8') as v:
        plverb = v.read()
        plv = plverb.split(' ')    
        return random.choice(plv)
    
def modif():
    am = []
    with open('modif.txt','r', encoding = 'utf-8') as m:
        modifier = m.read()
        am = modifier.split(' ')
        return random.choice(am)

def imperative():
    imp = []
    with open('imperative.txt','r', encoding = 'utf-8') as i:
        imper = i.read()
        imp = imper.split(' ')
        return random.choice(imp)

def conconj():
    con = []
    with open('condconj.txt','r', encoding = 'utf-8') as co:
        cond = co.read()
        con = cond.split(' ')
        return random.choice(con)
    
def conjunction():
    conj = []
    with open('conj.txt','r', encoding = 'utf-8') as c:
        conjs = c.read()
        conj = conjs.split(' ')
        return random.choice(conj)

def sentence1():
    return noun('s') + ' ' + verb('s') + ' ' + modif() + '.'

def sentence2():
    return noun('pl') + ' ' + verb('pl') + ' ' + modif() + '?'

def sentence3():
    return conconj() + ' ' + noun('pl') + ' - ' + noun('pl') + ', ' + conjunction() + ' ' + noun('s') + ' ' + verb('s') + '.'

def sentence4():
    return noun('pl') + ' не ' + verb('pl') + ' ' + modif() + '.'

def sentence5():
    return noun('s') + ', ' + imperative() + ' ' + modif() + '!'

def make_text():
    text = 0
    text = random.choice([1,2,3,4,5])
    while text:
        if text == 1:
            print(sentence1())
            text = random.choice([2,3,4,5])
            if text == 2:
                print(sentence2())
                text = random.choice([3,4,5])
                if text == 3:
                    print(sentence3())
                    text = random.choice([4,5])
                    if text == 4:
                        print(sentence4())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence4()) 
                    break
                elif text == 4:
                    print(sentence4())
                    text = random.choice([3,5])
                    if text == 3:
                        print(sentence3())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence3())
                    break
                else:
                    print(sentence5())
                    text = random.choice([3,4])
                    if text == 3:
                        print(sentence3())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence3())
                    break
            elif text == 3:
                print(sentence3())
                text = random.choice([2,4,5])
                if text == 2:
                    print(sentence2())
                    text = random.choice([4,5])
                    if text == 4:
                        print(sentence4())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence4())
                    break
                elif text == 4:
                    print(sentence4())
                    text = random.choice([2,5])
                    if text == 2:
                        print(sentence2())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence2())
                    break
                else:
                    print(sentence5())
                    text = random.choice([2,4])
                    if text == 2:
                        print(sentence2())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence2())
                    break
            elif text == 4:
                print(sentence4())
                text = random.choice([2,3,5])
                if text == 2:
                    print(sentence2())
                    text = random.choice([3,5])
                    if text == 3:
                        print(sentence3())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence3())
                    break
                elif text == 3:
                    print(sentence3())
                    text = random.choice([2,5])
                    if text == 2:
                        print(sentence2())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence2())
                    break
                else:
                    print(sentence5())
                    text = random.choice([2,3])
                    if text == 2:
                        print(sentence2())
                        print(sentence3())
                    else:
                        print(sentence3())
                        print(sentence2())
                    break
            else:
                print(sentence5())
                text = random.choice([2,3,4])
                if text == 2:
                    print(sentence2())
                    text = random.choice([3,4])
                    if text == 3:
                        print(sentence3())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence3())
                    break
                elif text == 3:
                    print(sentence3())
                    text = random.choice([2,4])
                    if text == 2:
                        print(sentence2())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence2())
                    break
                else:
                    print(sentence4())
                    text = random.choice([2,3])
                    if text == 2:
                        print(sentence2())
                        print(sentence3())
                    else:
                        print(sentence3())
                        print(sentence2())
                    break

        elif text == 2:
            print(sentence2())
            text = random.choice([1,3,4,5])
            if text == 1:
                print(sentence1())
                text = random.choice([3,4,5])
                if text == 3:
                    print(sentence3())
                    text = random.choice([4,5])
                    if text == 4:
                        print(sentence4())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence4())
                    break
                elif text == 4:
                    print(sentence4())
                    text = random.choice([3,5])
                    if text == 3:
                        print(sentence3())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence3())
                    break
                else:
                    print(sentence5())
                    text = random.choice([3,4])
                    if text == 3:
                        print(sentence3())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence3())
                    break
            elif text == 3:
                print(sentence3())
                text = random.choice([1,4,5])
                if text == 1:
                    print(sentence1())
                    text = random.choice([4,5])
                    if text == 4:
                        print(sentence4())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence4())
                    break
                elif text == 4:
                    print(sentence4())
                    text = random.choice([1,5])
                    if text == 1:
                        print(sentence1())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence1())
                    break
                else:
                    print(sentence5())
                    text = random.choice([1,4])
                    if text == 1:
                        print(sentence1())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence1())
                    break
            elif text == 4:
                print(sentence4())
                text = random.choice([1,3,5])
                if text == 1:
                    print(sentence1())
                    text = random.choice([3,5])
                    if text == 3:
                        print(sentence3())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence3())
                    break
                elif text == 3:
                    print(sentence3())
                    text = random.choice([1,5])
                    if text == 1:
                        print(sentence1())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence1())
                    break
                else:
                    print(sentence5())
                    text = random.choice([1,3])
                    if text == 1:
                        print(sentence1())
                        print(sentence3())
                    else:
                        print(sentence3())
                        print(sentence1())
                    break
            else:
                print(sentence5())
                text = random.choice([1,3,4])
                if text == 1:
                    print(sentence1())
                    text = random.choice([3,4])
                    if text == 3:
                        print(sentence3())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence3())
                    break
                elif text == 3:
                    print(sentence3())
                    text = random.choice([1,4])
                    if text == 1:
                        print(sentence1())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence1())
                    break
                else:
                    print(sentence4())
                    text = random.choice([1,3])
                    if text == 1:
                        print(sentence1())
                        print(sentence3())
                    else:
                        print(sentence3())
                        print(sentence1())
                    break

        elif text == 3:
            print(sentence3())
            text = random.choice([1,2,4,5])
            if text == 1:
                print(sentence1())
                text = random.choice([2,4,5])
                if text == 2:
                    print(sentence2())
                    text = random.choice([4,5])
                    if text == 4:
                        print(sentence4())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence4())
                    break
                elif text == 4:
                    print(sentence4())
                    text = random.choice([2,5])
                    if text == 2:
                        print(sentence2())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence2())
                    break
                else:
                    print(sentence5())
                    text = random.choice([2,4])
                    if text == 2:
                        print(sentence2())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence2())
                    break
            elif text == 2:
                print(sentence2())
                text = random.choice([1,4,5])
                if text == 1:
                    print(sentence1())
                    text = random.choice([4,5])
                    if text == 4:
                        print(sentence4())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence4())
                    break
                elif text == 4:
                    print(sentence4())
                    text = random.choice([1,5])
                    if text == 1:
                        print(sentence1())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence1())
                    break
                else:
                    print(sentence5())
                    text = random.choice([1,4])
                    if text == 1:
                        print(sentence1())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence1())
                    break
            elif text == 4:
                print(sentence4())
                text = random.choice([1,2,5])
                if text == 1:
                    print(sentence1())
                    text = random.choice([2,5])
                    if text == 2:
                        print(sentence2())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence2())
                    break
                elif text == 2:
                    print(sentence2())
                    text = random.choice([1,5])
                    if text == 1:
                        print(sentence1())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence1())
                    break
                else:
                    print(sentence5())
                    text = random.choice([1,2])
                    if text == 1:
                        print(sentence1())
                        print(sentence2())
                    else:
                        print(sentence2())
                        print(sentence1())
                    break
            else:
                print(sentence5())
                text = random.choice([1,2,4])
                if text == 1:
                    print(sentence1())
                    text = random.choice([2,4])
                    if text == 2:
                        print(sentence2())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence2())
                    break
                elif text == 2:
                    print(sentence2())
                    text = random.choice([1,4])
                    if text == 1:
                        print(sentence1())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence1())
                    break
                else:
                    print(sentence4())
                    text = random.choice([1,2])
                    if text == 1:
                        print(sentence1())
                        print(sentence2())
                    else:
                        print(sentence2())
                        print(sentence1())
                    break


        elif text == 4:
            print(sentence4())
            text = random.choice([1,2,3,5])
            if text == 1:
                print(sentence1())
                text = random.choice([2,3,5])
                if text == 2:
                    print(sentence2())
                    text = random.choice([3,5])
                    if text == 3:
                        print(sentence3())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence3())
                    break
                elif text == 3:
                    print(sentence3())
                    text = random.choice([2,5])
                    if text == 2:
                        print(sentence2())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence2())
                    break
                else:
                    print(sentence5())
                    text = random.choice([2,3])
                    if text == 2:
                        print(sentence2())
                        print(sentence3())
                    else:
                        print(sentence3())
                        print(sentence2())
                    break
            elif text == 2:
                print(sentence2())
                text = random.choice([1,3,5])
                if text == 1:
                    print(sentence1())
                    text = random.choice([3,5])
                    if text == 3:
                        print(sentence3())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence3())
                    break
                elif text == 3:
                    print(sentence3())
                    text = random.choice([1,5])
                    if text == 1:
                        print(sentence1())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence1())
                    break
                else:
                    print(sentence5())
                    text = random.choice([1,3])
                    if text == 1:
                        print(sentence1())
                        print(sentence3())
                    else:
                        print(sentence3())
                        print(sentence1())
                    break
            elif text == 3:
                print(sentence3())
                text = random.choice([1,2,5])
                if text == 1:
                    print(sentence1())
                    text = random.choice([2,5])
                    if text == 2:
                        print(sentence2())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence2())
                    break
                elif text == 2:
                    print(sentence2())
                    text = random.choice([1,5])
                    if text == 1:
                        print(sentence1())
                        print(sentence5())
                    else:
                        print(sentence5())
                        print(sentence1())
                    break
                else:
                    print(sentence5())
                    text = random.choice([1,2])
                    if text == 1:
                        print(sentence1())
                        print(sentence2())
                    else:
                        print(sentence2())
                        print(sentence1())
                    break
            else:
                print(sentence5())
                text = random.choice([1,2,3])
                if text == 1:
                    print(sentence1())
                    text = random.choice([2,3])
                    if text == 2:
                        print(sentence2())
                        print(sentence3())
                    else:
                        print(sentence3())
                        print(sentence2())
                    break
                elif text == 2:
                    print(sentence2())
                    text = random.choice([1,3])
                    if text == 1:
                        print(sentence1())
                        print(sentence3())
                    else:
                        print(sentence3())
                        print(sentence1())
                    break
                else:
                    print(sentence3())
                    text = random.choice([1,2])
                    if text == 1:
                        print(sentence1())
                        print(sentence2())
                    else:
                        print(sentence2())
                        print(sentence1())
                    break

        else:
            print(sentence5())
            text = random.choice([1,2,3,4])
            if text == 1:
                print(sentence1())
                text = random.choice([2,3,4])
                if text == 2:
                    print(sentence2())
                    text = random.choice([3,4])
                    if text == 3:
                        print(sentence3())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence3())
                    break
                elif text == 3:
                    print(sentence3())
                    text = random.choice([2,4])
                    if text == 2:
                        print(sentence2())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence2())
                    break
                else:
                    print(sentence4())
                    text = random.choice([2,3])
                    if text == 2:
                        print(sentence2())
                        print(sentence3())
                    else:
                        print(sentence3())
                        print(sentence2())
                    break
            elif text == 2:
                print(sentence2())
                text = random.choice([1,3,4])
                if text == 1:
                    print(sentence1())
                    text = random.choice([3,4])
                    if text == 3:
                        print(sentence3())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence3())
                    break
                elif text == 3:
                    print(sentence3())
                    text = random.choice([1,4])
                    if text == 1:
                        print(sentence1())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence1())
                    break
                else:
                    print(sentence4())
                    text = random.choice([1,3])
                    if text == 1:
                        print(sentence1())
                        print(sentence3())
                    else:
                        print(sentence3())
                        print(sentence1())
                    break
            elif text == 3:
                print(sentence3())
                text = random.choice([1,2,4])
                if text == 1:
                    print(sentence1())
                    text = random.choice([2,4])
                    if text == 2:
                        print(sentence2())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence2())
                    break
                elif text == 2:
                    print(sentence2())
                    text = random.choice([1,4])
                    if text == 1:
                        print(sentence1())
                        print(sentence4())
                    else:
                        print(sentence4())
                        print(sentence1())
                    break
                else:
                    print(sentence4())
                    text = random.choice([1,2])
                    if text == 1:
                        print(sentence1())
                        print(sentence2())
                    else:
                        print(sentence2())
                        print(sentence1())
                    break
            else:
                print(sentence4())
                text = random.choice([1,2,3])
                if text == 1:
                    print(sentence1())
                    text = random.choice([2,3])
                    if text == 2:
                        print(sentence2())
                        print(sentence3())
                    else:
                        print(sentence3())
                        print(sentence2())
                    break
                elif text == 2:
                    print(sentence2())
                    text = random.choice([1,3])
                    if text == 1:
                        print(sentence1())
                        print(sentence3())
                    else:
                        print(sentence3())
                        print(sentence1())
                    break
                else:
                    print(sentence3())
                    text = random.choice([1,2])
                    if text == 1:
                        print(sentence1())
                        print(sentence2())
                    else:
                        print(sentence2())
                        print(sentence1())
                    break

make_text()
