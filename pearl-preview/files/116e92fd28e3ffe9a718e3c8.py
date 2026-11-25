# -*- coding: utf-8 -*-
# №2207 Демоверсия 2022 (Уровень: Средний)
# Python + ручное сопоставление таблицы

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = int(bool((not (y <= (x == w))) and (z <= x)))
                if f1 == 1:
                    print(x, y, z, w, f1)
