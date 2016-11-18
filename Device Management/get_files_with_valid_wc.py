#!/usr/bin/env python
# downloads files from the remotepath directory of the remote server to home directory of local machine
import paramiko
import time
import os
from scp import SCPClient

fname = "/Users/Gautam/Desktop/ls_out.txt"
fwc = "/Users/Gautam/Desktop/wc_out.txt"

#YOUR REMOTE SERVER NAME
server = "timberlake.cse.buffalo.edu"
#YOUR DIRECTORY TO SAVE DONWLOADED FILES
home = "/Users/Gautam/Desktop/vm/"
#PATH DIRECTORY TO DOWNLOAD FROM
remotepath = "/home/csgrad/agautam2/testfolder/"

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect(server, username = "agautam2", password = "****")
filehandle = open(fname, 'w+')
(stdin, stdout, stderr) = session.exec_command("ls " + remotepath)
outlines = stdout.readlines()
response = ''.join(outlines)
filehandle.write(response)
print 'Writing Directory Contents to File...'
time.sleep(1)
print 'Reading Directory Contents from file...'
time.sleep(2)
print 'Calculating wc for files...'
filehandle = open(fname)
for line in filehandle:
    extract = line.strip()
    (stdin, stdout, stderr) = session.exec_command("cd "+remotepath+"; "+ "wc -w "+extract)
    outlines = stdout.readlines()
    response = ''.join(outlines)
    wcHandleOut = open(fwc, 'a')
    wcHandleOut.write(response)

print 'Done'
time.sleep(1)
print 'Downloading files with valid WC:'
time.sleep(2)
filehandle = open(fwc)
i=0
for i, line in enumerate(filehandle):
    tokens = line.strip().split()
    if int(tokens[0]) > 0:
        print 'Downloading: ',tokens[1], 'with size', tokens[0]
        sftp = SCPClient(session.get_transport())
        sftp.get(remotepath+tokens[1], home)
        i = i+1;


print '[Download Complete]'
time.sleep(2)
print 'Saved', i, 'files from ', server, 'to', home
