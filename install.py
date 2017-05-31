#-*-coding:utf-8--
import subprocess
import re
from pick import pick
import inspect

#dict.keys dict.values
# somekey: some_value
# somekey: other_value

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

def get_class_instance_values(class_vars):
    """inputs a list of class variables, outputs the variables attribute values
       could not get class_var.name as a variable???
    """
    instance_values = []
    for class_var in class_vars:
        instance_values.extend([class_var.name])
    return instance_values

manual_input_questions = [quest_B1, quest_B2]
got_B_questions = get_class_instance_values(manual_input_questions)


def run_B_questions(a_choice):
    """Asks the second layer of questions"""
    if a_choice == "Install all":
        ask_then_run(manual_input_questions)
    else:
        for manual_input_question, got_B_question in zip(manual_input_questions, got_B_questions):
            print (manual_input_question, got_B_question)
            if got_B_question == a_choice:
                ask_then_run(manual_input_question)

quest_A1 = question(
    run_B_questions,
    'no_value',
    'what do you want to do',
    ['Install all'] + got_B_questions + ['Exit']
)

print quest_A1.opti

def viewer(title, options):
    """Creates a select list returns the selected option."""
    option, not_used = pick(options, title, indicator='=>', default_index=0)
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
#    if isinstance(asks, list):
    got_options = []
    for ask in asks:
        option_out = viewer(ask.word, ask.opti)
        got_options.extend([[ask.func, option_out]]) #stores the values
    for got_option in got_options:
        got_option[0](got_option[1])
    return option_out
 #   else:
 #       option_out = viewer()

option = ask_then_run([quest_A1]) #runs the first questions
