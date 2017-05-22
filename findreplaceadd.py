def find_replace_add(file_current, find_this, replace_that):
  with open(file_current, 'rb') as file_old:
    with open(file_current + '.tmp', 'r+') as file_new:
      found = 0  
      for line in file_old:
        file_new.write(line.replace(find_this, replace_that))
        if find_this in line:
          found += 1
      if found == 0:
          with open(file_current, 'a') as file_append:
            file_append.write("\n" + replace_that)
