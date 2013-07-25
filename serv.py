#!/usr/bin/python
# udp connection

import socket

print "Creating socket"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "done"

print "looking up port number"
port = socket.getservbyname('http','tcp')
print "done"

s.connect(("www.freeniu.com",port))
print "done"

print "connect from",s.getsockname()
print "connect to",s.getpeername()
