# -*- coding: utf-8 -*-
# №13202 Основная волна 2024  (Уровень: Лёгкий)
# Python: ipaddress и перебор

from ipaddress import ip_network
net = ip_network('112.160.0.0/255.240.0.0', False)
k = 0
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1')%3!=0: k += 1
print(k)
