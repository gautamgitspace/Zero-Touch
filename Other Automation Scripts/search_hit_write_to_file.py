def _search_for_string_and_write_to_file(relative_path, file_to_scan, search_string):
    search_hit = 0
    #clear existing file if user searches for the same search string
    fname_here = relative_path + "/" + search_string
    if os.path.isfile(fname_here):
        f = open (fname_here, 'w')
        f.truncate()
        
    with open(file_to_scan) as f:
        for count, line in enumerate (f):
        if re.search(search_string, line):
            search_hit += 1
            #write to file irrespective of search_hit count
            rc = _write_to_file_mode_a(search_string, line)
            if search_hit > 75:
                print "[arr!] Output too large, written " + str(search_hit) + " lines to " + rc + " Successfuly!"
            elif 0 < search_hit < 75:
                print "\n[arr!] Found " + str(search_hit) + " Matching line(s)"
                #print the lesser 75 lines here after reading from file
                f = open(search_string, 'r')
                print f.read()
                f.close()
            else:
                print "[arr!] Search yielded 0 results"

def _write_to_file_mode_a(file_name, content):
    with open(file_name, 'a') as file_obj:
        file_obj.write(content)
        return file_name
