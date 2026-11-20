# -*- coding: utf-8 -*-
# №8_8 Демоверсия 2025 (Уровень: Средний)
# Python: product

from itertools import product
k = 0
for x in product("0123456789AB",repeat=5):
    s = "".join(x)
    if s[0]!='0' and s.count('7')==1 and sum(int(c,12)>8 for c in s)<=3: k += 1
print(k)
