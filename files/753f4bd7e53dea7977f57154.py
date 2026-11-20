# -*- coding: utf-8 -*-
# №15_9 (Уровень: Лёгкий)
# Python: делимость, поиск контрпримера через flag

otvet = []
for a in range(1, 13):
    flag = False
    for x in range(1, 13):
        if not ((x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0))):
            flag = True
            break
    if not flag:
        otvet.append(a)
print(max(otvet))
