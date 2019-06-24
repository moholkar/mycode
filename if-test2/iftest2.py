#!/usr/bin/python3

import ipaddress 
#ipchk='192.168.0.1'
ipchk= input('Apply an IP address: ')


try:
    ipaddress.ip_address(ipchk)
    if ipchk== '192.168.70.1':
        print('Looks like the gateway IP was set :' + ipchk +  'This is not recommended') 


    else: 
        print('Looks like the IP was set : ' +ipchk)


#    else: 
#       print('You did not provide input, dummy' )

except:
    print('Enter a valid input')



