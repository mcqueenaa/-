import re

forms = []
words = []
with open ('text.txt', 'r', encoding = 'utf-8') as t:
    texxt = t.read()
    texxt = texxt.lower()
words = texxt.split()
for i in range(len(words)): 
    words[i] = words[i].strip('”“".,!?')
    
prog = r"\b[п]рограммир(ова(в(ш((ий|ая|ее)(ся)?|и(сь)?))?|ть|л(ся|[аои](сь)?)?)|у(ю(сь|(т|щий|щая|щее)(ся)?)?|е((шь|т|м)(ся)?|те(сь)?)|я(сь)?))\b"

for i in range(len(words)):
    if re.search(prog,words[i]) != None:
        if words[i] not in forms:
            forms.append(words[i])


print('В тексте встретились такие формы глагола "программировать":  ' + ', '.join(forms) + '.')
