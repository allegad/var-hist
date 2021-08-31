import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn

import yfinance as yf

from tabulate import tabulate

df = yf.download('FB','2012-01-01','2018-01-31')

df['Returns'] = df.Close.pct_change()
print(df)

df = df.dropna()

plt.hist(df.Returns, bins=40)
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

df.sort_values('Returns', inplace= True, ascending= True)
print(df.sort_values)

VaR_90 = df['Returns'].quantile(0.1)
VaR_95 = df['Returns'].quantile(0.05)
VaR_99 = df['Returns'].quantile(0.01)

table = tabulate([['90%',VaR_90],['95%',VaR_95],['99%',VaR_99]],headers=['CI','VaR'])
print(table)
