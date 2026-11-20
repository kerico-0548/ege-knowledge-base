# -*- coding: utf-8 -*-
# №8109 (Уровень: Средний)
# Python: permutations

from itertools import permutations
k = 0
for x in set(permutations("ПЛЮСЫ", 4)):
    s = "".join(x)
    if "СЫ" not in s: k += 1
print(k)
