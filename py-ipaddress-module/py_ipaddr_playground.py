#!/usr/bin/env python3

import ipaddress

subnets = list(ipaddress.ip_network('192.168.10.0/24'))
for index, items in enumerate(subnets):
    print (items)
    if index == 10:
        break
print ('done printing first 10')

print ('Now printing last 10')

for i in range(len(subnets)-1, len(subnets)-10, -1):
    print (subnets[i])

v4nets = list(ipaddress.ip_network('21.45.55.0/24').subnets(new_prefix=28))
for items in v4nets:
    print (items.with_netmask)
