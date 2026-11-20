# -*- coding: utf-8 -*-
# №8104 (Уровень: Очень лёгкий)
# Python: product

from itertools import product
k = 0
for x in product("ГУРИК", repeat=6):
    s = "".join(x)
    if s.count("У")==1: k += 1
print(k)
