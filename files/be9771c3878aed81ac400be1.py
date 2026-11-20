# -*- coding: utf-8 -*-
# №8113 (Уровень: Средний)
# Python: permutations

from itertools import permutations
k = 0
for x in set(permutations("012345678",7)):
    s = "".join(x)
    if s[0]!='0' and all(int(s[i])%2!=int(s[i+1])%2 for i in range(6)): k += 1
print(k)
