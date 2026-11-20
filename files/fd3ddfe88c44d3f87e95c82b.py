# -*- coding: utf-8 -*-
# №8_10 Основная волна 2024 (Уровень: Средний)
# Python: product

from itertools import product
k = 0
for x in product("01234567",repeat=5):
    s = "".join(x)
    if s[0] in '246' and s[-1] not in '26' and s.count('7')<=2: k += 1
print(k)
