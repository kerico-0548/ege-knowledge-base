# -*- coding: utf-8 -*-
# Открытый вариант ФИПИ 2026 · №8
# Python: product и номер слова

from itertools import product
k = 0
for x in product("АЕЛПРЬ",repeat=6):
    k += 1
    s = "".join(x)
    if k%2==1 and s[0] not in "АЛ" and s.count("П")>=2:
        print(k)
        break
