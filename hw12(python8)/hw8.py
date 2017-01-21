## 3 вариант

def makepuzzle(words):
    puzzle = {}
    strings = []
    word = []
    with open (words, 'r', encoding = 'utf-8') as w:
        strings = w.readlines()
        for i in range(len(strings)):
            strings[i] = strings[i].strip('\n')        
    for i in range(len(strings)):
        word = strings[i].split(';')
        puzzle[word[0]] = word[1]
    return puzzle

def trytoguess():
    puzzle = makepuzzle('words.csv')

    for key in puzzle:
        print(puzzle[key], '...')
        guess = input('Дополните это словосочетание: ')
        for i in range(len(puzzle[key])):
            if guess == key:
                print("Вы угадали!!! Это" , '"' + puzzle[key] , key + '".')
                break
            guess = input('Вы не угадали, попробуйте еще раз: ')
        if i == len(puzzle[key]) - 1:
            print('Вы проиграли.')
        
trytoguess()
