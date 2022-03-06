import pandas as pd
import requests

# start and end dates since can only get 31 days at a time from API
start = ['2008-01-01','2008-02-01','2008-03-01','2008-04-01','2008-05-01','2008-06-01',
         '2008-07-01','2008-08-01','2008-09-01','2008-10-01','2008-11-01','2008-12-01']
end = ['2008-01-31','2008-02-29','2008-03-31','2008-04-30','2008-05-31','2008-06-30',
       '2008-07-31','2008-08-31','2008-09-30','2008-10-31','2008-11-30','2008-12-31']

# headers for API
headers = {'x-rapidapi-host': 'meteostat.p.rapidapi.com',
           'x-rapidapi-key': '8eb4564b2cmsh1fcd9ca19e5dd55p1326d8jsncd25d6c240cc'}

# empty dataframe to store the weather data in 
weather = pd.DataFrame()

# get data for each month from API and add to dataframe
for i in range(12):
    url = 'https://meteostat.p.rapidapi.com/stations/hourly?station=72530&start=' + start[i] + '&end=' + end[i]
    r=requests.get(url, headers=headers)
    weather = weather.append(pd.DataFrame(r.json()['data']))

# convert dataframe to csv
weather.to_csv('../../Data/original_data/weather_2008.csv')