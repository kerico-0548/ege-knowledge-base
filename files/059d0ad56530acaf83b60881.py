# -*- coding: utf-8 -*-
# №8112 Апробация 2023 (Уровень: Средний)
# Python: product

from itertools import product
k = 0
for x in product("012345678",repeat=7):
    s = "".join(x)
    if s[0] in '2468' and s[-1] in '1357' and s.count('8')==1: k += 1
print(k)
