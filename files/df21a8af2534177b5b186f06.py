# -*- coding: utf-8 -*-
# №8111 (Уровень: Средний)
# Python: permutations

from itertools import permutations
k = 0
for x in set(permutations("ПЕТРОВИЧ",6)):
    s = "".join(x)
    if s[1]!='О' and 'ОЕ' not in s and 'ОИ' not in s: k += 1
print(k)
