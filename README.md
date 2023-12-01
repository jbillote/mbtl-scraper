# MBTL Scraper
For scraping move information from Mizuumi

## Usage
python main.py \<character>

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

If no character is specified, then data is fetched for every character.

Data for characters is scraped from the Mizuumi wiki and saved to CSV files in 
the `movelist/mbtl` directory in the project directory. The directories are 
created if they don't exist.

## Dependencies
This project is dependent on the `beautifulsoup` and `requests` libraries, 
installed through `pip`. For more information, the full list of library 
dependencies are in `requirements.txt`, which can be used with `pip` to install 
all the required libraries.