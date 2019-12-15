from pandas import DataFrame
import datetime
from dateutil.parser import parse

from nsepy import get_history
import json
import sys

symbol = sys.argv[1].upper()
start = parse(sys.argv[2])
end = datetime.datetime.now()

# from nsetools import Nse
# nse = Nse()
#data = nse.get_quote('infy', as_json=True)
# Stock options (Similarly for index options, set index = True)
stock_fut = get_history(symbol=symbol,
                        start=start,
                        end=end)
print(stock_fut.head())
# with open('E:/stock/data/_data.json', 'w') as json_file:
#   json.dump(stock_fut, json_file)
# df = stock_fut[['Symbol', 'Open', 'High', 'Low', 'Close', 'Volume']]
df = DataFrame(stock_fut, columns=[
               'Symbol', 'Series', 'Prev Close', 'Open', 'High', 'Low', 'Close', 'Volume'])
Export = df.to_json(r'E:/stock/data/_data.json', orient='index')
# with open('E:/stock/data/_data.json', 'w') as json_file:
#     json.dump(stock_fut, json_file)
# print(stock_fut.head())
for col in stock_fut.columns:
    print(col)
print('Your STOCK DATA already downloaded in the data folder')
