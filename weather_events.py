#!/usr/bin/python

import os, csv

path = r'C:\Users\ivazirabad\AdvancedDataScience\StormEvents\csvfiles\cleaned'
mydict = {}
mylist = ['Thunderstorm Wind','Tornado','Flood','Hail','Flash Flood','Marine Thunderstorm Wind','Marine Strong Wind',
         'Marine High Wind','Winter Weather','Waterspout','Heavy Rain','Lightning','High Wind','Heavy Snow',
         'Debris Flow','Drought','Strong Wind','Winter Storm','Cold/Wind Chill','Coastal Flood','Wildfire',
         'Funnel Cloud','Blizzard','Ice Storm','Marine Hail','Dense Fog','Extreme Cold/Wind Chill','Lake-Effect Snow',
         'Rip Current','High Surf','Frost/Freeze','Avalanche','Astronomical Low Tide','Sleet','Sneakerwave',
         'Excessive Heat','Heat','Dust Storm','Freezing Fog','Hurricane','Dust Devil','Lakeshore Flood',
         'Marine Tropical Storm','Tropical Storm','Storm Surge/Tide','Marine Hurricane/Typhoon',
         'Tropical Depression','Dense Smoke','Marine Tropical Depression']

for item in mylist:

    for year in range(1950, 2018):
        if item not in mydict:
            mydict[item] = [{year: 0}]
        else:
            mydict[item].append({year: 0})

for directory, folders, files in os.walk(path):
    for f in files:
        year = int(os.path.splitext(f)[0][24:28])
        print(year)
        with open(os.path.join(directory, f)) as infile:
            infile.readline()
            stormreader = csv.reader(infile, delimiter=',', quotechar='"')
            for row in stormreader:
                for years in mydict[row[0]]:
                    mydict[row[0]][year] += 1

for k, v in mydict.items():
    for mytup in v:
        for year, count in mytup.items():
            print(k, year, count)