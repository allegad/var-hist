#https://blog.quantinsti.com/calculating-value-at-risk-in-excel-python/?utm_campaign=News&utm_medium=Community&utm_source=DataCamp.com

#1 is to import the necessary libraries
# Data manipulation
import numpy as np
import pandas as pd

#plotting
import matplotlib.pyplot as plt
import seaborn

#data fetching
import yfinance as yf

#print VaR values in tabular format
from tabulate import tabulate

#2 is to calc the daily percentage returns and plot in histogram
#download time series data from yahoo with Open, High, Low, Close, Adj Close, Volume
df = yf.download('FB','2012-01-01','2018-01-31')

#calc the returns of the close price with (t1-t0)/t0 and append to the end of the table and call it 'Returns'
df['Returns'] = df.Close.pct_change()
print(df)

#drop blank values from the time series or historical data
df = df.dropna()

#plot the returns in a histogram
plt.hist(df.Returns, bins=40)
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

#3 is to sort the returns
df.sort_values('Returns', inplace= True, ascending= True)
print(df.sort_values)

#4 - calc var
VaR_90 = df['Returns'].quantile(0.1)
VaR_95 = df['Returns'].quantile(0.05)
VaR_99 = df['Returns'].quantile(0.01)

#5 format int table
table = tabulate([['90%',VaR_90],['95%',VaR_95],['99%',VaR_99]],headers=['CI','VaR'])
print(table)

#add project to github
cd var-hist
git remote add origin https://github.com/allegad/var-hist.git
git push --tags
 



