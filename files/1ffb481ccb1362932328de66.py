# -*- coding: utf-8 -*-
# №8115 Резервный день 19.06.25 (Уровень: Средний)
# Python: product

from itertools import product
k = 0
for x in product("0123456", repeat=5):
    s = "".join(x)
    if s[0]!="0" and s.count("6")==1 and all(s[i]!=s[i+1] for i in range(4)): k += 1
print(k)
