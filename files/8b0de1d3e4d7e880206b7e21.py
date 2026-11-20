# -*- coding: utf-8 -*-
# №13109 Открытый вариант 2024 (Уровень: Средний)
# Python: ip_network и перебор двоичных адресов

from ipaddress import *
net = ip_network('122.159.136.144/255.255.255.248', strict=False)
count = 0
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1') % 4 != 0:
        count += 1
print(count)
