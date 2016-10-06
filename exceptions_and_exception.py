#!python/usr/bin

"""Exceptions and Exception:
Identifying exceptions (errors)
Trapping exceptions with try/except
Raising exceptions with raise
Defining custom exception classes"""

"""lesson 1: Trapping and raising exceptions"""

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# key = raw_input('please input a key: ')

try:
    print('testing for error')
    print("the value for {0} is {1}".format(key, my_dict[key]))
    print('everything is ok')

except KeyError:
    print('trapped error')
    print("the key " + key + " does not exist")

print('program continues ...')

another way

import sys

try:
    arg = sys.argv[1]
    num = int(arg)

except(IndexError, ValueError):
    exit('please enter an integer on the command line')

print "thanks for the int"


"""lesson 2: custom exceptions"""

import re

def process_date(this_date):
    # this regex makes sure that this_date is YYYY-MM-DD
    if not re.search(r'^\d\d\d\d\-\d\d\-\d\d$', this_date):
        raise ValueError('please submit date in YYYY-MM-DD format')

    print "the submitted dates is {0}".format(this_date)

process_date('1980-01-03')
print

class MyError(Exception):
    def __init__(self, *args):
        print 'calling init'
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print "calling str"
        if self.message:
            return "here's a MyError exception with a message: {0}".format(self.message)
        else:
            return "here's a MyError exception!"
#raise MyError
raise MyError('Houston, we have a problem')

