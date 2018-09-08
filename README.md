# ThreePP
Script to automate retrival and comparison of ip ownership under a hosts 
domain name and/or ip range. 

By Chris Thompson & Bryan Speelman

---Version 0.2---  9/8/18
Testing output when passing hostname and ip address
program currently runs under python 3.x and 2.7

Example:

    IN: 
    python ThreePP.py amazon.com

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

TODO:
-Encapsulate data
-Clean up output with printf formating
-Create function to handle file i/0
-Confirm desired output when given ip address 
-Confirm desired output when given ip range
-Obtain test data and validate output against original Bash script
-Compare results to find if ownership differs within each query.
-Color code output to show comparisons of ownership
-Convert to .pyc

