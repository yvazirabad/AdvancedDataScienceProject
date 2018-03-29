#!/usr/bin/python

import os

ghc_stations = {}

with open(r'C:\Users\ivazirabad\AdvancedDataScience\ghcnd-stations.txt') as infile:
    for line in infile:
        splitline = line.rstrip().split('\t')
        ghc_stations[splitline[0]] = (splitline[1], splitline[2])

coreset = set()
for directory, folders, files in os.walk(r'C:\Users\ivazirabad\AdvancedDataScience\YearlyClimate\weather_station_pos'):
    for f in files:
        if f.endswith('weather_stations.txt'):
            littleset = set()
            year = os.path.splitext(f)[0].split('_')[0]
            with open(os.path.join(directory, f)) as infile:
                infile.readline()
                for line in infile:
                    splitline = line.rstrip().split('\t')
                    littleset.add(splitline[0])
            if year == '1900':
                coreset = coreset.union(littleset)
            else:
                coreset = coreset.intersection(littleset)
            print(year, len(coreset), sep='\t')

with open(os.path.join(r'C:\Users\ivazirabad\AdvancedDataScience\YearlyClimate\weather_station_pos\totals\coreweatherstation.txt'), 'w') as outfile:
    outfile.write('\t'.join(['Station', 'Lat', 'Long', '\n']))
    for station in coreset:
        if station in ghc_stations:
            outfile.write(station + '\t' + '\t'.join(ghc_stations[station]) + '\n')