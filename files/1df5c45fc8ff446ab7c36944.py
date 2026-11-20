# -*- coding: utf-8 -*-
# №13103 (Уровень: Лёгкий)
# Python / ручной: все непрерывные маски

from ipaddress import *
otvet = []
for p in range(33):
    net = ip_network('117.191.37.176/'+str(p), strict=False)
    if str(net.network_address) == '117.191.37.160':
        otvet.append(int(str(net.netmask).split('.')[3]))
print(min(otvet))
