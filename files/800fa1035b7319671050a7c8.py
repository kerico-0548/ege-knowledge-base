# -*- coding: utf-8 -*-
# №5_5 (Уровень: Средний)
# Python: bin и ветви алгоритма

otvet = []
for n in range(1,1000):
    s = bin(n)[2:]
    s = '1'+s+'00' if n%2==0 else s+bin(s.count('1'))[2:]
    r = int(s,2)
    if r>190: otvet.append(n)
print(min(otvet))
