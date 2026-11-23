# -*- coding: utf-8 -*-
# №15105 (Уровень: Лёгкий)
# Python: неравенства, поиск контрпримера через flag

otvet = []
for a in range(0, 101):
    flag = False
    for x in range(40):
        for y in range(40):
            if not ((39 != y+2*x) or (a < x) or (a < y)):
                flag = True
                break
        if flag:
            break
    if not flag:
        otvet.append(a)
print(max(otvet))
