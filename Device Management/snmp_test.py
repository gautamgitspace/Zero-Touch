#!/usr/bin/env python
from easy_snmp import snmp_get, snmp_set, snmp_bulk, snmp_get_next

snmp_get_output = snmp_get('sysName.0', hostname = '172.16.0.1', community = 'public', version = 2)

#snmp get
value = get.value
oid_index = get.oid_index
tokens = get.value.split('.')
print 'Device Name:', tokens[0]
print 'Domain Name:', tokens[1]
print 'Object Identifier Index', oid_index

#snmp walk - a walk through all the interfaces
snmp_walk_output = snmp_walk('1.3.6.1.2.1.2.2.2', hostname = '172.16.0.1', community = 'public', version = 2)
interfaces = []
for item in snmp_walk_output:
    interfaces.append(item.value)
print interfaces

#snmp set operation
snmp_set_output = snmp_set('sysName.0', "Gautam's Macbook Pro", hostname = '172.16.0.1', community = 'public', version = 2)
if snmp_set_output:
    print 'Successfully applied changes'

#snmp set multiple operation
snmp_set_multiple_output = snmp_set([('sysName.0', "Gautam's Macbook Pro"), ('sysContact.0', '9999999'), ('sysLocation.0', 'Aisle2TOR')], hostname = '172.16.0.1', community = 'private', version = 2)
if snmp_set_multiple_output:
    print 'Successfully applied changes'
