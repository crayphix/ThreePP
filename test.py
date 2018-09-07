"""
Libraries needed to be installed: 
'pip install cymruwhois', 'pip install pythonwhois'
"""
import socket
from cymruwhois import Client
import dns.resolver
import json
import pythonwhois
from pprint import pprint

"""
Function findDNS
Program accepts file filled with hostnames then runs a dns lookup using
dns.resolver
Outputs table of hostnames with relevant ip addresses
"""
# create a new instance named 'myResolver'
myResolver = dns.resolver.Resolver()

# Lookup the record(s) for amazon.com
myAnswers = myResolver.query("npr.org")

for rdata in myAnswers:  # for each response
    print(rdata)  # print the data


# query IP for owner using cymruwhois
ip =('216.35.221.76')  # Assign IP
c = Client()  # Create Client object
r = c.lookup(ip)  # Assign lookup data to variable
print(r.owner)  #  print owner


# get information from Arin using hostname
domain = pythonwhois.get_whois('npr.org')
print(domain['registrar'])

