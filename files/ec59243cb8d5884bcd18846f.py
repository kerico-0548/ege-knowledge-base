# -*- coding: utf-8 -*-
# №8_3 (Уровень: Лёгкий)
# Python: permutations

from itertools import permutations
k = 0
for x in set(permutations("РАДИО",5)):
    s = "".join(x)
    if s[0]!='А' and 'ДО' not in s: k += 1
print(k)
