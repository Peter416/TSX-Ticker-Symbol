import requests
import json

def get_tsx_tickers():
    # Request the TSX company directory in json format
    r = requests.get('https://www.tsx.com/json/company-directory/search/tsx/%5E*')

    # read the json file
    raw_data = r.json()

    # access the key which contains ticker symbols
    raw_data = raw_data['results']
    ticker_list  = [d['symbol'] for d in raw_data]
    return ticker_list