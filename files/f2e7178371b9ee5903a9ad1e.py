# -*- coding: utf-8 -*-
# №8101 (Уровень: Очень лёгкий)
# Python: product

from itertools import product
k = 0
for x in product("ЗИМА", repeat=4):
    s = "".join(x)
    if s[0] in "ИА": k += 1
print(k)
