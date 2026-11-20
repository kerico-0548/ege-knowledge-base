# -*- coding: utf-8 -*-
# №13_5 ​​Пересдача 2024 (Уровень: Средний)
# Python: ip_network и перебор двоичных адресов

from ipaddress import *
net = ip_network('115.192.0.0/255.192.0.0', strict=False)
count = 0
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1') % 3 != 0:
        count += 1
print(count)
