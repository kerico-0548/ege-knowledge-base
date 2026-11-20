# -*- coding: utf-8 -*-
# №15_2 (Уровень: Лёгкий)
# Python: битовая конъюнкция, поиск контрпримера через flag

otvet = []
for a in range(0, 64):
    flag = False
    for x in range(0, 64):
        if not (((x & 52 != 0) and (x & 36 == 0)) <= (x & a != 0)):
            flag = True
            break
    if not flag:
        otvet.append(a)
print(min(otvet))
