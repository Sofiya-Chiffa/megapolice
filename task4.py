# python

import csv

'''словарь для хранения классов монстров и информации о них в формате списка: [кол-во; общая сила]'''
monsters = dict()
''' открытие файла '''
with open("monster_game.csv", encoding="utf8") as f:
    '''преобразование файла в список'''
    r = list(csv.reader(f, delimiter=","))[1:]
    '''заполнение словаря'''
    for line in r:
        monsters.setdefault(line[0].split()[1], [0, 0])
        monsters[line[0].split()[1]][0] += 1
        monsters[line[0].split()[1]][1] += int(line[3])
'''вывод результата'''
for i in monsters.keys():
    print(f"{monsters[i][0]} монстров класса {i}, средняя сила атаки {round(monsters[i][1] / monsters[i][0], 2)}")
