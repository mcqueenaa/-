import re
from math import log

punct = '[.,!«»?&@"$\[\]\(\):;%#&\'—-]'

def preprocessing(text):
    text_wo_punct = re.sub(punct, '', text.lower())
    words = text_wo_punct.strip().split()
    return words

import os
anek = ''
teh = ''
izvest = ''
for root, dirs, files in os.walk('texts'):
    for f in files:
        if 'anekdots' in root:
            num_anek = len(files)
            anek += open(os.path.join(root, f), encoding='utf-8').read()
        elif 'izvest' in root:
            num_izvest = len(files)
            izvest += open(os.path.join(root, f), encoding='utf-8').read()
        elif 'teh_mol' in root:
            num_teh = len(files)
            teh += open(os.path.join(root, f), encoding='utf-8').read()
            
words_anek = preprocessing(anek)
words_teh = preprocessing(teh)
words_izvest = preprocessing(izvest)

words = words_anek + words_teh + words_izvest

def freq_dict(arr):
    dic = {}
    for element in arr:
        if element in dic:
            dic[element] += 1
        else:
            dic[element] = 1
    return dic

corpus_freq = freq_dict(words)
anek_freq = freq_dict(words_anek)
izvest_freq = freq_dict(words_izvest)
teh_freq = freq_dict(words_teh)

def pmi_for_cats(x, y):
    if y == 'anek':
        dic = anek_freq
        num = num_anek
    elif y == 'teh':
        dic = teh_freq
        num = num_teh
    elif y == 'izvest':
        dic = izvest_freq
        num = num_izvest
    p_xy = dic[x]/len(dic)
    p_x, p_y = corpus_freq[x]/len(corpus_freq), num/(num_izvest + num_teh + num_anek)
    pmi = log(p_xy/(p_x * p_y))
    return pmi

cat_pmi = {}
i = 0
for word in corpus_freq:
    if i > 100:
        break
    try:
        pmi_anek = pmi_for_cats(word, 'anek') #try: код который мы хотим исполнить // except: что делать если код упал (чтобы при ошибке запускался другой код)
    except KeyError: ##после except через запятую можем писать типы ошибок, которые мы игнорируем
        pmi_anek = 0
    try:
        pmi_teh = pmi_for_cats(word, 'teh')
    except KeyError:
        pmi_teh = 0
    try:
        pmi_izvest = pmi_for_cats(word, 'izvest')
    except KeyError:
        pmi_izvest = 0
    max_pmi = max(pmi_anek, pmi_teh, pmi_izvest)
    if max_pmi == 0:
        continue
    if max_pmi == pmi_anek:
        cat = 'anek'
    elif max_pmi == pmi_teh:
        cat = 'teh'
    elif max_pmi == pmi_izvest:
        cat = 'izvest'
    print(word, cat)
    i += 1
