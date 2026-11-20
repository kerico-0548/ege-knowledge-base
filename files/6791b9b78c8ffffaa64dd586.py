# -*- coding: utf-8 -*-
# №13_4 Демоверсия 2025 (Уровень: Средний)
# Python: ip_network и перебор двоичных адресов

from ipaddress import *
net = ip_network('172.16.168.0/255.255.248.0', strict=False)
count = 0
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1') % 5 != 0:
        count += 1
print(count)
