# -*- coding: utf-8 -*-
# №13204 (Уровень: Лёгкий)
# Python: ipaddress и перебор

from ipaddress import ip_network
net = ip_network('176.16.128.0/255.255.192.0', False)
k = 0
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if '1101' not in s: k += 1
print(k)
