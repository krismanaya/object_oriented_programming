!/usr/bin/python
python2

class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = self.filter_int(val)
        InstanceCounter.count +=1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def filter_int(value):
        if not isinstance(value,int):
            return 0
        else:
            return value

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)


print a.val
print b.val
print c.val

import abc

class GetterSetter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self,input):
        """Set a value in the instance"""
        return

    @abc.abstractmethod
    def get_val(self):
        """Get and return a value from teh instance . . """
        return

class MyClass(GetterSetter):

    def set_val(self,input):
        self.val = input


    def get_val(self):
        return self.val

x = MyClass()
print x


import abc

class GetSetParent(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self,value):
        self.val = 0

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def show_doc(self):
        return

class GetSetInt(GetSetParent):
    def set_val(self, value):
        if not isinstance(value,int):
            value = 0
        super(GetSetInt, self).set_val(value)

    def show_doc(self):
        print('GetSetInt object ({0}), only accepts'
              'integer values'.format((id(self))))

class GetSetList(GetSetParent):
    def __init__(self,value=0):
        self.vallist = [value]

    def get_val(self):
        return self.vallist[-1]

    def get_vals(self):
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)

    def show_doc(self):
        print('GetSetList object, len {0}, stores'
              'history of values set'.format(len(self.vallist)))


x = GetSetInt(3)
x.set_val(5)
print(x.get_val())
x.show_doc()

gsl = GetSetList(5)
gsl.set_val(10)
gsl.set_val(20)
print gsl.get_val()
print gsl.get_vals()
gsl.show_doc()


import StringIO

class WriteMyStuff(object):

    def __init__(self, writer):
        self.writer = writer

    def write(self):

        write_text = "this is a silly message"
        self.writer.write(write_text)

fh = open('text.txt', 'w')
w1 = WriteMyStuff(fh)
w1.write()
fh.close()

sioh = StringIO.StringIO()
w2 = WriteMyStuff(sioh)
w2.write()

print 'file object:      ', open('text.txt', 'r').read()
print 'StringIO object:  ', sioh.getvalue()



