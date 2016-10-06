"""Implementing core syntax(operators,looping,etc.)
in our class design
Inheriting from build-ints(like lists, dictionaries,etc.)
@property: control attributes access
Attribute / variable naming conventions
With context. New-Style classes overview."""

"""lesson 1: core syntax"""


# var = 1
# var2 = 2
# print(var.__add__(var2))  # magic attribute


class SumList(object):
    def __init__(self, this_list):
        self.my_list = this_list

    def __add__(self, other):
        new_list = [x + y for x, y in zip(self.my_list, other.my_list)]

        # following 4 lines same as line above
        # new_list = []
        # zipped_list = zip(self.mylist,other.mylist)
        # for tup in zipped_list:
        #   new_list.append(tup[0] + tup[1])

        return SumList(new_list)

    def __repr__(self):
        return str(self.my_list)


cc = SumList([1, 2, 3, 4, 5])
dd = SumList([100, 200, 300, 400, 500])

ee = cc + dd  # cc.__add__(dd)
print ee  # [101, 202, 303, 404, 505]

"""lesson 2: subclassing Built ins"""


class MyDict(dict):
    def __setitem__(self, key, value):
        print "setting a key and value!"
        dict.__setitem__(self, key, value)


dd = MyDict()
dd['a'] = 5
dd['b'] = 6

for key in dd.keys():
    print('{0}={1}'.format(key, dd[key]))


# MyList inherits from 'list' object but indexes from 1 instead of 0!

class MyList(list):  # inherit from list

    def __getitem__(self, index):
        if index == 0: raise IndexError
        if index > 0: index -= 1
        return list.__getitem__(self, index)  # this method is called when we access
        # a value with subscript (x[1],etc.)

    def __setitem__(self, key, value):
        if index == 0: raise IndexError
        if index > 0: index -= 1
        list.__setitem__(self, index, value)


x = MyList(['a', 'b', 'c'])  # __init__() inherited from builtin list

print x  # __repr__() inherited from builtin list
x.append('spam')  # append() inherited ''  ...   ''
print x[1]  # 'a' (MyList.__get__item__
#      customizes list superclass method)
print x[4]  # index is 1, buf reflects 0!
# 'spam' (index is 4 bu reflects 3!)


"""lesson 3: Attribute Encapsulation"""


class GetSet(object):
    def __init__(self, value):
        self.attrval = value

    @property
    def var(self):
        print "getting the 'var' attribute"
        return self.attrval

    @var.setter
    def var(self, value):
        print "setting the 'var' attribute"
        self.attrval = value

    @var.deleter
    def var(self):
        print "deleting the 'var' attribute"
        self.attrval = None


me = GetSet(5)

me.var = 1000
print me.var
del me.var
print me.var

"""lesson 4: private variables"""


class GetSet(object):
    instance_count = 0

    __mangled_name = 'no privacy!'

    def __init__(self, value):
        self._attrval = value
        GetSet.instance_count +=1

    @property
    def var(self):
        print "getting the 'var' attribute"
        return self._attrval

    @var.setter
    def var(self, value):
        print "setting the 'var' attribute"
        self._attrval = value

    @var.deleter
    def var(self):
        print "deleting the 'var' attribute"
        self._attrval = None

cc = GetSet(5)
cc.var = 10
print cc._attrval
print cc._GetSet__mangled_name


"""lesson 5: __with__ context """

# with open('filename.txt') as fh:
#     for line in fh:
#         line = line.rstrip()
#         print(line)
#
# print 'done!'
#
# fh = open('filename.txt')
# for line in fh:
#     print(line)
# fh.close()

class MyClass(object):

    def __enter__(self):
        print('we have entered "with"')
        return self

    def __exit__(self, type, value, traceback):
        print('we a leaving "with"')

    def say_hi(self):
        print('hi, instance %s' % (id(self)))

with MyClass() as cc:
    cc.say_hi()

print('after the "with" block')


class MyClass2(object):

    def __enter__(self):
        print('we have entered "with"')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('error type: {0}'.format(exc_type))
        print('error type: {0}'.format(exc_val))
        print('error type: {0}'.format(exc_tb))

    def say_hi(self):
        print('hi, instance %s' % (id(self)))

with MyClass2() as cc:
    cc.say_hi()

print('after the "with" block')


"""lesson 6: New Style Classes"""

# old style "classic" class
class OldClass:
    pass

# new style class
class NewClass(object):
    pass

oc = OldClass()
nc = NewClass()

print(type(oc))
print(type(nc))

print oc.__class__