# -*- coding: utf-8 -*-
# №13102 (Уровень: Лёгкий)
# Python / ручной: все непрерывные маски

from ipaddress import *
otvet = []
for p in range(33):
    net = ip_network('117.211.93.102/'+str(p), strict=False)
    if str(net.network_address) == '117.211.88.0':
        otvet.append(int(str(net.netmask).split('.')[2]))
print(min(otvet))
