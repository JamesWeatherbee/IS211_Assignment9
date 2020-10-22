# Assignment 9 football_stats.py

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import os, ssl

# This is needed to avoid CERTIFICATE ERRORS
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
     ssl._create_default_https_context = ssl._create_unverified_context
# DO NOT DELETE ABOVE

my_url = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

counter = 0
# Uses page_soup to scrape information for each player.
for name_span in page_soup.find_all('span', class_='CellPlayerName--long'):
     player_name = name_span.a.text
     position_span = page_soup.find('span', class_='CellPlayerName-position')
     position = position_span.text.strip()
     team_span = page_soup.find('span', class_='CellPlayerName-team')
     team = team_span.text.strip()

     # Outputs the counter, name, position, and team.  Missing the total touchdowns.
     print(str(counter + 1) + ') ' + player_name + '\t' + position + '\t' + team + '\t')
     counter += 1
     if counter >= 20:
          break




'''
first_td = page_soup.find('span', class_='TableBase-bodyTd--number')
td_first = first_td
if td_first == None:
     td_first = 0
print(td_first)
'''

# This is my attempt at getting the value from the first td column.
for first_td in page_soup.find('span', class_='TableBase-bodyTd--number'):
     td_first = first_td
     if td_first == None:
          td_first = 0
     print(td_first)

# This returns this error:
# TypeError: 'NoneType' object is not iterable

