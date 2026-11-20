# -*- coding: utf-8 -*-
# №5108 (Уровень: Средний)
# Python: bin, преобразование строки, список otvet

otvet = []
for n in range(1, 1000):
    s = bin(n)[2:]
    s += s[-3:] if n%3==0 else bin(3*(n%3))[2:]
    r = int(s, 2)
    if r < 100: otvet.append(n)
print(max(otvet))
