# -*- coding: utf-8 -*-
# №2201 Досрочная волна 2023 (Уровень: Лёгкий)
# Python + ручное сопоставление таблицы

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = int(bool((x and (not y)) or (y == z) or (not w)))
                if f1 == 0:
                    print(x, y, z, w, f1)
