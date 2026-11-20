# -*- coding: utf-8 -*-
# №13107 (Уровень: Средний)
# Python / ручной: все непрерывные маски

from ipaddress import *
otvet = []
for p in range(33):
    net = ip_network('101.196.50.90/'+str(p), strict=False)
    if str(net.network_address) == '101.196.50.80':
        otvet.append(net.num_addresses)
print(max(otvet))
