#-*-coding:utf-8-*-
from __future__ import print_function #check, don't know might be part of pick.
import sys
sys.path.insert(1, '/modules')
from pick import pick #select lists
import subprocess #run the bash scripts in python
from findreplaceadd import find_replace_add #find and replaces or adds


title = ("How much swap/paging space do you need for your instance")
options = ['512', '1024', '2048', '4096', 'Skip >>']
option, index = pick(options, title, indicator='=>', default_index=0)
subprocess.call("echo 'test'" +option+ "'more test'", shell=True)

title = ("Install PHP")
options = ['Php 7', 'Php 5', 'Skip >>']
install_php = pick(options, title, indicator='=>', default_index=0) 
if install_php == 'Php 7':
  subprocess.call("echo 'shell installs php 7'", shell=True)
if install_php == 'Php 5': 
  subprocess.call("echo 'shell isntalls php 5'", shell=True)

title = ("Update the php.ini file")
options = ['yes', 'no' ]
update_php_ini, index = pick(options, title, indicator='=>', default_index=0)
if update_php_ini == 'yes':
  find_this = "hello"
  replace_that = "Hope this still doesn't work test 2"
  find_replace_add('yourBigFile.txt', find_this, replace_that)

title = ("Second the  php.ini file")
options = ['yes', 'no' ]
secondupdate_php_ini, index = pick(options, title, indicator='=>', default_index=0)
if secondupdate_php_ini == 'yes':
  find_this = "hello"
  replace_that = "Append this text 2"
  find_replace_add('notFoundBigFile.txt', find_this, replace_that)
