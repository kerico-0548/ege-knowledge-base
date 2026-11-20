# -*- coding: utf-8 -*-
# №13206 (Уровень: Средний)
# Python: ip_network и перебор двоичных адресов

from ipaddress import *
net = ip_network('192.168.32.160/255.255.255.240', strict=False)
count = 0
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s[:16].count('1') >= s[16:].count('1'):
        count += 1
print(count)
