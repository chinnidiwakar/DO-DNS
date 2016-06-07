#!/usr/bin/python

import socket
import dns.resolver
import dns.exception

print "\n\033[1;32mWelcome To The DO DNS V1.0  by Chinni Diwakar\033[1;m\n\n"

a = dns.resolver.Resolver()

userinput = raw_input("Give a domain Name: ")

A = a.query(userinput, 'A' )
print "\n\nIp For The Host"
print '_______________________________\n'
for AA in A:
	print userinput
	print AA

NS = a.query(userinput, 'NS')
print "\n\nName Servers Of The Host"
print '_______________________________\n'
for N in NS:
	print N
	print socket.gethostbyname(str(N))

MX = a.query(userinput, 'MX')
print "\n\nMail Exchange Servers Of the Host"
print '_______________________________\n'
for M in MX:
	sam = str(M)
	sam = sam.replace(sam[:3], '')
	print sam
	mx = socket.gethostbyname(sam)
	print mx
