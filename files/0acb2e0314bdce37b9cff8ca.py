# -*- coding: utf-8 -*-
# №8_13 (Уровень: Средний)
# Python: product

from itertools import product
k = 0
for x in product("012345",repeat=6):
    s = "".join(x)
    if s[0]!='0' and s.count('2')==1 and all(p not in s for p in ('12','21','32','23','52','25')): k += 1
print(k)
