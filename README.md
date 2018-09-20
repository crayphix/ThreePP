# ThreePP
Script to automate retrival and comparison of ip ownership under a hosts 
domain name and/or ip range. 

By Chris Thompson & Bryan Speelman

---Version 0.4---  9/19/18

[] Program retrieves ip ownership from single line and file.

[] program currently runs under python 3.x and 2.7

[] Dependencies: cymruswhois, pythonwhois



Example (Single input:

    IN: 
    python ThreePP.py -s amazon.com

    OUT:
    amazon.com

    176.32.98.166
    Owner ---->
    AMAZON-02 - Amazon.com, Inc., US
    ----------------------------------------------------------------------

    176.32.103.205
    Owner ---->
    AMAZON-02 - Amazon.com, Inc., US
    ----------------------------------------------------------------------

    205.251.242.103
    Owner ---->
    AMAZON-02 - Amazon.com, Inc., US
    ----------------------------------------------------------------------

    amazon.com Registrar ------>
    ['MarkMonitor Inc.']

Example (file):
    
    IN:
    python ThreePP.py -f test.txt
    
    OUT:
    spotify.com

    15169      104.154.127.47   104.154.96.0/19  US 'GOOGLE - Google LLC, US'
    15169      104.199.64.136   104.199.64.0/19  US 'GOOGLE - Google LLC, US'
    15169      104.199.240.211  104.199.224.0/19 US 'GOOGLE - Google LLC, US'

    spotify.com Registrar
    ['Ports Group AB']

    **********************************************************************

    104.199.240.211

    15169      104.199.240.211  104.199.224.0/19 US 'GOOGLE - Google LLC, US'
    **********************************************************************


    google.com

    15169      172.217.12.142   172.217.12.0/24  US 'GOOGLE - Google LLC, US'

    google.com Registrar
    ['MarkMonitor Inc.']

    **********************************************************************


    reddit.com

    54113      151.101.1.140    151.101.0.0/22   US 'FASTLY - Fastly, US'
    54113      151.101.65.140   151.101.64.0/22  US 'FASTLY - Fastly, US'
    54113      151.101.193.140  151.101.192.0/22 US 'FASTLY - Fastly, US'
    54113      151.101.129.140  151.101.128.0/22 US 'FASTLY - Fastly, US'

    reddit.com Registrar
    ['MarkMonitor Inc.']

    **********************************************************************


    amazon.com

    16509      176.32.103.205   176.32.96.0/21   IE 'AMAZON-02 - Amazon.com, Inc., US'
    16509      205.251.242.103  205.251.240.0/22 US 'AMAZON-02 - Amazon.com, Inc., US'
    16509      176.32.98.166    176.32.98.0/24   IE 'AMAZON-02 - Amazon.com, Inc., US'

    amazon.com Registrar
    ['MarkMonitor Inc.']

    **********************************************************************
                
TODO:

-Obtain test data and validate output against original Bash script

-Compare results to find if ownership differs within each query.

-Color code output to show comparisons of ownership

-Convert to .pyc

