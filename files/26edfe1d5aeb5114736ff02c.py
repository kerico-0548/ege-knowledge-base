# -*- coding: utf-8 -*-
# №15303 (Уровень: Лёгкий)
# Python: битовая конъюнкция, поиск контрпримера через flag

otvet = []
for a in range(0, 32):
    flag = False
    for x in range(0, 32):
        if not ((x & a != 0) <= (((x & 17 == 0) and (x & 5 == 0)) <= (x & 3 != 0))):
            flag = True
            break
    if not flag:
        otvet.append(a)
print(max(otvet))
