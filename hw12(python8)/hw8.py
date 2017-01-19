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
                print("Вы угадали!!!")
                break
            print('Вы не угадали.')
            if i != len(puzzle[key]) - 1:
                guess = input('Попробуйте еще раз: ')
        print('Игра окончена.')
        break

trytoguess()
