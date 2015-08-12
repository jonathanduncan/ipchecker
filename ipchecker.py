import urllib2 as ulib
import smtplib as email
import os
import datetime

emailAddress = str()
PW = str()

with open('./creds', 'r') as creds:
    lines = creds.readlines()
    emailAddress = lines[0].strip('\n')
    PW = lines[1].strip('\n')

server = email.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(emailAddress, PW)

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
            server.sendmail(emailAddress,
                            emailAddress,
                            header + msg + str(Cip).strip('\n'))
else:
    with open(ipLog_path, 'w') as f:
        f.write(Cip)
        print 'log initialized'
