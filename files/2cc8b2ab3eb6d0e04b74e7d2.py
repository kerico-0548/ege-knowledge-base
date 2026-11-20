# -*- coding: utf-8 -*-
# №15101 (Уровень: Лёгкий)
# Python: неравенства, поиск контрпримера через flag

otvet = []
for a in range(0, 401):
    flag = False
    for x in range(12):
        for y in range(34):
            if not ((x >= 12) or (3*x < y) or (x*y < a)):
                flag = True
                break
        if flag:
            break
    if not flag:
        otvet.append(a)
print(min(otvet))
