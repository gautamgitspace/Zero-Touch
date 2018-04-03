#!/usr/bin/env python
def decimal_to_hex():
    value = raw_input('Enter decimal data ')
    print hex(int(value)).split('x')[-1]
decimal_to_hex()
