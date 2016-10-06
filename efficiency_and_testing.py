"""Efficiency and testing
"python debugger"
built-in to python
Allows step-by-step execution of the script
Allows flow contorl (can execute at any line or function)
Allows inspection of variables
one of many debuggers; some IDEs show visual execution
"""

"""lesson 1; pdb debugging """
import pdb

# pdb.set_trace() type h to see commands

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mysum = 0
# for val in values:
#     mysum = 0   # inside the loop error
#     mysum += val
# print mysum

# pdb.set_trace() you can see the values in the loop. Neat!

def doubleval(argsum, val):
    argsum = 0
    newval = argsum + val
    return newval


for val in values:
    mysum = doubleval(mysum,val)

print mysum

"""lesson 2: logging """

import logging

logging.basicConfig(level=logging.INFO)

logging.debug('this message will be ignored') # will not print this
logging.info('this should be logged') # will print this
logging.warning('And this, too') # will not print this

"""lesson 3: Benchmarking: the Timeit Module"""

import timeit

print 'by index:  ', timeit.timeit(stmt="mydict['c']", setup="mydict = {'a': 5, 'b': 6, 'c': 7}", number=1000000)
print 'by get:    ', timeit.timeit(stmt="mydict.get('c')", setup="mydict ={'a': 5, 'b': 6, 'c': 7} ", number=1000000)


def testme(this_dict,key):
    return this_dict[key]

print timeit.timeit("testme(mydict,key)", setup= "from __main__ import testme; mydict ={'a':1,'b':2,'c':3}; key='c'", number=1000000)



"""lesson 4: unittesting pytest module """


##################################
#  in a file called myprogram.py #
##################################
import sys
def doubleit(x):
    if not isinstance(x, (int,float))
    var = x*2
    return var

if __name__ == '__main__':
    input_val = sys.argv[1]
    double_val = doubleit(input_val)

    print 'the value of {0} is {1}'.format(input_val, double_val)


######################################
# in a file called test_myprogram.py #
######################################
import myprogram
import pytest

def test_doubleit():
    assert myprogram.doubleit(10) == 20


def test_doubleit_tyoe()
    with pytest.raises(TypeError):
        myprogram.doubleit('hello')




