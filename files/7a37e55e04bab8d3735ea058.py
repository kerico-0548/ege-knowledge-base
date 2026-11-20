# -*- coding: utf-8 -*-
# №13105 (Уровень: Средний)
# Python / ручной: все непрерывные маски

from ipaddress import *
otvet = []
for p in range(33):
    net = ip_network('162.212.58.192/'+str(p), strict=False)
    if str(net.network_address) == '162.212.0.0':
        otvet.append(p)
print(max(otvet))
