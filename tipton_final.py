# -*- coding: utf-8 -*-
"""
@author: nick
"""
#import bs4, requests, matplotlib
from bs4 import BeautifulSoup as soup     
import requests
import matplotlib.pyplot as plt
import numpy as np

#statement telling what program is doing
print('Generating a weather forecast summary for Athens, OH and another city!')
#define the parent function called City
class City():
    #define the init function
    def __init__(self, s=' ', n=' ', lat=0, lon=0):
        self.state = s
        self.name = n
        self.latitude = lat
        self.longitude = lon
            
    #define the Info function
    def CityInfo(self):
        print("City State: " , self.state)
        print("City Name: " , self.name)
        print("City Latitude: " , self.latitude)
        print("City Longitude: " , self.longitude)

#define a child class of city called WeatherHigh
class WeatherHigh(City):
    #define the init function
    def __init__(self, h=0, p=' ', d=' ', c = City()):
        self.high = h
        self.period = p
        self.description = d
        City.__init__(self,c.state,c.name,c.latitude,c.longitude)

    #define the Info function
    def WeatherHighInfo(self):                
        City.CityInfo(self)
        print('City High Temperature: ',self.high)
        print('City Period: ',self.period)
        print('City Description: ',self.description)
        
#define a child class of city called WeatherLow    
class WeatherLow(City):
    #define the init function
    def __init__(self, l=0, pp=' ', dd=' ', c = City()):
        self.low = l
        self.periodd = pp
        self.descriptionn = dd
        City.__init__(self,c.state,c.name,c.latitude,c.longitude)

    #define the Info function
    def WeatherLowInfo(self):                
        City.CityInfo(self)
        print('City Low Temperature: ',self.low)
        print('City Period: ',self.periodd)
        print('City Description: ',self.descriptionn)

#variables to store exit codes and user input information for City
exit_codes = ['x']
listcity = []

#user begins to input information to create the first city with the given info
answers = input('Enter c (to create the first city), or x, (to quit): ')
print()
print('City state = ' 'OH')
print('City name = ' 'Athens')
print('Latitude coordinate = ' '39.3285')
print('Longitude coordinate = ' '-82.1044')
print()
#create a loop to add cities until 'x' has been entered
while answers not in exit_codes:
    if answers == 'c':
        s = input('Enter the city State: ')
        n = input('Enter the city Name: ')
        lat = input('Enter the city Latitude coordinate: ')
        lon = input('Enter the city Longitude coordinate: ')
        city=City(s,n,lat,lon)
        listcity.append(city)
        
    else:
        print('Invalid option')
        print()
        
    #ask user to create the next city or exit
    answers = input('Enter c (to create the next city), or x, (to quit): ')
    print()
    print('City state = ' 'IL')
    print('City name = ' 'Chicago')
    print('Latitude coordinate = ' '41.8843')
    print('Longitude coordinate = ' '-87.6324')
    print()

#storing city1 (Athens) latitude and longitude for url 
city_1 = [39.3285, -82.1044]
city_1_name = 'Athens, OH'
url1 = "https://forecast.weather.gov/MapClick.php?lat={}&lon={}#.YE-AuOlKifR".format(city_1[0], city_1[1])

#storing city2 (Chicago) latitude and longitude for url 
city_2 = [41.8843, -87.6324]
city_2_name = 'Chicago, IL'
url2 = "https://forecast.weather.gov/MapClick.php?lat={}&lon={}#.YISox-lKifQ".format(city_2[0], city_2[1])

#'get' the url information for each url
r = requests.get(url1)
rr = requests.get(url2)

#gather the text from web scrape for each url
html_code = soup(r.text, "html.parser")
html_codee = soup(rr.text, "html.parser")

#scraping specific data one day at a time for each url
episode = html_code.find_all("li", {"class": "forecast-tombstone"})
episodee = html_codee.find_all("li", {"class": "forecast-tombstone"})


#store infromation scraped from each city url
Alist = []
Llist = []

#store temperatures to graph
Ahigh = []
Alow = []
Lhigh = []
Llow = []

#store days to graph
hperiod = []
lperiod = []

#loop to pull "p" tags
#description and period name, that correspond with high temperatures
for i in range (0, len(episode)):
    cells=episode[i].find_all("p")
    if len(cells) > 3:
        if "High: " in cells[3].text:
            p = (cells[0].text)
            hperiod.append(p)
            d = (cells[2].text)
            #get only numeric values for the temperatures
            h_ = (cells[3].text)
            h__ = []
            for word in h_.split():
                if word.isdigit():
                    h__.append(int(word))
                    h = str(h__).lstrip('[').rstrip(']')
                    Ahigh.append(h)
                    #append collected data to list for Athens WeatherHigh
                    highseries=WeatherHigh(h, p, d, listcity[0])
                    Alist.append(highseries)
        else:
            #description and period name, that correspond with low temperatures
            if "Low: " in cells[3].text:
                pp = (cells[0].text)
                lperiod.append(pp)
                dd = (cells[2].text)
                #get only numeric values for the temperatures
                l_ = (cells[3].text)
                l__ = []
                for word in l_.split():
                    if word.isdigit():
                        l__.append(int(word))
                        l = str(l__).lstrip('[').rstrip(']')
                        Alow.append(l)
                        #append collected data to list for Athens WeatherLow
                        lowseries=WeatherLow(l, pp, dd, listcity[0])
                        Alist.append(lowseries)

#loop to pull "p" tags
#description and period name, that correspond with high temperatures
for i in range (0, len(episodee)):
    cells=episodee[i].find_all("p")
    if len(cells) > 3:
        if "High: " in cells[3].text:
            p = (cells[0].text)
            d = (cells[2].text)
            #get only numeric values for the temperatures
            h_ = (cells[3].text)
            h__ = []
            for word in h_.split():
                if word.isdigit():
                    h__.append(int(word))
                    h = str(h__).lstrip('[').rstrip(']')
                    Lhigh.append(h)
                    #append collected data to list for Chicago WeatherHigh
                    highseries=WeatherHigh(h, p, d, listcity[1])
                    Llist.append(highseries)
        else:
            #description and period name, that correspond with low temperatures
            if "Low: " in cells[3].text:
                pp = (cells[0].text)
                dd = (cells[2].text)
                #get only numeric values for the temperatures
                l_ = (cells[3].text)
                l__ = []
                for word in l_.split():
                    if word.isdigit():
                        l__.append(int(word))
                        l = str(l__).lstrip('[').rstrip(']')
                        Llow.append(l)
                        #append collected data to list for Chicago WeatherLow
                        lowseries=WeatherLow(l, pp, dd, listcity[1])
                        Llist.append(lowseries)
                        
#use a dictionary to store the counts
b = {'WeatherHigh': 0, 'WeatherLow': 0 }
b1 = {'Cloudy': 0, 'Clear': 0, 'Rain': 0, 'Wind': 0 }
#use two lists to store the counts
x = ['WeatherHigh', 'WeatherLow','WeatherHigh', 'WeatherLow']
x1 = ['Cloudy', 'Clear','Rain', 'Wind']
#y[0] - counts shape objects
#y[1] - counts circle objects
#y[2] - counts rectangle objects
#y[3] - counts square objects
y = [0,0,0,0]

#printing all information collected from user and webscrape 
#WeatherHigh, WeatherLow, and CityInfo inherited for Athens
for item in Alist:
    # print out the WeatherHigh info
    if type(item) is WeatherHigh:
        item.WeatherHighInfo()
        print()
        #increase the dictionary counter
        b['WeatherHigh'] += 1
        #increase the list counter
        y[0] = y[0] +1
        
    # print out the WeatherLow info
    elif type(item) is WeatherLow:
        item.WeatherLowInfo()
        print()
        #increase the dictionary counter
        b['WeatherLow'] += 1
        #increase the list counter
        y[1] = y[1] +1
    
    else:
        print('Type is not recognized')
    
    print()

#printing all information collected from user and webscrape 
#WeatherHigh, WeatherLow, and CityInfo inherited for Athens
for item in Llist:
    # print out the WeatherHigh info
    if type(item) is WeatherHigh:
        item.WeatherHighInfo()
        print()
        #increase the dictionary counter
        b['WeatherHigh'] += 1
        #increase the list counter
        y[2] = y[2] +1
        
    # print out the WeatherLow info      
    elif type(item) is WeatherLow:
        item.WeatherLowInfo()
        print()
        #increase the dictionary counter
        b['WeatherLow'] += 1
        # #increase the list counter
        y[3] = y[3] +1
        
    else:
        print('Type is not recognized')
    
    print()
    
for i in range(0,len(Ahigh)):
    Ahigh[i] = int(Ahigh[i])
for i in range(0,len(Lhigh)):
    Lhigh[i] = int(Lhigh[i])
    
for i in range(0,len(Alow)):
    Alow[i] = int(Alow[i])
for i in range(0,len(Llow)):
    Llow[i] = int(Llow[i])

#variables for graphing high temperatures
x3 = Ahigh  
z4 = Lhigh 
y7 = hperiod[0:5]

#variables for graphing low temperatures
x33 = Alow  
z44 = Llow 
y77 = lperiod[0:5]

#creating figures
fig, axs = plt.subplots(3,1, figsize=(12,8))
x_axis = np.arange(len(hperiod))
x_axis2 = np.arange(len(lperiod))

#creating title of graphs
axs[0].set_title(city_1_name + ' & ' + city_2_name)

#creating graphs for high temperatures
axs[0].plot(y7, x3, label='Athens', ls='solid', marker='o')
axs[0].plot(y7, z4,  label='Chicago', ls='dotted', marker='^')
axs[0].set_xticks(x_axis)
axs[0].set_xticklabels(hperiod)
axs[0].legend()

#creating graphs for low temperatures
axs[1].plot(y77, x33, label='Athens', ls='solid', marker='o')
axs[1].plot(y77, z44,  label='Chicago', ls='dotted', marker='^')
axs[1].set_xticks(x_axis2)
axs[1].set_xticklabels(lperiod)
axs[1].legend()

#if using a dictionary, set up 2 lists to graph
#creating bar graph to count occurrences of description words
x_axis3 = list(b1.keys())
y_axis3 = list(b1.values())

#bar graph for the 2 lists
axs[2].bar(x1,y)

#bar graph for the dictionary
axs[2].bar(x_axis3,y_axis3)

#creating title for the figure
fig.suptitle('1-Day Forecast Comparison for Two Cities')

#saving figure
fig.savefig('tipton_final-graphs.png')
