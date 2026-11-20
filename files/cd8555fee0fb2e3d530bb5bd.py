# -*- coding: utf-8 -*-
# №5_1 (Уровень: Очень лёгкий)
# Python: bin и ветви алгоритма

otvet = []
for n in range(1,109):
    s = bin(n)[2:]
    s += '01' if n%2 else '10'
    r = int(s,2)
    if r<109: otvet.append(r)
print(max(otvet))
