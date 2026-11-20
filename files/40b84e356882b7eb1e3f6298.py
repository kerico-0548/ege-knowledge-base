# -*- coding: utf-8 -*-
# №15_1 (Уровень: Лёгкий)
# Python: неравенства, поиск контрпримера через flag

otvet = []
for a in range(0, 101):
    flag = False
    for x in range(26):
        for y in range(26):
            if not ((y+2*x < a) or (x > 25) or (y > 25)):
                flag = True
                break
        if flag:
            break
    if not flag:
        otvet.append(a)
print(min(otvet))
