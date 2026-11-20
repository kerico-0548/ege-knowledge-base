# -*- coding: utf-8 -*-
# №8103 (Уровень: Лёгкий)
# Python: product

from itertools import product
k = 0
for x in product("АБВГД", repeat=6):
    s = "".join(x)
    if "Д" not in s[1:]: k += 1
print(k)
