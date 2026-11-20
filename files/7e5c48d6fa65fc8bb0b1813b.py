# -*- coding: utf-8 -*-
# Демоверсия ФИПИ 2027 · №13
# Ручной / Python: маска сети

from ipaddress import ip_network
net = ip_network("95.106.135.150/255.255.255.0",False)
print(sum(map(int,str(net.network_address).split("."))))
