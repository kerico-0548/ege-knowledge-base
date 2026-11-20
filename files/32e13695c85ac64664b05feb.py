# -*- coding: utf-8 -*-
# №13205 (Уровень: Лёгкий)
# Python: ip_network и перебор двоичных адресов

from ipaddress import *
net = ip_network('176.16.128.0/255.255.192.0', strict=False)
count = 0
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('100') == 3:
        count += 1
print(count)
