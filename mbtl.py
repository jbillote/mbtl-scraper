from bs4 import BeautifulSoup
import csv
import os
import requests

BASE_URL = 'https://wiki.gbl.gg/w/Melty_Blood/MBTL/%character%'
BASE_OUTPUT_PATH = 'movelist/mbtl/%character%.csv'


class MBTLScraper:
    def __init__(self, character, character_url):
        self.url = BASE_URL.replace('%character%', character_url)
        self.output_path = BASE_OUTPUT_PATH.replace('%character%', character)
        self.character = character

    def scrape_movelist(self):
        print(f"Scraping move list for {self.character}")

        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')

        moves = []

        move_tables = soup.findAll(class_='movedata-container')
        for t in move_tables:
            inputs = t.findAll(class_='movedata-flex-framedata-name-item movedata-flex-framedata-name-item-middle')
            for i in inputs:
                move = {'name': t.previous_sibling.previous_sibling.text.strip(), 'input': i.text.strip()}

                info_table = i.parent.parent.findNextSibling()
                info_rows = info_table.findAll(style='text-align:center; height:29px;')

                # First row
                row = info_rows[0]
                cells = row.findChildren('td')

                move['damage'] = cells[0].text.strip()
                move['block'] = cells[1].text.strip()
                move['cancel'] = cells[2].text.strip()
                move['property'] = cells[3].text.strip()
                move['cost'] = cells[4].text.strip()
                move['attribute'] = cells[5].text.strip()

                # Second row
                row = info_rows[1]
                cells = row.findChildren('td')

                move['startup'] = cells[0].text.strip()
                move['active'] = cells[1].text.strip()
                move['recovery'] = cells[2].text.strip()
                move['overall'] = cells[3].text.strip()
                move['advantage'] = cells[4].text.strip()
                move['invuln'] = cells[5].text.strip()

                moves.append(move)

        print(f"Saving move list as CSV file for {self.character} to {self.output_path}")

        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        with open(self.output_path, 'w') as f:
            w = csv.DictWriter(f, moves[0].keys())
            w.writeheader()
            w.writerows(moves)

        print(f"Finished scraping and saving move list for {self.character} to {self.output_path}")
