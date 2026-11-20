# -*- coding: utf-8 -*-
# №8107 (Уровень: Лёгкий)
# Python: product

from itertools import product
k = 0
for x in product("УЧЕБНИК",repeat=5):
    s = "".join(x)
    if s[0]!='Ч' and s[-1]!='Ч' and any(c in 'УЕИ' for c in s): k += 1
print(k)
