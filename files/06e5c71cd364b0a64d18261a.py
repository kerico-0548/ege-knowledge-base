# -*- coding: utf-8 -*-
# №8_14 ЕГКР 2023 (Уровень: Средний)
# Python: product

from itertools import product
k = 0
for x in product("012345678",repeat=5):
    s = "".join(x)
    if s[0]!='0' and s.count('5')==1 and all(s[i]!=s[i+1] for i in range(4)): k += 1
print(k)
