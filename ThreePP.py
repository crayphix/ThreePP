"""
Libraries needed to be installed:
'pip install cymruwhois', 'pip install pythonwhois'
"""
from cymruwhois import Client
import dns.resolver
import pythonwhois

foo = 0

# create a new instance named 'myResolver'
myResolver = dns.resolver.Resolver()

# create client object
c = Client()

#initialize domanin variable
host = 'spotify.com'

# Lookup the record(s) for amazon.com
myAnswers = myResolver.query(host)

print('\n' + host + '\n')
for rdata in myAnswers:  # for each response
    print(rdata)  # print the data
    print('Owner ---->')
    foo = rdata
    r = c.lookup(foo)  # Assign lookup data to variable
    print(r.owner)  # print owner
    print('-' * 70 + '\n')

# get information from Arin using hostname
print(host + ' Registrar ------>')
domain = pythonwhois.get_whois(host)
print(domain['registrar'])
print
