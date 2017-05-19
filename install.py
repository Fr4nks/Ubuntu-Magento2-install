#-*-coding:utf-8-*-
import sys
sys.path.insert(0, '/modules')
from __future__ import print_function #check, don't know might be part of pick.
from pick import pick #select lists
import subprocess #run the bash scripts in python
from findreplaceadd import find_replace_add #find and replaces or adds


title = ("How much swap/paging space do you need for your instance")
options = ['512', '1024', '2048', '4096', 'Skip >>']
option, index = pick(options, title, indicator='=>', default_index=1)
subprocess.call("echo 'test'" +option+ "'more test'", shell=True)

title = ("Install PHP")
options = ['Php 7', 'Php 5', 'Skip >>']
option, index = pick(options, title, indicator='=>', default_index=1) 
if option == 'Php 7':
  subprocess.call("echo 'shell installs php 7'", shell=True)
if option == 'Php 5': 
  subprocess.call("echo 'shell isntalls php 5'", shell=True)

title = ("Update the php.ini file")
options = ['yes', 'no' ]
options, index = pick(options, title, indicator='=>', default_index=1)
find = "hi"
replace = "Hope this doesn't work"
find_replace_add('yourBigFile.txt', find, replace)
