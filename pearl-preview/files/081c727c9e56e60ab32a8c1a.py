# -*- coding: utf-8 -*-
# Демоверсия ФИПИ 2027 · №14
# Python: системы счисления

for x in "0123456789ABCDEFGHIJKL":
    a = int("27"+x+"98876",22)+int("26"+x+"51",22)+int("711"+x+"5",22)
    if a%21==0:
        print(a//21)
        break
