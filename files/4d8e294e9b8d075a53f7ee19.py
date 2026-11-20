# -*- coding: utf-8 -*-
# №15603 (Уровень: Лёгкий)
# Python: делимость, поиск контрпримера через flag

otvet = []
for a in range(1, 45):
    flag = False
    for x in range(1, 51):
        if not ((x % a == 0) or ((40 <= x <= 50) <= (x % 11 != 0))):
            flag = True
            break
    if not flag:
        otvet.append(a)
print(max(otvet))
