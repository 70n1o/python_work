#import csv
#
#filename = 'data/sitka_weather_07-2018_simple.csv'
#with open(filename) as f:
#    reader = csv.reader(f)
#    header_row = next(reader)
#
#    for index, column_header in enumerate(header_row):
#        print(index, column_header)



"""Extracting and Reading Data."""

#
#import csv
#
#filename = 'data/sitka_weather_07-2018_simple.csv'
#with open(filename) as f:
#    reader = csv.reader(f)
#    header_row = next(reader)
#
#    #Get high temps from this file.
#    highs = []
#    for row in reader:
#        high = int(row[5])
#        highs.append(high)
#
#    print(highs)



"""Plotting Data in a Temperature Chart."""

#
#import csv
#
#import matplotlib.pyplot as plt
#
#filename = 'data/sitka_weather_07-2018_simple.csv'
#with open(filename) as f:
#    reader = csv.reader(f)
#    header_row = next(reader)
#
#    #Get high temps from this file.
#    highs = []
#    for row in reader:
#        high = int(row[5])
#        highs.append(high)
#
#
##Plot the high temps.
#plt.style.use('seaborn-v0_8')
#fig, ax = plt.subplots()
#ax.plot(highs, c='red')
#
##Format plot.
#ax.set_title("Daily high temps, July 2018", fontsize=24)
#ax.set_xlabel('', fontsize=16)
#ax.set_ylabel("Temp (F)", fontsize=16)
#ax.tick_params(axis='both', which='major', labelsize=16)
#
#plt.show()


"""Plotting Dates."""


#import csv
#from datetime import datetime
#
#import matplotlib.pyplot as plt
#
#filename = 'data/sitka_weather_07-2018_simple.csv'
#with open(filename) as f:
#    reader = csv.reader(f)
#    header_row = next(reader)
#
#    #Get  dets and high temps from this file.
#    dates, highs = [], []
#    for row in reader:
#        current_date = datetime.strptime(row[2], '%Y-%m-%d')
#        high = int(row[5])
#        dates.append(current_date)
#        highs.append(high)
#
#
##Plot the high temps.
#plt.style.use('seaborn-v0_8')
#fig, ax = plt.subplots()
#ax.plot(dates, highs, c='red')
#
##Format plot.
#ax.set_title("Daily high temps, July 2018", fontsize=24)
#ax.set_xlabel('', fontsize=16)
#fig.autofmt_xdate()
#ax.set_ylabel("Temp (F)", fontsize=16)
#ax.tick_params(axis='both', which='major', labelsize=16)
#
#plt.show()



import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Get  dates and high temps from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)


#Plot the high temps.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#Format plot.
ax.set_title("Daily high temps, 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temp (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()