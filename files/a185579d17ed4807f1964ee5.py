# -*- coding: utf-8 -*-
# №13_3 (Уровень: Лёгкий) Авторская​​
# Python: размер сети

from ipaddress import *
net = ip_network('192.168.32.160/255.255.255.192', strict=False)
print(net.num_addresses)
