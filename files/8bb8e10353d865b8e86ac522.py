# -*- coding: utf-8 -*-
# №15_7 (Уровень: Лёгкий)
# Python: битовая конъюнкция, поиск контрпримера через flag

otvet = []
for a in range(0, 16):
    flag = False
    for x in range(0, 16):
        if not ((x & a != 0) <= ((x & 12 == 0) <= (x & 5 != 0))):
            flag = True
            break
    if not flag:
        otvet.append(a)
print(max(otvet))
