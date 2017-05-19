def find_replace_add(file_current, find, replace):
  print (file_current)
  file_old = open(file_current, 'r')
  file_new = open(file_current + '.tmp', 'w') 
  lines = file_old.read()
  found = lines.find(find)
  if found is True:
    for line in file_old:
      file_new.write(line.replace( find, replace))
  else:
    file_new.write(replace)  

  file_old.close()
  file_new.close()  
