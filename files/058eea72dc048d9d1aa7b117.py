# -*- coding: utf-8 -*-
# №8108 (Уровень: Средний) 
# Python: permutations

from itertools import permutations
k = 0
for x in set(permutations("КАЧАЛКА", 7)):
    s = "".join(x)
    if True: k += 1
print(k)
