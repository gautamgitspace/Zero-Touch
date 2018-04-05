#!/usr/bin/python

import os

def _fetch_disk_space():
    df_output_lines = [s.split() for s in os.popen("df .").read().splitlines()]
    for items in df_output_lines[1:]:
        percent_used_with_percent_char = items[4]
        percent_used_figure = percent_used_with_percent_char.rstrip('%')
        percent_left_figure = 100 - int(percent_used_figure)
        print "[arr!] Looks good, disk space left: " + str(percent_left_figure) + "%"
    if int(percent_used_figure) > 90:
        return True, percent_used_figure
    percent_used = items[4]
