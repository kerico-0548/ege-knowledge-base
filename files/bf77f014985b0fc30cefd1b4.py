# -*- coding: utf-8 -*-
# №8_5 (Уровень: Лёгкий)
# Python: product и номер слова

from itertools import product
k = 0
otvet = []
for x in product("АВЛОС",repeat=4):
    k += 1
    s = "".join(x)
    if s[0]=='Л': otvet.append(k)
print(min(otvet))
