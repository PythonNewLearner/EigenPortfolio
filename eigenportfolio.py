# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:36:01 2019

@author: baichen
"""
import pandas as pd
import numpy as np

from sklearn.decomposition import PCA
from sklearn import preprocessing
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import seaborn as sns

start=pd.to_datetime('2017-6-1')
end=pd.to_datetime('2019-5-25')
tickers=['JNJ','DIS','MSFT','PG','PFE','IBM','INTC','MMM','MRK','WBA','CSCO','AAPL','XOM','UNH','KO']
         #'CAT','GS','NKE','MCD','TRV','V','CVX','UTX','VZ','WMT','HD','AXP','JPM','BA']
df=pd.DataFrame()
for s in tickers:
    df[s]=web.DataReader(s,'yahoo',start=start,end=end)['Close']

df_ret=df.pct_change().dropna()
training_number=100
train_data=df_ret.iloc[:training_number,:]

cov_matrix=train_data.cov()

value,vector=np.linalg.eigh(cov_matrix)




eigen_port1=vector[-1]
eigen_port2=vector[-2]

eigen_norm_port1=eigen_port1/eigen_port1.sum()   #normalize the eigen vector, sum is one
eigen_norm_port2=eigen_port2/eigen_port2.sum()


eigenportfolio1=pd.DataFrame(eigen_norm_port1)
eigenportfolio2=pd.DataFrame(eigen_norm_port2)

print(vector)

eigenportfolio1.plot(kind='bar')
eigenportfolio2.plot(kind='bar')
plt.show();


# df_scaled=preprocessing.scale(df)
# pca=PCA()
# pca.fit(df_scaled)
# pca_data=pca.transform(df_scaled)
# print(pca.explained_variance_ratio_)







