# -*- coding: utf-8 -*-
# №13203 ЕГКР 2024 (Уровень: Лёгкий)
# Python: ipaddress и перебор

from ipaddress import ip_network
net = ip_network('112.208.0.0/255.255.128.0', False)
k = 0
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1')%11==0: k += 1
print(k)
