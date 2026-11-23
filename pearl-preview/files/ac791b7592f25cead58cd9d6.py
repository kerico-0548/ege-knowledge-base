# -*- coding: utf-8 -*-
# №8_7 ЕГКР 2024 (Уровень: Лёгкий-Средний)
# Python: product

from itertools import product
k = 0
for x in product("0123456",repeat=7):
    s = "".join(x)
    if s[0]!='0' and sum(c in '0246' for c in s)==2: k += 1
print(k)
