#!/usr/bin/python

import webbrowser

def input_rfc_number():
    rfc_number = raw_input('Enter RFC NUMBER: ')
    urlify = 'https://tools.ietf.org/html/' + rfc_number
    webbrowser.open(urlify)

if __name__ == '__main__':
    input_rfc_number()
