#!/usr/bin/python3 

import urllib.request
import json

majortom = 'http://api.open-notify.org/astros.json'

groundctrl = urllib.request.urlopen(majortom)

helmet = groundctrl.read()

helmetson = json.loads(helmet.decode('utf-8'))

print('\n\nConverted python data')

print(helmetson)

print('\n\nPeople in Space : ', helmetson['number'])

people = helmetson['people']

print(people)

print('name[1] , craft[1]')


for i in people:
    print(i.get('name') + ' on the ' + i.get('craft') + '.')



        
