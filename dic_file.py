#!/usr/bin/python
# my solution
import sys


class ConfigDict(dict):
    def __init__(self, filename):
        self._filename = filename

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        fh = open(self._filename, 'a')
        fh.write('%s:%s\n' % (key, value))


# output
cd = ConfigDict('config_file.txt')

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('writing data: {0},{1}'.format(key, value))

    cd[key] = value

# teachers solution
import os


class ConfigDict(dict):
    def __init__(self, filename):
        self._filename = filename
        if os.path.isfile(self._filename):
            with open(self._filename) as fh:
                for line in fh:
                    line = line.rstrip()
                    key, value = line.split('=', 1)
                    dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as fh:
            for key, value in self.items():
                fh.write('{0}={1}\n'.format(key, value))
