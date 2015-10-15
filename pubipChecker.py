__author__ = 'jonathan'

import IPCLib

ip = IPCLib.PublicIp()
log = IPCLib.FileWorks()

if log.readLastLine()[0] == ip.report()[0]:
    log.writeLine(', '.join(ip.report()))

    notifyme = IPCLib.emailer()
    with open("emailbody") as body:
        notifyme.compose(body.read() + ' ' + ip.report()[0])
        notifyme.send()