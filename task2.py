# python

import csv

''' открытие файла '''
with open("monster_game.csv", encoding="utf8") as f:
    '''преобразование файла в список'''
    r = list(csv.reader(f, delimiter=","))[1:]
    '''сортировка списка вставками'''
    line = 1
    n = r[line]
    while line < len(r):
        if line != 0 and n[1] > r[line - 1][1]:
            r[line] = r[line - 1]
            line -= 1
        else:
            r[line] = n
            line += 1
            if line < len(r):
                n = r[line]
    '''вывод первых трех монстров'''
    for i in range(3):
        print(f"{r[i][0]} имеет возможность: {r[i][1]}, вероятность использования возможности равна {r[i][2]}")
