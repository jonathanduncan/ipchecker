import urllib2 as ulib
import smtplib as email
import os
import datetime

server = email.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('jonathanjosephduncan@gmail.com', 'spiritindomitable')

ipLog_path = '.ipLog'

Cip = ulib.urlopen('http://www.ipecho.net/plain').read()

header = 'Subject:Valencia DR IP Address Change'
msg = '\n\nThe IP address has changed on ' + str(datetime.datetime.now()) + ' to '
if not os.path.isfile(ipLog_path):
    open(ipLog_path, 'w').close() # touch file

if os.stat(ipLog_path).st_size > 0:
    with open(ipLog_path, 'a+') as hfile:
        for i in hfile: # most receant entry
            pass #   ^^^^^^^^^^^^^^^^^^^^^^
        print str(i).strip('\n') + ' - entry in log'
        print Cip + ' - Cip'
        if i == Cip:
            print 'No Change'
        else:
            print 'IP changed'
            hfile.write(Cip)
            server.sendmail('jonathanjosephduncan@gmail.com',
                            'jonathanjosephduncan@gmail.com',
                            header + msg + str(Cip).strip('\n'))
else:
    with open(ipLog_path, 'w') as f:
        f.write(Cip)
        print 'log initialized'
