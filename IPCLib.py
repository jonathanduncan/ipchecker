__author__ = 'jonathan'

import urllib2 as ulib
import datetime
import os


class PublicIp:
    """
    Provide quick access to the public IP address with a timestamp.2

    """
    def __init__(self):
        self.__publicIp = '0.0.0.0'
        self.__timestamp = ''

        self.__getpublicip()
        self.__gettimestamp()

    def __getpublicip(self):
        self._publicIp = str(ulib.urlopen('http://www.ipecho.net/plain').read())

    def __gettimestamp(self):
        self._timestamp = str(datetime.datetime.now())

    def report(self):
        '''Return the IP address and timestamp.

        :rtype list
        '''
        return [self.__publicIp, self.__timestamp]


class FileWorks:
    def __init__(self, name='PublicIpLog', path='./'):
        self._path = path
        self._name = name
        self._completePath = self._path + self._name

    def openFileR(self):
        '''Return the handle of the file in READONLY mode.'''
        self.create()  # checks if it exists before it creates
        with open(self._completePath, 'r') as self.handle:
            return self.handle

    def create(self):
        '''if the file doesn't exist, create it.'''
        if not self.checkExist():
            open(self._completePath, 'w').close()

    def checkExist(self):
        '''Check to see if the file exists.'''
        return os.path.isfile(self._completePath)

    def writeLine(self, line):
        '''Inser line into the file.'''
        with open(self._completePath, 'a') as handle:
            handle.write(line)

    def readLastLine(self):
        '''Return only the most receant entry in the IPLog.'''
        for line in self.openFileR(self):
            pass
        return str(line).strip('\n')

    def readAll(self):
        '''Return everything in the IPLog.'''
        return self.openFileR()
