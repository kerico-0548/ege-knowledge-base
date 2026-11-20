# -*- coding: utf-8 -*-
# №13106 (Уровень: Средний)
# Python / ручной: все непрерывные маски

from ipaddress import *
otvet = []
for p in range(33):
    net = ip_network('52.228.68.36/'+str(p), strict=False)
    if str(net.network_address) == '52.228.64.0':
        otvet.append(p)
print(len(otvet))
