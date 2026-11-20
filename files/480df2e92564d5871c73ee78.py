# -*- coding: utf-8 -*-
# №15_10 (Уровень: Средний)
# Python: делимость, поиск контрпримера через flag

otvet = []
for a in range(1, 301):
    flag = False
    for x in range(0, 106):
        if not (((x % a != 0) and (x % 35 == 0)) <= ((x % 21 != 0) or (x % 35 != 0))):
            flag = True
            break
    if not flag:
        otvet.append(a)
print(max(otvet))
