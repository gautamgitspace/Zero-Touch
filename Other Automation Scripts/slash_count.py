#!/usr/bin/python

content = "ws/abhigaut/abc/def/ghi/jkl/folder"
slash_count = 0
first_slash = False
segments = content.split("/")
print segments
if segments[0] == '':
    first_slash = True
for alphabets in content:
    if "/" == alphabets:
        slash_count += 1
if first_slash:
    print "decrementing slash_count " + str(slash_count -1)
else:
    print slash_count
