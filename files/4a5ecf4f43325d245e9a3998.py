# -*- coding: utf-8 -*-
# №8102 (Уровень: Очень лёгкий)
# Python: product

from itertools import product
k = 0
for x in product("РУЧКА", repeat=5):
    s = "".join(x)
    if s[0] in "РЧК" and s[-1] in "РЧК": k += 1
print(k)
