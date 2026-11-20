# -*- coding: utf-8 -*-
# №13207 Демоверсия 2026 (Уровень: Средний)
# Python: крайний адрес узла

from ipaddress import *
net = ip_network('191.128.66.83/255.192.0.0', strict=False)
ip = net[-2]
print(str(ip).replace('.', ''))
