"""
Libraries needed to be installed:
'pip install cymruwhois', 'pip install pythonwhois'
"""
from cymruwhois import Client
import dns.resolver
import pythonwhois
import sys

foo = 0

# create client object
c = Client()

#initialize domanin variable with arg from cmd line  
host = sys.argv[1]

if('.com' in host):
    # create a new instance named 'myResolver'
    myResolver = dns.resolver.Resolver()

    # Lookup the record(s) for amazon.com
    myAnswers = myResolver.query(host)

    # loop output if multiple IP's
    print('\n' + host + '\n')
    for rdata in myAnswers:  # for each response
        print(rdata)  # print the data
        print('Owner ---->')
        foo = rdata
        r = c.lookup(foo)  # Assign lookup data to variable
        print(r.owner)  # print owner
        print('-' * 70 + '\n')

    # get registrar from Arin using hostname
    print(host + ' Registrar ------>')
    domain = pythonwhois.get_whois(host)
    print(domain['registrar'])
    print


else:
    print('\n' + host)
    print('Owner ---->')
    r = c.lookup(host)  # Assign lookup data to variable
    print(r.owner)  # print owner
    print('-' * 70 + '\n')


