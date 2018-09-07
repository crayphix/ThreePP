import whois
import dns.resolver
import json
from pprint import pprint
from ipwhois import IPWhois

"""
Function findDNS
Program accepts file filled with hostnames then runs a dns lookup using
dns.resolver
Outputs table of hostnames with relevant ip addresses
"""
# create a new instance named 'myResolver'
myResolver = dns.resolver.Resolver()

# Lookup the record(s) for amazon.com
myAnswers = myResolver.query("amazon.com")

for rdata in myAnswers:  # for each response
    print rdata  # print the data

"""Class whoOwns
Program accepts hostname and relevant ip addresses
Outputs table with ownership for each

Option 1:
Must install librarys whois and ipwhois
github.com/secynic/ipwhois/
pip install ipwhois
pip install whois

Option 2:
pip install python rdap client
Ver 0.2 add color coding for diferant ownership.
If AWS ect red, if not then orange.
"""

# get information from Arin using hostname
domain = whois.whois('npr.org')
pprint(domain)

# query IP using ipwhois and rdap
obj = IPWhois('74.125.225.229')
result = obj.lookup_whois()
pprint(result)
