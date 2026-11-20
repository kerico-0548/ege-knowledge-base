# -*- coding: utf-8 -*-
# №8110 (Уровень: Средний)
# Python: permutations

from itertools import permutations
k = 0
for x in set(permutations("ЗАРЯД",5)):
    s = "".join(x)
    if all((s[i] in 'АЯ') != (s[i+1] in 'АЯ') for i in range(4)): k += 1
print(k)
