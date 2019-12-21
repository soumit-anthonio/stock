import urllib
from pandas import DataFrame
import datetime
from dateutil.parser import parse
from datetime import date
from nsepy import get_history
import json
import sys
# import urllib
# import json
# from urllib.request import build_opener, HTTPCookieProcessor, Request
# from urllib.parse import urlencode
# from http.cookiejar import CookieJar

# import six
# import ast
# import re
# import json
# import zipfile
# import io
# from dateutil import parser
# from nsetools.bases import AbstractBaseExchange
# from nsetools.utils import byte_adaptor
# from nsetools.utils import js_adaptor
print('Your STOCK DATA already downloaded in the data folder')
sbin = get_history(symbol='SBIN',
                   start=date(2015, 1, 1),
                   end=date(2015, 1, 10))
sbin.to_csv('E:/stock/data/')
# symbol = sys.argv[1].upper()
# start = parse(sys.argv[2])
# end = datetime.datetime.now()
# print('Your STOCK DATA already downloaded in the data folder')
# stock_fut = get_history(symbol=symbol,
#                         start=start,
#                         end=end)
# print('Your STOCK DATA already downloaded in the data folder')
# print(stock_fut.head())
# print('Your STOCK DATA already downloaded in the data folder')
# df = DataFrame(stock_fut, columns=[
#                'Symbol', 'Series', 'Prev Close', 'Open', 'High', 'Low', 'Close', 'Volume'])
# Export = df.to_json(r'E:/stock/data/_data.json', orient='index')
# print('Your STOCK DATA already downloaded in the data folder')

# url = "http://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json"

# response = urllib.urlopen(url)

# data = json.loads(response.read())
# print(data)


# a = Nse()

# Export = a.get_top_gainers().to_json(r'E:/stock/data/_data1.json', orient='index')
# print('Your STOCK DATA already downloaded in the data 1folder')
# with open('E:/stock/data/_data.json', 'w') as json_file:
#     json.dump(stock_fut, json_file)
# print(stock_fut.head())
# for col in stock_fut.columns:
#     print(col)


# class Nse():
#     """
#     class which implements all the functionality for
#     National Stock Exchange
#     """
#     __CODECACHE__ = None

#     def __init__(self):
#         self.opener = self.nse_opener()
#         self.headers = self.nse_headers()
#         # URL list
#         self.get_quote_url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?'
#         self.stocks_csv_url = 'http://www.nseindia.com/content/equities/EQUITY_L.csv'
#         self.top_gainer_url = 'http://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json'
#         self.top_loser_url = 'http://www.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json'
#         self.top_fno_gainer_url\
#             = 'https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/fnoGainers1.json'
#         self.top_fno_loser_url = 'https://www.nseindia.com/live_market/dynaContent/live_analysis/losers/fnoLosers1.json'
#         self.advances_declines_url = 'http://www.nseindia.com/common/json/indicesAdvanceDeclines.json'
#         self.index_url = "http://www.nseindia.com/homepage/Indices1.json"
#         self.bhavcopy_base_url = "https://www.nseindia.com/content/historical/EQUITIES/%s/%s/cm%s%s%sbhav.csv.zip"
#         self.bhavcopy_base_filename = "cm%s%s%sbhav.csv"
#         self.active_equity_monthly_url =\
#             "https://www.nseindia.com/products/dynaContent/equities/equities/json/mostActiveMonthly.json"
#         self.year_high_url = "https://www.nseindia.com/products/dynaContent/equities/equities/json/online52NewHigh.json"
#         self.year_low_url = "https://www.nseindia.com/products/dynaContent/equities/equities/json/online52NewLow.json"
#         self.preopen_nifty_url = "https://www.nseindia.com/live_market/dynaContent/live_analysis/pre_open/nifty.json"
#         self.preopen_fno_url = "https://www.nseindia.com/live_market/dynaContent/live_analysis/pre_open/fo.json"
#         self.preopen_niftybank_url =\
#             "https://www.nseindia.com/live_market/dynaContent/live_analysis/pre_open/niftybank.json"
#         self.fno_lot_size_url = "https://www.nseindia.com/content/fo/fo_mktlots.csv"

#     def nse_opener(self):
#         """
#         builds opener for urllib2
#         :return: opener object
#         """
#         cj = CookieJar()
#         return build_opener(HTTPCookieProcessor(cj))

#     def nse_headers(self):
#         """
#         Builds right set of headers for requesting http://nseindia.com
#         :return: a dict with http headers
#         """
#         return {'Accept': '*/*',
#                 'Accept-Language': 'en-US,en;q=0.5',
#                 'Host': 'nseindia.com',
#                 'Referer': "https://www.nseindia.com/live_market\
#                     /dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=INFY&illiquid=0&smeFlag=0&itpFlag=0",
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
#                 'X-Requested-With': 'XMLHttpRequest'
#                 }

#     def get_top_gainers(self, as_json=False):
#         """
#         :return: a list of dictionaries containing top gainers of the day
#         """
#         url = self.top_gainer_url
#         req = Request(url, None, self.headers)
#         # this can raise HTTPError and URLError
#         res = self.opener.open(req)
#         # for py3 compat covert byte file like object to
#         # string file like object
#         res = byte_adaptor(res)
#         res_dict = json.load(res)
#         # clean the output and make appropriate type conversions
#         res_list = [self.clean_server_response(
#             item) for item in res_dict['data']]
#         return self.render_response(res_list, as_json)

#     def get_top_losers(self, as_json=False):
#         """
#         :return: a list of dictionaries containing top losers of the day
#         """
#         url = self.top_loser_url
#         req = Request(url, None, self.headers)
#         # this can raise HTTPError and URLError
#         res = self.opener.open(req)
#         # for py3 compat covert byte file like object to
#         # string file like object
#         res = byte_adaptor(res)
#         res_dict = json.load(res)
#         # clean the output and make appropriate type conversions
#         res_list = [self.clean_server_response(item)
#                     for item in res_dict['data']]
#         return self.render_response(res_list, as_json)
