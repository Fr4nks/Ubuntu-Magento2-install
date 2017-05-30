#-*-coding:utf-8--
import subprocess
import re
from pick import pick
import inspect

#dict.keys dict.values
# somekey: some_value
# somekey: other_value

def run_B_questions(a_choice):
    """Asks the second layer of questions"""
    if a_choice == "Install all":
        ask_then_run([quest_B1, quest_B2])
    if a_choice == "Exit":
        return "Exit"
    else:
        ask_then_run([quest_B2])

def replace_php(option):
    """Fi"""
    if option == 'yes':
        find_this = "hello"
        replace_that = "Hope this still doesn't work test 2"
        find_replace_add('yourBigFile.txt', find_this, replace_that)

def something():
    find_this = 'always_populate_raw_post_data'
    replace_that = "always_populate_raw_post_data = -1"
    find_replace_add('php.ini', find_this, replace_that)

def something_else(option):
    find_this = 'memory_limit'
    replace_that = 'memory_limit = '+ option
    find_replace_add('php.ini', find_this, replace_that)

def run_swap(option):
    """Fixes problem with memory"""
    subprocess.call("echo 'test'" +option+ "'more test'", shell=True)

def run_php(option):
    """Install php"""
    if option == 'Php 7':
        subprocess.call("echo 'shell installs php 7'", shell=True)
    if option == 'Php 5':
        subprocess.call("echo 'shell isntalls php 5'", shell=True)

class question(object):

#object.attribute >> field, method
    def __init__(self, func, name, word, opti):
#instances
        self.func = func
        self.name = name
        self.word = word
        self.opti = opti


        # self.data = data
        # self.index = len(data)


    # def __iter__(self):
    #     return self

    # def next(self):
    #     if self.index == 0:
    #         raise StopIteration
    #     self.index = self.index -1
    #     return self.data[self.index]

    # def __str__(self):
    #     return ( str(self.func) , str(self.name) )

    # def get_question_func(self):
    #     return self.name

    #method, function that is assosiated with a class.

quest_A1 = question(
    run_B_questions,
    'no_value',
    'what do you want to do',
    ['Install all', 'Exit']
)

quest_B1 = question(
    run_swap,
    'Swap Memory',
    'How much swap/paging space do you need for your instance',
    ['512', '1024', '2048', '4096', 'Skip >>']
)

quest_B2 = question(
    run_php,
    'Install PHP',
    'Install PHP',
    ['Php 7', 'Php 5', 'Skip >>']
)

def viewer(title, options):
    """Creates a select list returns the selected option."""
    option, something = pick(options, title, indicator='=>', default_index=0)
    return option

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

def ask_then_run(asks):
    """Inputs questions list, asks all then runs """
    got_options = []
    for ask in asks:
        option_out = viewer(ask.word, ask.opti)
        got_options.extend([[ask.func, option_out]]) #stores the values
    for got_option in got_options:
        got_option[0](got_option[1])
    return option_out

option = ask_then_run([quest_A1]) #runs the first questions



# D = {}

# D['func'] = ['run_swap']
# D['name'] = ['Swap memory']
# D['word'] = ['How much swap/paging space do you need for your instance']
# D['opti'] = [['512', '1024', '2048', '4096', 'Skip >>']]

# D['func'] += ['run_php']
# D['name'] += ['Install PHP']
# D['word'] += ['Install PHP']
# D['opti'] += [['Php 7', 'Php 5', 'Skip >>']]

# D['func'] += ['replace_php']
# D['name'] += ['Php.ini file']
# D['word'] += ['Update the oho.ini file']
# D['opti'] += [['yes', 'no']]

# D['func'] += ['replace_php']
# D['name'] += ['Php.ini file']
# D['word'] += ['Update the oho.ini file']
# D['opti'] += [['yes', 'no']]


# general notes:
# ==============
# 1861008840     ID
# <class'int'>   TYPE(float class, Integer class, String class) Class is like a blueprint
# 1              VALUE

#Type: float = 9.435 >>This is an object
#Type: Integer = 5 >>This is an object
#Type: String = >>"hello world" >>This is also an object




# def run_program():
#     """Stuff"""
#     screen_options = ['Install all'] + D['name'] + ['Exit']
#     screen_option_returned = viewer ("What do you want to do", screen_options)

#     if screen_option_returned == 'Install all':
#         got_options = []
#         for name, options_in in zip(D['word'], D['opti']):
#             option_out = viewer(name, options_in)
#             got_options.extend([option_out]) #stores the values
#         for func, got_option in zip(D['func'], got_options):
#             globals()[func.__name__](got_option) #executes the functions with selected options
#     else:
#         ziped_D = zip(D['
#         ['func'], D['name'], D['word'], D['opti'])
#         indexed = D['name'].index(screen_option_returned)
#        def run_B_questions(got_option):


#runs the functions option_out = viewer(ziped_D[indexed][2], ziped_D[indexed][3])
#         func = ziped_D[indexed][0] #gets the function name.
#         globals()[func](option_out) #turns string - variable.


#     screen_options = ['Install all'] + D['name'] + ['Exit']
#     screen_option_returned = viewer("What do you want to do", screen_options)
#     if screen_option_returned == 'Install all':
#         run_all()
#     else:
#         run_this()





 