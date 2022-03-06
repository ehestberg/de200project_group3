cd .. 
mkdir original_data
cd original_data
wget http://ww2.amstat.org/sections/graphics/datasets/DataExpo2009.zip
unzip DataExpo2009.zip
rm DataExpo2009.zip
cd DataExpo2009
bunzip2 2008.csv.bz2
mv 2008.csv ..