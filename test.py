import pandas_datareader as pdr
from datetime import date



df = pdr.get_data_yahoo(symbols="TSLA", start=date(2021, 10, 1), end=date(2021, 11, 1))

print(df.index)
print(date(2021,10,1))