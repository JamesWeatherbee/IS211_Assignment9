# Assignment 9 apple_stocks.py
# Github:  https://github.com/JamesWeatherbee/IS211_Assignment9

from bs4 import BeautifulSoup
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)): ssl._create_default_https_context = ssl._create_unverified_context

from urllib.request import urlopen
html = urlopen("https://www.nasdaq.com/market-activity/stocks/aapl/historical")
bsObj = BeautifulSoup(html)

stockData = bsObj.findAll('tr')

def main():
    print('AAPL Daily Closing Prices:')
    for i in stockData:
        t_data = i.findAll('td', {"class":"historical-data_cell"})
        if len(t_data) is 7:
            date = t_data[0].contents[0]
            close = t_data[6].contents[0]
            print('Date: {}, Closing Price: {}').format(date, close)

if __name__ == '__main__':
    main()
