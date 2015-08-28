__author__ = 'jonathan'

import urllib2 as ulib
import datetime

class PublicIp:


    def __init__(self):
        self._publicIp = '0.0.0.0'
        self._timestamp = ''

        self.getPublicIp()
        self.getTimestamp()

    def getPublicIp(self):
        self._publicIp = ulib.urlopen('http://www.ipecho.net/plain').read()
    def getTimestamp(self):
        self._timestamp = datetime.datetime.now()

    def IP(self):
        return self._publicIp
    def TS(self):
        return self._timestamp
    def IP_TS(self):
        return self._publicIp + self._timestamp

class FileWorks:

    def __init__(self, name = 'PublicIpLog', path = './'):
        self._name = name
        self._path = path
        self.fileHandle = open(self._path+self._name, )


    def create(self):
        pass

    def checkExist(self):
        pass

    def writeLine(self, line):
        pass

    def readLastLine(self):
        pass

    def readAll(self):
        pass

    def diag(self):
        pass

