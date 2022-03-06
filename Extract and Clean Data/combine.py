import pandas as pd

flights = pd.read_csv('../Data/ORD_2008_clean.csv')
weather = pd.read_csv('../Data/weather_2008_clean.csv')

temp = []
dwpt = []
rhum = []
prcp = []
wdir = []
wspd = []
pres = []
for i in range(len(flights)):
    match = weather[weather['time'] == flights.iloc[i]['CRSDepRound']]
    temp.append(match['temp'].values[0])
    dwpt.append(match['dwpt'].values[0])
    rhum.append(match['rhum'].values[0])
    prcp.append(match['prcp'].values[0])
    wdir.append(match['wdir'].values[0])
    wspd.append(match['wspd'].values[0])
    pres.append(match['pres'].values[0])
flights_and_weather = flights 
flights_and_weather['Temp'] = temp
flights_and_weather['DewPoint'] = dwpt
flights_and_weather['RelHumidity'] = rhum
flights_and_weather['Precip'] = prcp
flights_and_weather['WindDir'] = wdir
flights_and_weather['WindSpeed'] = wspd
flights_and_weather['AirPressure'] = pres

flights_and_weather.to_csv('../Data/combined.csv')