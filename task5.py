# python

import csv

'''словарь для хранения классов монстров'''
table = dict()
''' открытие файла '''
with open("monster_game.csv", encoding="utf8") as f:
    '''преобразование файла в список'''
    r = list(csv.reader(f, delimiter=","))[1:]
    ''' заполнение словаря'''
    for line in r:
        table[line[0] + line[1] + line[2]] = line[1]
k = 0
'''вывод первых 10-ти результатов'''
for i in table.keys():
    k += 1
    print(f"{i} - {table[i]}")
    if k == 10:
        break
