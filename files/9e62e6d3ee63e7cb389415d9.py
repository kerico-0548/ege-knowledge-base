# -*- coding: utf-8 -*-
# №8_12 (Уровень: Средний)
# Python: permutations

from itertools import permutations
k = 0
for x in set(permutations("0123456789",5)):
    s = "".join(x)
    if s[0]!='0' and int(s)%5==0 and all(int(s[i])%2!=int(s[i+1])%2 for i in range(4)): k += 1
print(k)
