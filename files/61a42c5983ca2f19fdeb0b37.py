# -*- coding: utf-8 -*-
# №14_7 Демоверсия 2025 (Уровень: Средний)
# Python: перебор параметра и цифр

otvet = []
for x in range(1, 2031):
    a = 7**170+7**100-x
    k = 0
    while a > 0:
        if a % 7 == 0: k += 1
        a //= 7
    if k == 71: otvet.append(x)
print(max(otvet))
