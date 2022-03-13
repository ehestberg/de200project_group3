# DE200 Final Project G3
Emma Estberg and Samuel Jung

## Data
Contains all the data used 
### original 
`2008.csv` has all of the US commerical flight data from 2008. `ORD_2008.csv` has all the flights departing from O'Hare airport in 2008. `weather_2008.csv` has the hourly weather data for 2008.
### cleaned
Weather and flight data after cleaned. 
Flight data was cleaned by removing all flights that did not have departure or arrival times, scheduled and actual. 
A rounded scheduled departure time was also added, so if the scheduled departure time was before XX:30 then the time would be rounded to XX:00 and if it was after it would be rounded to XX+1:30.

Weather data was cleaned by removing variables that were unimportant or valueless, like total snow in the past hour and the weather condition code. 
### combined 
`combined.csv` contains all of the flights from the cleaned flight data matched with the weather data. Matching was done by getting the weather data for the rounded scheduled departure time. 
### condensed 
`condensed.ipynb` is the code used to condense the combined data. The condensed data takes the first 3 or 5 flights for each date and time. 

## Extract and Clean Data 
### get_data 
Contains the scripts for downloaded and converting the data to csv files. 
`get_flight_data.sh` downloads the flight data and unzips the files needed. `get_ORD_flights.py` selects only the flights departing from O'Hare in 2008 and saves a csv file with the data. `get_weather_data.py` gets the hourly weather data from the Meteostat Developers API and saves it as a csv file. 
### combine 
`combine.py` contains the script for matching the flight data with the weather data and saving it as a csv file.

## plots
`plots.ipynb` uses `matplotlib.pyplot` to create plots for departure delay vs average temperature, wind speed, dew point, and precipitation as well as precipitation vs average departure delay. 
The plots are included in the folder as well.

## tableau 
Contains Tableau workbooks for plotting.
