# -*- coding: utf-8 -*-
# №15401 (Уровень: Лёгкий)
# Python: множества и дополнение A

p = {1,2,4,5,8,11,13,15,21}
q = {2,3,4,5,6,8,15,25}
a = set()
for x in range(100):
    if ((x in p) <= ((x not in q) or (x in a)))==False:
        a.add(x)
print(len(a))
