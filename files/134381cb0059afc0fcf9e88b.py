# -*- coding: utf-8 -*-
# №8114 (Уровень: Средний)
# Python: product

from itertools import product
k = 0
for x in product("012345", repeat=6):
    s = "".join(x)
    if s[0]!="0" and sum(map(int,s[:3]))>sum(map(int,s[3:])): k += 1
print(k)
