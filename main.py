import json
import sys
import urllib.request
import time
from nsetools import Nse
nse = Nse()

data_main = {}


def import_web(stock,start,end):
    """
    :param ticker: Takes the company ticker
    :return: Returns the HTML of the page
    """
    url = 'https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol='+stock+'&segmentLink=3&symbolCount=2&series=ALL&dateRange=+&fromDate='+start+'&toDate='+end+'&dataType=PRICEVOLUMEDELIVERABLE'
    req = urllib.request.Request(url, headers={'User-Agent' : "Chrome Browser"}) 
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
    
    print (
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
    #assign: stores html tag to find where data starts
    searchString2 = '</div>'
    #stores:  stores html tag where  data end
    sta = string_html.find(searchString)
    print(sta)
    # returns & store: find() method returns the lowest index of the substring (if found). If not found, it returns -1.
    #data = string_html[sta + 84543:]
    #returns & stores: skips 43 characters and stores the index of substring
    #end = data.find(searchString2)
    # returns & store: find() method returns the lowest index of the substring (if found). If not found, it returns -1.
    #fdata = data[:end]
    #fetch: stores the fetched data into fdata
    #stripped = fdata.strip()
    #removes: blank spaces
    #return stripped





print('Your STOCK DATA already downloaded in the data folder')





	


ticker='tcs'
ticker = ticker.upper()
#print('Your STOCK NAME IS ' + sys.argv[1])
string_html = import_web(ticker, '01-12-2019', '31-12-2019')
print(string_html)
#filter_data(string_html)
#print(filter_data(string_html))
#get_data(filter_data(string_html),ticker)


#with open('E:/stock/data/_data.json', 'w') as json_file:
 #   json.dump(data_main, json_file)
#with open('E:/stock/data/_data.json','w') as f:
#	    f.write(str(data_main))
#q = nse.get_quote(sys.argv[1])
#q = nse.get_quote('TCS')
#from pprint import pprint
# pprint(q)
    # with open('E:/stock/data/'+sys.argv[1]+'_data.json', 'w') as json_file:
#with open('E:/stock/data/_data.json', 'w') as json_file:
    #json.dump(q, json_file)