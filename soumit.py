import urllib
from pandas import DataFrame
import datetime
from dateutil.parser import parse
from datetime import date
from nsepy import get_history
import json
import sys
from util import Util

s = Util()
stock_name = sys.argv[1]
start_date = sys.argv[2]
end_date = sys.argv[3]
f = s.get_quote(stock_name.upper(), start_date, end_date)
