def find_replace_add(file_current, find, replace):
  print (file_current)
  file_old = open(file_current, 'r')
  file_new = open(file_current + '.tmp', 'w')
  for line in file_old:
      if file_new.write(line.replace( find, replace)) is False:
        file_new.write(replace)
  file_old.close()
  file_new.close()  
