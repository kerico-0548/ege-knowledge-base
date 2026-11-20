# -*- coding: utf-8 -*-
# №2_13 СтатГрад (Уровень: Сложный)
# Python + ручное сопоставление таблицы

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = int(bool((w == x) and (y <= z)))
                f2 = int(bool((w <= x) <= (y == z)))
                print(x, y, z, w, f1, f2)
