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
import ansible

def main(): 
    # Use cmd line arg flag to determine what type of lookup to perform
    if(sys.argv[1] == '-f'):
        inFile(sys.argv[2]) # call inFile method with 2nd cmd line arg
    elif(sys.argv[1] == '-s'):
        singleQuery(sys.argv[2]) # call singleQuery method with 2nd cmd line arg
    else:
        print('*' * 70 +"\nPlease use -f to indicate file or -s to indicate single query."
            "\nexample: -f test.txt or -s google.com") # display flag info if invalid input

# function that takes host domain name and prints IP addresses w/ ownership
# and registrar 
def getHostinfo(hostname):
    # create client object
    c = Client()
    
    # Lookup the record(s) host 
    resolver = dns.resolver.Resolver();
    myAnswers = resolver.query(hostname, 'A') 
 
    # loop output if multiple IP's
    print('\n' + hostname + '\n')
    for rdata in myAnswers:  # for each response
        print(c.lookup(rdata.address))  # print data
         
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

# Call main function
main()
