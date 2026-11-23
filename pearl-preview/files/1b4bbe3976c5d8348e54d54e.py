# -*- coding: utf-8 -*-
# Демоверсия ФИПИ 2027 · №5
# Python: bin и список otvet

otvet = []
for n in range(1,1000):
    s = bin(n)[2:]
    s = "11"+s+"11" if n%2==0 else "1"+s+"00"
    r = int(s,2)
    if r>95: otvet.append(r)
print(min(otvet))
