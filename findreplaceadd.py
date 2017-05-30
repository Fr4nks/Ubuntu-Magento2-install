import re
def find_replace_add(file_current, find_this, replace_that):
    """Finds text and replaces entire line, if no line is found appends the replaced line"""
    regex = re.compile(find_this) # Some benefits to leaving outside the loop??
    with open(file_current, 'rb') as file_old:
        with open(file_current + '.tmp', 'w') as file_new:
            found = 0
            for line in file_old:
                if regex.search(line) is not None:
                    line = replace_that
                    found += 1
                file_new.write(line) # print >>f1, 'string' OR print ('string' file=somefile)
            if found == 0:
                with open(file_current, 'a') as file_append:
                    file_new.write("\n" + replace_that) # ("\n" + replace_that) adds a line
