# -*- coding: utf-8 -*-
# №13101 (Уровень: Очень лёгкий)
# Python / ручной: адрес сети и число единиц

from ipaddress import *
net = ip_network('179.136.219.36/255.255.240.0', strict=False)
print(bin(int(net.network_address))[2:].count('1'))
