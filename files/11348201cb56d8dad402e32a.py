# -*- coding: utf-8 -*-
# №13_7 (Уровень: Средний)​​
# Python / ручной: все непрерывные маски

from ipaddress import *
otvet = []
for p in range(33):
    net = ip_network('118.85.170.23/'+str(p), strict=False)
    if str(net.network_address) == '118.85.168.0':
        otvet.append(p)
print(min(otvet))
