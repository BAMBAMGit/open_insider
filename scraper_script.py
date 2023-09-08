# BUILD SCRAPER FUNCTION
from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape_openinsider_and_return_df(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'tinytable'})
    data = []

    for row in table.find_all('tr')[1:]:  # Skip the header row
        cols = row.find_all('td')
        data.append([col.text.strip() for col in cols])

    df = pd.DataFrame(data, columns = ['X', 'Filing Date', 'Trade Date', 'Ticker', 'Company Name', 'Insider Name', 'Title', 'Trade Type  ', 'Price', 'Qty', 'Owned', 'ΔOwn', 'Value', '1d', '1w', '1m', '6m'])

    return df