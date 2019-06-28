#!/usr/bin/pyton3

import urllib.request
import json
import turtle

eoss= 'http://api.open-notify.org/iss-now.json'

trackiss = urllib.request.urlopen(eoss)

ztrack = trackiss.read()

result = json.loads(ztrack.decode('utf-8'))

print('\n\nConverted python data')

print(result)

input('\nISS data retrieved & converted. Press any key to continue')

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude: ',lat) 
print('Longtitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)

screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('iss_map.gif')

screen.register_shape('spriteiss.gif')
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

lon = round(float(lon))
lat = round(float(lat))
iss.penup()
iss.goto(lon, lat)
 

yellowlat= 18.52
yellowlon= 73.85
mylocation= turtle.Turtle()
mylocation.penup()
mylocation.color('yellow')
mylocation.goto(yellowlon, yellowlat)
mylocation.dot(5)
mylocation.hideturtle()


passiss= 'http://api.open-notify.org/iss-pass.json'
passiss= passiss + '?lat=' + str(yellolat) + '&lon=' + str(yellowlon)
response = urllib.request.urlopen(passiss)
result = json.loads(response.read().decode('utf-8'))

over = result['response'][0]['risetime']

import time

style = ('Arial' , 6, 'bold') 
mylocation.write(time.ctime(over), font=style)


turtle.mainloop()














