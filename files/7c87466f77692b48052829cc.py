# -*- coding: utf-8 -*-
# №5_7 ЕГКР 2024 (Уровень: Средний)
# Python: bin и ветви алгоритма

otvet = []
for n in range(1,1000):
    s = bin(n)[2:]
    s += s[-2:] if n%3==0 else bin(3*(n%3))[2:]
    r = int(s,2)
    if r>=195: otvet.append(r)
print(min(otvet))
