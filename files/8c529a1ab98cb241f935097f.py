# -*- coding: utf-8 -*-
# №13_1 (Уровень: Легкий)​​
# Python / ручной: все непрерывные маски

from ipaddress import *
otvet = []
for p in range(33):
    net = ip_network('111.81.93.127/'+str(p), strict=False)
    if str(net.network_address) == '111.81.80.0':
        otvet.append(int(str(net.netmask).split('.')[2]))
print(min(otvet))
