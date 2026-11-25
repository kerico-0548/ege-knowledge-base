# -*- coding: utf-8 -*-
# №13201 Основная волна 2024 (Уровень: Лёгкий)
# Python: ipaddress и перебор

from ipaddress import ip_network
net = ip_network('172.16.128.0/255.255.192.0', False)
k = 0
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1')%2!=0: k += 1
print(k)
