# -*- coding: utf-8 -*-
# №15404 (Уровень: Средний)
# Python: множества, добавление обязательных элементов

from math import prod
p = set(range(2, 29, 2))
q = set(range(3, 31, 3))
r = {3, 6, 12, 24, 30, 36, 48}
a = set()
for x in range(0, 49):
    if not ((x not in a) <= (((x in q) and (x in r)) <= (x in p))):
        a.add(x)
print(prod(a))
