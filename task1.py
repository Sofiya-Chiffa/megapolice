# python

import csv

''' создание переменных для хранения максимумов
reg - регенерация
dopst - дополнительный ход
pow - усиление атаки'''
reg, dopst, pow = 0, 0, 0

''' открытие файла и нахождение максимумов '''
with open("monster_game.csv", encoding="utf8") as f:
    r = list(csv.reader(f, delimiter=","))[1:]
    #
    for line in r:
        if line[1] == "регенерация":
            reg = max(reg, int(line[5]) * int(line[2]) / 100)
        if line[1] == "усиление атаки":
            pow = max(pow, int(line[3]) * int(line[2]) / 100)
        if line[1] == "дополнительный ход":
            s = int(line[3]) + int(line[4]) + int(line[5]) + int(line[6])
            dopst = max(dopst, s * int(line[2]) / 100)

''' вывод ответа'''
print("Регенерация:", reg)

''' создание нового файла '''
with open("monster_opportunity.csv", "w", newline="", encoding="utf8") as newf:
    w = csv.writer(newf, delimiter=",")
    w.writerow(["opportunity", 'power'])
    w.writerow(["регенерация", reg])
    w.writerow(["дополнительный ход", dopst])
    w.writerow(["усиление атаки", pow])
