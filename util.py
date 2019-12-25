import urllib
import json
import requests
import pandas as pd


class Util():
    def __init__(self):
        self.url = "https://beta.nseindia.com/api/historical/cm/equity?symbol=@&series=[%22EQ%22]&from=!&to=20-12-2019"

    def get_quote(self, stock, start, end):
        r = requests.get(
            self.url.replace('@', stock.upper()).replace('!', start).replace('*', end))
        # print(r.json())
        with open('E:/stock/data/_data.json', 'w') as json_file:
            json.dump(r.json(), json_file)
        # df = pd.DataFrame(r).filter(items=['data'])
        # print(df)
        # # Export = df.to_json(r'E:/stock/data/_data1.json', orient='values')
        # Export = df.to_json(r'E:/stock/data/_data1.json', orient='table')
        print('Your STOCK DATA already downloaded in the data folder')
