#-*-coding:utf-8-*-
from __future__ import print_function #check, don't know might be part of pick.
from pick import pick #select lists
import subprocess #run the bash scripts in python
from yesorno import query_yes_no #runs the yes on no question
from findreplaceadd import find_replace_add

swappage = query_yes_no("Do you even want this fucking swap memory?", None)
if swappage is True:
  title = ("How much swap/paging space do you need for your instance")
  options = ['512', '1024', '2048', '4096', 'Exit']
  option, index = pick(options, title, indicator='=>', default_index=2)
  subprocess.call("echo 'test'" +option+ "'more test'", shell=True)

php_install = query_yes_no("Install Php?", None)
if php_install is True:
  title = ("Install Php 7 or Php 5")
  options = ['Php 7', 'Php 5', 'Exit']
  option, index = pick(options, title, indicator='=>', default_index=1) 
  if option == 'Php 7':
    subprocess.call("echo 'shell installs php 7'", shell=True)
  if option == 'Php 5': 
    subprocess.call("echo 'shell isntalls php 5'", shell=True)

php_ini = query_yes_no("set php.ini file", None)
if php_install is True:
  find = "hi"
  replace = "Fucking hope this doesn't work"
  find_replace_add('yourBigFile.txt', find, replace)
