#!/user/bin/python
"""Object Serialization:
Serialization means persistent storage, i.e., to disk
Relational storage writes data to tables (e.g., relational
database text files)
Object-based storage stores objects as they are used in
code object databases
Object-relational mappings can mediate between the two """


"""lesson 1: pickle """
import pickle
#
# mylist = ['a','b','c','d']
#
# with open('datafile.txt','w') as fh:
#     pickle.dump(mylist,fh)
#
#
# with open('datafile.txt') as fh:
#     unpickledlist = pickle.load(fh)
#
# print unpickledlist

# x = pickle.dumps(['a','b,1,2.3])
# var = pickle.loads(x)
# print var
# type(x) <type 'str'>

"""multiple objects"""

this_int = 555
this_string = "oh my goodness"
mydict_of_lists = {'a': [1,2,3],'b': [4,5,6]}
query_results = [('joe',22,'clear'),('pete', 34, 'salesman')]

with open('datafile.txt', 'w') as fh:
    pickle.dump((this_int, this_string, mydict_of_lists, query_results), fh)

with open('datafile.txt') as fh:
    tup = pickle.load(fh)

for i in range(0,len(tup)):
    print tup[i]

"""storing instances"""

class Myclass(object):

    def __init__(self, init_val):
        self.val = init_val

    def increment(self):
        self.val += 1

cc = Myclass(5)
cc.increment()
cc.increment()

with open('datafile.txt', 'w') as fh:
    pickle.dump(cc, fh)

with open('datafile.txt') as fh:
    unpickled_cc = pickle.load(fh)

print unpickled_cc
print unpickled_cc.val

"""lesson 2: JSON DATA STRUCTURE"""

import json

# with open('back_config.json') as fh:
#     conf = json.load(fh)  # loads a JSON of type 'dict'
#
# conf['newkey'] = 5.00005
#
# with open('back_config.json', 'w') as fh:
#     json.dump(conf, fh)  # writes to JSON

"""lesson 3: YAML"""

import yaml

mydict = {'a': 1, 'b': 2, 'c': 3}
mylist = [1,2,3,4,5]
mytuple = ('x','y','z')

loaded_yaml = yaml.dump(mydict, default_flow_style = False)
print loaded_yaml

print yaml.dump((mylist,mytuple, mydict), default_flow_style = False)
"""with open('app.yaml') as fh:
    struct = yaml.load(fh)

print jsdon.dumps(struct, indent=4, separators=(',', ':') """

class MyClass(object):

    classvar = 10

    def __init__(self, val):
        self.val = val

    def increment(self):
        self.val +=1

x = Myclass(5)
x.increment()
x.increment()

with open('obj.yaml', 'w') as fh:
    yaml.dump(x,fh)

with open('obj.yaml') as fh:
    inst = yaml.safe_load(fh)

print inst.val