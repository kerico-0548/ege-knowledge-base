# -*- coding: utf-8 -*-
# Открытый вариант ФИПИ 2026 · №2
# Python: вложенные циклы и ручное сопоставление

for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (((z <= x) <= (x == y)) or not w)==False:
                    print(w,x,y,z)
