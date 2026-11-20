# -*- coding: utf-8 -*-
# №5_9 (Уровень: Средний-Повышенный)
# Python: срезы двоичной записи

for n in range(2,1025):
    s = bin(n)[2:]
    r = abs(s[1::2].count('1')-s[0::2].count('0'))
    if r==5:
        print(n)
        break
