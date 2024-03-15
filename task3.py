# python

import csv

''' открытие файла '''
with open("monster_game.csv", encoding="utf8") as f:
    '''преобразование файла в список'''
    r = list(csv.reader(f, delimiter=","))[1:]
    '''цикл, чтобы программа не прекращала работать'''
    while True:
        ask = input()  # ввод пользователем
        if ask == "хватит":  # выход из программы
            break
        user = int(ask)  # перевод ввода пользователя в int
        k = 0  # счётчик монстров
        '''подсчет монстров'''
        for line in r:
            if int(line[5]) < user and int(line[5]) != 0:
                k += 1
        '''вывод ответа пользователю'''
        if k == 0:
            print("Вы очень слабы. Сходите и наберитесь опыта!")
        else:
            print(f"Вы сможете победить: {k} монстров")
