# -*- coding: utf-8 -*-
# №8_1 Демоверсия 2021 (Уровень: Лёгкий)
# Python: product

from itertools import product
k = 0
for x in product("ШКОЛА",repeat=3):
    s = "".join(x)
    if s.count('К')==1: k += 1
print(k)
