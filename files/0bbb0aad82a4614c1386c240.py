# -*- coding: utf-8 -*-
# №2_3 Демоверсия 2025 (Уровень: Средний)
# Python + ручное сопоставление таблицы

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = int(bool(((w <= y) <= x) or (not z)))
                if f1 == 0:
                    print(x, y, z, w, f1)
