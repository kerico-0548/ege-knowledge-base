# -*- coding: utf-8 -*-
# №5106 (Уровень: Очень лёгкий)
# Python: bin, преобразование строки, список otvet

otvet = []
for n in range(1, 1000):
    s = bin(n)[2:]
    s += '00' if n%2==0 else '11'
    r = int(s, 2)
    if r <= 126: otvet.append(r)
print(max(otvet))
