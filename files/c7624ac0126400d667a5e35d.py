# -*- coding: utf-8 -*-
# №13208 (Уровень: Средний) Пересдача 03.07.25
# Python: крайний адрес узла

from ipaddress import *
net = ip_network('102.162.200.51/255.255.255.0', strict=False)
ip = net[-2]
print(sum(map(int, str(ip).split('.'))))
