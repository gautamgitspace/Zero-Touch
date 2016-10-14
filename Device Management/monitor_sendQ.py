#!/usr/bin/env python
#network congestion detection using netstat
import os
import re
from itertools import islice

os.system("netstat -p tcp > /Users/Gautam/Desktop/netstat_output.txt")
filehandle = open("/Users/Gautam/Desktop/netstat_output.txt")
for line in islice(filehandle,2,200):
    recvQ = []
    #regex for 2 or more white space characters
    token = re.sub('\s{2,}', ' ', line.strip()).split(' ')
    if int(token[1]) > 100 or int(token[2]) > 100:
        print 'recvQ:   ', token[1], '  ', 'sendQ:    ', token [2], '   ' , 'src: ', token[3], ' ',  'dst:  ', token[4]
