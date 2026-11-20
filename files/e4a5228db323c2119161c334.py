# -*- coding: utf-8 -*-
# №15_11 (Уровень: Средний)
# Python: делимость, поиск контрпримера через flag

otvet = []
for a in range(1, 53):
    flag = False
    for x in range(1, 61):
        if not ((x % a == 0) or ((50 <= x <= 60) <= (x % 13 != 0))):
            flag = True
            break
    if not flag:
        otvet.append(a)
print(max(otvet))
