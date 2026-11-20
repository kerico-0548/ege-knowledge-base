# -*- coding: utf-8 -*-
# №15104 (Уровень: Лёгкий)
# Python: неравенства, поиск контрпримера через flag

otvet = []
for a in range(0, 101):
    flag = False
    for x in range(101):
        for y in range(101):
            if not ((x > a) or (y > a) or (y-2*x+12 != 0)):
                flag = True
                break
        if flag:
            break
    if not flag:
        otvet.append(a)
print(max(otvet))
