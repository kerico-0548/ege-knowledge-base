# -*- coding: utf-8 -*-
# №15_6 (Уровень: Лёгкий)
# Python: неравенства, поиск контрпримера через flag

otvet = []
for a in range(0, 101):
    flag = False
    for x in range(0, 101):
        for y in range(0, 101):
            if not ((x*y > a) or (x > y) or (8 >= x)):
                flag = True
                break
        if flag:
            break
    if not flag:
        otvet.append(a)
print(max(otvet))
