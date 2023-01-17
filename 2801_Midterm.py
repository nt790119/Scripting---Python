#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nick
"""
import requests
from bs4 import BeautifulSoup as soup
import datetime

#intro to program
#user can copy and paste given data to retrieve weather forecast
print('Generating a weather forecast summary for Athens, OH and the city of your choice!')
print('NOTE: program will automatically end once information is complete')
print('\n')
print('Enter the following information when prompted to retrieve the weather forecast:')
print('City= ' 'Logan, OH')
print('Latitude coordinate = ' '39.5405')
print('Longitude coordinate = ' '-82.4068')

#contains pre-given city and coordinates as well as url
city_1 = [39.3235222, -82.1198955]
city_1_name = 'Athens, OH'
url1 = "https://forecast.weather.gov/MapClick.php?lat={}&lon={}#.YE-AuOlKifR".format(city_1[0], city_1[1])

#creating values to hold user name and coordinates
city_2 = []
city_2_name = []

#user inputs previous information to get weather forecast
name = input('Enter a city: ')
lat = input("Enter a city's latitude cordinate: ") 
lon = input("Enter a city's longitude cordinate: ")

#adding user input data into different values,
#name and coordinates
city_2_name.append(name)
city_2.append(lat)
city_2.append(lon)

#converting numbers to float integers to use in url
for i in range(0,len(city_2)):
    city_2[i] = float(city_2[i])

#link for user city with coordinates being placed inside url
city_2 = [39.5405, -82.4068]
city_2_name = 'Logan, OH'
url2 = "https://forecast.weather.gov/MapClick.php?lat={}&lon={}#.YE-t6elKifQ".format(city_2[0], city_2[1])

#opening output file to move data into
outputs = open("AtLoName.tipton_output.txt", "a", encoding="utf-8")
output = open("AtLoHighs.tipton_output.txt", "a", encoding="utf-8")
outpu = open("AtLoLows.tipton_output.txt", "a", encoding="utf-8")
outp = open("AtLoDesc.tipton_output.txt", "a", encoding="utf-8")


#getting data from tested urls
site = requests.get(url1)
sites = requests.get(url2)

#distinguising a variable for each city to locate weather forecast
AT = soup(site.text, 'html.parser')
LO = soup(sites.text, 'html.parser')



#making the day that the program ran show
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
today = days[datetime.datetime.today().weekday()]

#creating values to hold highs, lows, descriptions, and days
AthensName = []
AthensDesc = []
AthensHigh = []
AthensLow = []


outputs.write('\n')
outputs.write('{} / {}: '.format(city_1_name, today))
outputs.write('\n')
outputs.write('-'*50)
outputs.write('\n')

output.write('\n')
output.write('{} / {}  - Highs: '.format(city_1_name, today))
output.write('\n')
output.write('-'*50)
output.write('\n')

outpu.write('\n')
outpu.write('{} / {}  - Lows: '.format(city_1_name, today))
outpu.write('\n')
outpu.write('-'*50)
outpu.write('\n')

outp.write('\n')
outp.write('{} / {} - Descriptions: '.format(city_1_name, today))
outp.write('\n')
outp.write('-'*50)
outp.write('\n')




#gathering the days data and appending to values, also replacing This, Today, Ton with 'today's day'
for ATname in AT.find_all('p', class_="period-name"):
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    today = days[datetime.datetime.today().weekday()]
    # #output.write(ATname.get_text(separator=' '))
    AthensName.append(ATname.get_text(separator=' '))
AthensName = [item.replace("This", today) for item in AthensName]
AthensName = [item.replace("Today", today) for item in AthensName]
AthensName = [item.replace("Ton", today+' N') for item in AthensName]
outputs.write('\n'.join(map(str,AthensName)))
outputs.write('\n')


#gathering the high data and appending to values
for AThigh in AT.find_all('p', class_="temp temp-high"):
    # #output.write(AThigh.get_text(separator=' '))
    AthensHigh.append(AThigh.get_text(separator=' '))
    AThigh = [i.replace(":", ": ") for i in AThigh]
    for item in AThigh:
        for subitem in item.split():
            if(subitem.isdigit()):
                AthensHigh.append(subitem)
AthensH = AthensHigh[1::2] 
output.write('\n'.join(map(str,AthensH)))
output.write('\n')


#gathering the low data and appending to values
for ATlow in AT.find_all('p', class_="temp temp-low"):
   # #output.write(ATlow.get_text(separator=' '))
    AthensLow.append(ATlow.get_text(separator=' ')) 
    ATLow = [i.replace(":", ": ") for i in ATlow]
    for item in ATlow:
        for subitem in item.split():
            if(subitem.isdigit()):
                AthensLow.append(subitem)
AthensL = AthensLow[1::2] 
outpu.write('\n'.join(map(str,AthensL)))
outpu.write('\n')


#gathering the description data and appending to values
for ATdesc in AT.find_all('p', class_="short-desc"):
   # #output.write(ATdesc.get_text(separator=' '))
    AthensDesc.append(ATdesc.get_text(separator=' '))
outp.write('\n'.join(map(str,AthensDesc)))
outp.write('\n')



#making the day that the program ran show
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
today = days[datetime.datetime.today().weekday()]

#creating values to hold highs, lows, descriptions, and days
LoganName = []
LoganDesc = []
LoganHigh = []
LoganLow = []


outputs.write('\n')
outputs.write('{} / {}: '.format(city_2_name, today))
outputs.write('\n')
outputs.write('-'*50)
outputs.write('\n')

output.write('\n')
output.write('{} / {} - Highs: '.format(city_2_name, today))
output.write('\n')
output.write('-'*50)
output.write('\n')

outpu.write('\n')
outpu.write('{} / {} - Lows: '.format(city_2_name, today))
outpu.write('\n')
outpu.write('-'*50)
outpu.write('\n')

outp.write('\n')
outp.write('{} / {} - Descriptions: '.format(city_2_name, today))
outp.write('\n')
outp.write('-'*50)
outp.write('\n')



#gathering the days data and appending to values, also replacing This, Today, Ton with 'today's day'
for LOname in LO.find_all('p', class_="period-name"):
   # #output.write(LOname.get_text(separator=' '))
    LoganName.append(LOname.get_text(separator=' '))
LoganName = [item.replace("This", today) for item in LoganName]
LoganName = [item.replace("Today", today) for item in LoganName]
LoganName = [item.replace("Ton", today+' N') for item in LoganName]
outputs.write('\n'.join(map(str,LoganName)))
outputs.write('\n')


#gathering the high data and appending to values
for LOhigh in LO.find_all('p', class_="temp temp-high"):
   # #output.write(LOhigh.get_text(separator=' '))
    LoganHigh.append(LOhigh.get_text(separator=' '))
    LOhigh = [i.replace(":", ": ") for i in LOhigh]
    for item in LOhigh:
        for subitem in item.split():
            if(subitem.isdigit()):
                LoganHigh.append(subitem)
LoganH = LoganHigh[1::2] 
output.write('\n'.join(map(str,LoganH)))
output.write('\n')


#gathering the low data and appending to values 
for LOlow in LO.find_all('p', class_="temp temp-low"):
   # #output.write(ATlow.get_text(separator=' '))
    LoganLow.append(LOlow.get_text(separator=' ')) 
    LOLow = [i.replace(":", ": ") for i in LOlow]
    for item in LOlow:
        for subitem in item.split():
            if(subitem.isdigit()):
                LoganLow.append(subitem)
LoganL = LoganLow[1::2] 
outpu.write('\n'.join(map(str,LoganL)))
outpu.write('\n')


#gathering the description data and appending to values
for LOdesc in LO.find_all('p', class_="short-desc"):
  # #output.write(LOdesc.get_text(separator=' '))
   LoganDesc.append(LOdesc.get_text(separator=' '))
outp.write('\n'.join(map(str,LoganDesc)))
outp.write('\n')


#closing the output file
outputs.close()
output.close()
outpu.close()
outp.close()