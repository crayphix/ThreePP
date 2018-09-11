"""
Script to automate retrieval and comparison of ip ownership under a hosts 
domain name and/or ip range. 

@BryanSpeelman & @ChrisThompson

---Version 0.3---  9/10/18

Testing input of files. 
***Bug getting DNS when reading from file***

Libraries needed to be installed:
'pip install cymruwhois', 'pip install pythonwhois'
"""

from cymruwhois import Client
import dns.resolver
import pythonwhois
import sys
import socket

<<<<<<< HEAD
def main(): 
    # Use cmd line arg flag to determine what type of lookup to perform
    if(sys.argv[1] == '-f'):
        inFile(sys.argv[2])
    elif(sys.argv[1] == '-s'):
        singleQuery(sys.argv[2])
    else:
        print('*' * 70 +"\nPlease use -f to indicate file or -s to indicate single query."
            "\nexample: -f test.txt or -s google.com")

# function that takes host domain name and prints IP addresses w/ ownership
# and registrar 
def getHostinfo(hostname):
    # create client object
    c = Client()

    # Lookup the record(s) host amazon.com
    myAnswers = dns.resolver.query(hostname) 
  
    # loop output if multiple IP's
    print('\n' + hostname + '\n')
    for rdata in myAnswers:  # for each response
        print(c.lookup(rdata))  # print data
    
    # get registrar from Arin using hostname
    print('\n' + hostname + ' Registrar')
    domain = pythonwhois.get_whois(hostname)
    print(domain['registrar'])
    print('\n'+ "*" * 70 +'\n')

# Function that prints ownership info for IP address
def getIPinfo(ip):
    # create client object
    c = Client()
    
    r = c.lookup(ip)  # Assign lookup data to variable
    print(ip+ '\n')
    print(r)
    print('*' * 70 + '\n')

def inFile(file):
    # Open file
    host_file = open(file)

    #Read file contents and filter actions
    for host in host_file:
        # if host name ex: amazon.com
        if('.com' in host):
            getHostinfo(host)
        
        #if IP address 
        else:
            getIPinfo(host)
    # close file
    host_file.close()

def singleQuery(host):
    # if host name ex: amazon.com
    if('.com' in host):
        getHostinfo(host)
    
    #if IP address 
    else:
        getIPinfo(host)
=======
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

>>>>>>> master

# Call main function
main()