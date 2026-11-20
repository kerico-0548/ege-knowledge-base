# -*- coding: utf-8 -*-
# №13_6 (Уровень: Средний)​​
# Python / ручной: все непрерывные маски

from ipaddress import *
otvet = []
for p in range(33):
    net = ip_network('117.191.208.37/'+str(p), strict=False)
    if str(net.network_address) == '117.191.192.0':
        otvet.append(int(str(net.netmask).split('.')[2]))
print(min(otvet))
