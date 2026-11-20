# -*- coding: utf-8 -*-
# №8203 Апробация 2023 (Уровень: Очень лёгкий)
# Python: product и номер слова

from itertools import product
k = 0
otvet = []
for x in product("АВОРТ",repeat=6):
    k += 1
    s = "".join(x)
    if s=='ВОРОТА': otvet.append(k)
print(min(otvet))
