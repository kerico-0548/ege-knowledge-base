# -*- coding: utf-8 -*-
# №8_2 (Уровень: Лёгкий)
# Python: product и номер слова

from itertools import product
k = 0
otvet = []
for x in product("АБЗИ",repeat=4):
    k += 1
    s = "".join(x)
    if s=='ИЗБА': otvet.append(k)
print(min(otvet))
