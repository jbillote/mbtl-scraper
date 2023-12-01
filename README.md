# MBTL Scraper
For scraping move information from Mizuumi

Since this is a utility just for fetching and saving static web data, liberties 
such as not securely making SQL INSERT statements are taken.

In the future, I'm planning on cleaning up the code to make it more secure and 
easier to read, as well as making it easier to support other games. For now, 
the ony goal was to write something that would write data as needed.

## Usage
python main.py \<path_to_db>

For ease of use, the character parameter uses the following nickname mapping:
```
"tohno": "Shiki Tohno"
"arcueid": "Arcueid Brunestud"
"akiha": "Akiha Tohno"
"ciel": "Ciel"
"hisui": "Hisui"
"kohaku": "Kohaku"
"maids": "Hisui & Kohaku"
"miyako": "Miyako Arima"
"kouma": "Kouma Kishima"
"noel": "Noel"
"roa": "Michael Roa Valdamjong"
"vlov": "Vlov Arkhangel"
"warc": "Red Arcueid"
"saber": "Saber"
"aoko": "Aoko Aozaki"
"dan": "Dead Apostle Noel"
"mario": "Mario Gallo Bestino"
"pciel": "Powered Ciel"
"neco": "Neco-Arc"
"mash": "Mash Kyrielight"
"ushi": "Ushiwakamaru"
"dantes": "Monte Cristo"
```

Data for characters is scraped from the Mizuumi wiki and saved to the provided 
`sqlite` database. The database's tables will be destroyed and created every 
time as this is only intended to be ran when there are major game updates.

Data will also be saved to CSV files in the `movelist/mbtl` directory in the 
project directory. The directories are created if they don't exist.

## Dependencies
This project is dependent on the `beautifulsoup` and `requests` libraries, 
installed through `pip`. For more information, the full list of library 
dependencies are in `requirements.txt`, which can be used with `pip` to install 
all the required libraries.
