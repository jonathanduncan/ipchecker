__author__ = 'jonathan'

import smtplib as email
import urllib2 as ulib
import datetime
import os


class PublicIp:
    """
    Provide quick access to the public IP address with a timestamp.2

    """
    def __init__(self):
        self.__publicIp = ulib.urlopen('http://www.ipecho.net/plain').read()
        self.__timestamp = str(datetime.datetime.now())

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
        self._filehandle = ''

        self.create()

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
            handle.write(line + '\n')

    def readLastLine(self):
        '''Return only the most receant entry in the IPLog.'''
        with open(self._completePath, 'r') as handle:
            for line in handle:
                pass
            return str(line).strip('\n').split(',')

class emailer:
    def __init__(self):
        self._toAddress = ""
        self._fromAddress = ""
        self._message = ""

        self.server = email.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        if not os.path.isfile("creds"):
            print "No creds file, can't login to gmail."
        else:
            with open("creds") as creds:
                lines = creds.readlines()
            self.server.login(lines[0].rstrip(), lines[1].rstrip())

    def compose(self, message, to_address="<jonathanjosephduncan@gmail.com>", from_address="<jonathanjosephduncan@gmail.com>"):
        self._toAddress = to_address
        self._fromAddress = from_address
        self._message = message

    def send(self):
        self.server.sendmail(self._fromAddress, self._toAddress, self._message)