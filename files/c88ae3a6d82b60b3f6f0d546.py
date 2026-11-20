# -*- coding: utf-8 -*-
# №15103 Апробация 2023 (Уровень: Лёгкий)
# Python: неравенства, поиск контрпримера через flag

otvet = []
for a in range(0, 101):
    flag = False
    for x in range(1, 101):
        for y in range(1, 101):
            if not ((x+y <= 32) or (y <= x+4) or (y >= a)):
                flag = True
                break
        if flag:
            break
    if not flag:
        otvet.append(a)
print(max(otvet))
