# -*- coding: utf-8 -*-
# №8_4 (Уровень: Лёгкий)
# Python: permutations

from itertools import permutations
k = 0
for x in set(permutations("ТЕХНАРЬ",7)):
    s = "".join(x)
    if s[0]!='Ь' and all('Ь'+c not in s for c in 'ТНХ'): k += 1
print(k)
