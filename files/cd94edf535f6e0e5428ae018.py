# -*- coding: utf-8 -*-
# №14108 Открытый вариант (Уровень: Средний)
# Python: перебор параметра и цифр

otvet = []
for x in range(1, 2031):
    a = 3**100-x
    k = 0
    while a > 0:
        if a % 3 == 0: k += 1
        a //= 3
    if k == 5: otvet.append(x)
print(max(otvet))
