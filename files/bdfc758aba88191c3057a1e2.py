# -*- coding: utf-8 -*-
# Открытый вариант ФИПИ 2026 · №5
# Python: bin и список otvet

otvet = []
for n in range(1,1000):
    s = bin(n)[2:]
    s = "10"+(s+"0")[2:] if s.count("1")%2==0 else "11"+(s+"1")[2:]
    r = int(s,2)
    if r<=19: otvet.append(n)
print(max(otvet))
