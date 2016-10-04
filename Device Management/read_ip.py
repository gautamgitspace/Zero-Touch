#!/usr/bin/env python
fname = '/path/to/your/file'
filehandle = open(fname)
d = {}
most_common_ip_name = None
most_common_ip_count = None
for line in filehandle:
    extract = line.strip().split('  ')
    IP = extract[0]
    if IP not in d:
        d[IP] = 1
    else:
        d[IP] = d[IP] + 1
for key, value in d.items():
    if most_common_ip_name is None or value > most_common_ip_count:
        most_common_ip_name = key
        most_common_ip_count = value

print 'IP: ', most_common_ip_name, 'occurs: ', most_common_ip_count, 'times'
