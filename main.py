from characters import URL_NAMES
from mbtl import MBTLScraper

import sys

if len(sys.argv) <= 1:
    for c in URL_NAMES:
        scraper = MBTLScraper(URL_NAMES[c])
        scraper.scrape_movelist()
else:
    if sys.argv[1] in URL_NAMES:
        scraper = MBTLScraper(URL_NAMES[sys.argv[1]])
        scraper.scrape_movelist()
