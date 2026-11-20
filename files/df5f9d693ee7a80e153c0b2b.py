# -*- coding: utf-8 -*-
# №5_10 Основная волна 2023 (Уровень: Повышенный)
# Python: перевод остатками и список otvet

def perevod(n, b):
    s = ''
    while n>0:
        s = str(n%b)+s
        n //= b
    return s or '0'
otvet = []
for n in range(1,199):
    s = perevod(n,3)
    if n%3==0: s = '1'+s+'02'
    else: s += perevod(4*(n%3),3)
    r = int(s,3)
    if r<199: otvet.append((r,n))
print(max(n for r,n in otvet))
