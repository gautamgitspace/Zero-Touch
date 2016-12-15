#!/usr/bin/bash
import os

os.system("echo '$' > foo.txt")
for i in range (0,100):
    os.system("echo 'Hello World' >> foo.txt")
os.system("split -l 30 foo.txt f.txt")
