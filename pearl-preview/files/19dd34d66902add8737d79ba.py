# -*- coding: utf-8 -*-
# Демоверсия ФИПИ 2027 · №2
# Python: вложенные циклы и ручное сопоставление

for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (((x == (not y)) <= (not(w <= x))) or not z)==False:
                    print(w,x,y,z)
