#!/usr/bin/python3 

def main():
    switch= {'hostname': 'sw1', 'ip': '10.0.1.1' , 'versio': '1.2' , 'vendor': 'cisco'} 

    print( switch['hostname'] )
    print( switch['ip'] )
    switch["lynx"]= "1.1.1.1" 
    print( switch['lynx'] ) 
    print( switch.get("hughes"))

main() 


