# -*- coding: utf-8 -*-
# №15_8 (Уровень: Лёгкий)
# Python: делимость, поиск контрпримера через flag

otvet = []
for a in range(1, 101):
    flag = False
    for x in range(1, 101):
        if not (((x % 2 == 0) <= (x % 3 != 0)) or (x+a >= 100)):
            flag = True
            break
    if not flag:
        otvet.append(a)
print(min(otvet))
