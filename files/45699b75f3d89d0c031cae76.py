# -*- coding: utf-8 -*-
# №8106 (Уровень: Лёгкий)
# Python: product

from itertools import product
k = 0
for x in product("КОВТН", repeat=5):
    s = "".join(x)
    if s.count("О")>=2 and "Т" not in s[:-1]: k += 1
print(k)
