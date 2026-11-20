# -*- coding: utf-8 -*-
# №8206 (Уровень: Средний)
# Python: product

from itertools import product
k = 0
for x in product("АЛПЦЯ",repeat=5):
    s = "".join(x)
    if s.count('А')<=1 and s.count('Ц')==2 and 'Л' not in s: k += 1
print(k)
