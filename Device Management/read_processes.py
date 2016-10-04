#!/usr/bin/env python
import paramiko

fname = '/Users/Gautam/Desktop/ps_aux_out2.txt'
server = "timberlake.cse.buffalo.edu"
session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect(server, username = "****", password = "****")
filehandle = open(fname, 'w+')
(stdin, stdout, stderr) = session.exec_command("ps aux")
outlines = stdout.readlines()
response = ''.join(outlines)

filehandle.write(resp)
d = {}
most_common_user_name = None
most_common_user_process_count = None
filehandle2 = open(fname)
for line in filehandle2:
    extract = line.strip().split()
    user = extract[0]
    if user not in d:
        d[user] = 1
    else:
        d[user] = d[user] + 1
for key, value in d.items():
    if most_common_user_name is None or value > most_common_user_process_count:
        most_common_user_name = key
        most_common_user_process_count = value

print 'User: ', most_common_user_name, 'has: ', most_common_user_process_count, 'processes running on', server
for key, value in d.items():
    if key == '****':
        print key, 'has', value, 'processes running on', server
