import requests
from urllib.parse import urlencode
from urllib.request import build_opener, HTTPCookieProcessor, Request
from nsetools.utils import js_adaptor
from nsetools.utils import byte_adaptor
from nsetools.bases import AbstractBaseExchange
from dateutil import parser
import io
import zipfile
import re
import ast
import six
import json
import sys
import urllib.request
import time
from nsetools import Nse
nse = Nse()

data_main = {}


def import_web(stock, start, end):
    """
    :param ticker: Takes the company ticker
    :return: Returns the HTML of the page
    """
    url = 'https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol='+stock + \
        '&segmentLink=3&symbolCount=2&series=ALL&dateRange=+&fromDate=' + \
        start+'&toDate='+end+'&dataType=PRICEVOLUMEDELIVERABLE'
    req = urllib.request.Request(url, headers={'User-Agent': "Chrome Browser"})
    fp = urllib.request.urlopen(req, timeout=80)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr


def get_data(stripped, company):
    js = json.loads(stripped)
    datajs = js['data'][0]
    subdictionary = {}
    subdictionary['1. open'] = datajs['open']
    subdictionary['2. high'] = datajs['dayHigh']
    subdictionary['3. low'] = datajs['dayLow']
    subdictionary['4. close'] = datajs['lastPrice']
    subdictionary['5. volume'] = datajs['totalTradedVolume']

    print(
        'Adding value at : ',
        js['lastUpdateTime'],
        ' to ',
        company,
        ' Price:',
        datajs["lastPrice"],
    )
    data_main[js['lastUpdateTime']] = subdictionary


def filter_data(string_html):
    searchString = '<div id="csvContentDiv" style="display:none;">'
    # assign: stores html tag to find where data starts
    searchString2 = '</div>'
    # stores:  stores html tag where  data end
    sta = string_html.find(searchString)
    print(sta)
    # returns & store: find() method returns the lowest index of the substring (if found). If not found, it returns -1.
    #data = string_html[sta + 84543:]
    # returns & stores: skips 43 characters and stores the index of substring
    #end = data.find(searchString2)
    # returns & store: find() method returns the lowest index of the substring (if found). If not found, it returns -1.
    #fdata = data[:end]
    # fetch: stores the fetched data into fdata
    #stripped = fdata.strip()
    # removes: blank spaces
    # return stripped


print('Your STOCK DATA already downloaded in the data folder')


ticker = 'tcs'
ticker = ticker.upper()
#print('Your STOCK NAME IS ' + sys.argv[1])
string_html = import_web(ticker, '01-12-2019', '31-12-2019')
print(string_html)
# filter_data(string_html)
# print(filter_data(string_html))
# get_data(filter_data(string_html),ticker)


# with open('E:/stock/data/_data.json', 'w') as json_file:
#   json.dump(data_main, json_file)
# with open('E:/stock/data/_data.json','w') as f:
#	    f.write(str(data_main))
#q = nse.get_quote(sys.argv[1])
#q = nse.get_quote('TCS')
#from pprint import pprint
# pprint(q)
# with open('E:/stock/data/'+sys.argv[1]+'_data.json', 'w') as json_file:
# with open('E:/stock/data/_data.json', 'w') as json_file:
#json.dump(q, json_file)

# ---------------------------------

"""
    The MIT License (MIT)

    Copyright (c) 2014 Vivek Jha

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""


class Util():
    def __init__(self):
        self.headers = self.nse_headers()

    def get_quote(self, code, as_json=False):
        #localFn = 'E:/stock/data/_data.json'
        #url = 'https://beta.nseindia.com/api/historical/cm/equity?symbol=TCS&series=[%22EQ%22]&from=18-12-2019&to=20-12-2019'
        # r = requests.get(url, stream=True)

        # req = Request(url, None)
        # print(self.render_response(req, as_json))
        # return True
        req = urllib.request.Request('http://www.voidspace.org.uk')

        with urllib.request.urlopen(req) as response:
        the_page = response.read()

    def render_response(self, data, as_json=False):
        if as_json is True:
            return json.dumps(data)
        else:
            return data

    def nse_headers(self):
        """
        Builds right set of headers for requesting http://nseindia.com
        :return: a dict with http headers
        """
        return {'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Host': 'nseindia.com',
                'Referer': "https://www.nseindia.com/live_market\
                /dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=INFY&illiquid=0&smeFlag=0&itpFlag=0",
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
                'X-Requested-With': 'XMLHttpRequest'
                }
