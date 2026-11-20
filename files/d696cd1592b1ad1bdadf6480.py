# -*- coding: utf-8 -*-
# №8105 (Уровень: Лёгкий)
# Python: product для нескольких длин

from itertools import product
k = 0
for n in range(3,6):
    for x in product("МБАПЕ", repeat=n):
        k += 1
print(k)
