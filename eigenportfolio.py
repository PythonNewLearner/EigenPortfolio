import pandas as pd
import numpy as np
from sklearn.decomposition import   KernelPCA
from iexfinance.stocks import get_historical_data
import pandas_datareader.data as web

start=pd.to_datetime('2018-5-1')
end=pd.to_datetime('2019-5-1')
tickers=['JNJ','DIS','MSFT','PG','PFE','IBM','INTC','MMM','MRK','WBA','CSCO','AAPL','XOM','UNH','KO',
         'CAT','GS','NKE','MCD','TRV','V','CVX','UTX','VZ','WMT','HD','AXP','JPM','DOW','BA']
df=pd.DataFrame()
for s in tickers:
    df[s]=web.DataReader(s,'yahoo',start=start,end=end)['Close']

print(len(tickers))


