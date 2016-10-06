#!/usr/bin/python
#python2

import datetime
import abc

class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self,write_text):
        return


class LogFile(WriteFile):

    def __init__(self,file_name):
        self.file_name = open(file_name,'a')

    def write(self, write_text):
        date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.file_name.write(date_time + ' ' + write_text)
        self.file_name.close() #this is bad

class DelimFile(WriteFile):

    def __init__(self,file_name,delimeter):
        self.file_name = open(file_name,'a')
        self.delimeter = delimeter

    def write(self, write_text):
        self.file_name.write(self.delimeter.join(list(write_text)))
        self.file_name.close() #this is bad


#teacher's solution

class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return

    def __init__(self, filename):
        self.filename = filename

    def write_line(self, text):
        fh = open(self.filename, 'a')
        fh.write(text + '\n')
        fh.close()

class DelimFile(WriteFile):

    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim

    def write(self, this_list):
        line = self.delim.join(this_list)
        self.write_line(line)

class Logfile(WriteFile):

    def write(self, this_line):
        dt = datetime.datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M')
        self.write_line('{0}     {1}'.format(date_str, this_line))




log = LogFile('log.txt')
c = DelimFile('text.csv',',')
log.write('this is a log message')
c.write(['a','b','c','d'])

