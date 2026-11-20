# -*- coding: utf-8 -*-
# №8_15 (Уровень: Средний-Повышенный)
# Python: permutations

from itertools import permutations
k = 0
for x in set(permutations("МАШИНА",6)):
    s = "".join(x)
    if all(not (s[i] in 'АИ' and s[i+1] in 'АИ') for i in range(5)): k += 1
print(k)
