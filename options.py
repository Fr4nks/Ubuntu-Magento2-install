import subprocess
from pick import pick
from findreplaceadd import find_replace_add 

def viewer(title, options):
    """Creates a select list returns the selected option."""
    option, this = pick(options, title, indicator='=>', default_index=0)
    return option

D = {}

D['func'] = ['run_swap']
D['name'] = ['Swap memory']
D['word'] = ['How much swap/paging space do you need for your instance']
D['opti'] = [['512', '1024', '2048', '4096', 'Skip >>']]

D['func'] += ['run_php']
D['name'] += ['Install PHP']
D['word'] += ['Install PHP']
D['opti'] += [['Php 7', 'Php 5', 'Skip >>']]

D['func'] += ['replace_php']
D['name'] += ['Php.ini file']
D['word'] += ['Update the oho.ini file']
D['opti'] += [['yes', 'no']]

def run_swap(option):
    """Runs a shell command"""
    subprocess.call("echo 'test'" +option+ "'more test'", shell=True)

def run_php(option):
    if option == 'Php 7':
        subprocess.call("echo 'shell installs php 7'", shell=True)
    if option == 'Php 5': 
        subprocess.call("echo 'shell isntalls php 5'", shell=True)

def replace_php(option):
    if option == 'yes':
        find_this = "hello"
        replace_that = "Hope this still doesn't work test 2"
        find_replace_add('yourBigFile.txt', find_this, replace_that)

#title = ("Second the php.ini file")
#options = ['yes', 'no' ]
#secondupdate_php_ini, index = pick(options, title, indicator='=>', default_index=0)


#if secondupdate_php_ini == 'yes':
#  find_this = 'always_populate_raw_post_data'
#  replace_that = "always_populate_raw_post_data = -1"
#  find_replace_add('php.ini', find_this, replace_that)

#if 
#  find_this = 'memory_limit'
#  replace_that = 'memory_limit = '+ memory
#  find_replace_add(php.ini, find_this, replace_that)
