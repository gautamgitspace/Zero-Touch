#!/usr/bin/python

def _unpack(fname):
    p = subprocess.Popen('tar -xvf ' + fname, shell=True, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, close_fds=True)
    out,err = p.communicate()
    p = subprocess.Popen('pwd', shell=True, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, close_fds=True)
    out2,err = p.communicate()
    print "[arr!] Unpacked package at: " + out2 + "with contents: \n" + out

def _unzip(fname):
    p = subprocess.Popen('gunzip ' + fname, shell=True, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, close_fds=True)
    out,err = p.communicate()
    p = subprocess.Popen('pwd', shell=True, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, close_fds=True)
    out2,err = p.communicate()
    print "[arr!] Unzipped zip file at: " + out2 + "with contents: \n" + out
