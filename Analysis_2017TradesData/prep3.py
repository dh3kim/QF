import pandas as pd
import os
import time
import matplotlib.pyplot as plt
import seaborn as sns

os.chdir('C:/Users/HannK/OneDoc/StonyAMS520/code')

start = time.time()
raw=pd.read_csv('../dataCleaned/trades2017_Cleaned2.csv')
print(time.time() - start)

# trade data
# the number of trades by stock
raw.groupby(["Symbol"]).count()
Ntrade_by_Stock = raw.groupby(["Symbol"]).count().reset_index()
Ntrade_by_Stock = Ntrade_by_Stock[['Symbol','Time']].rename(columns={'Time': 'Count'})
Ntrade_by_Stock.describe()
Ntrade_by_Stock.hist(column='Count')

# the number of trades by stock
# create date and month
raw["Time"] = pd.to_datetime(raw["Time"])
raw['Date'] = raw['Time'].dt.date
raw['Month'] = raw['Time'].dt.strftime('%b')
raw['MonthA'] = raw['Time'].dt.month_name()

# the number of trades by stock and month
raw.groupby(["Symbol", "MonthA"]).count()
Ntrade_by_Stock_Month = raw.groupby(["Symbol", "MonthA"]).count().reset_index()
Ntrade_by_Stock_Month = Ntrade_by_Stock_Month[['Symbol','MonthA', 'Time']].rename(columns={'Time': 'Count'})
Ntrade_by_Stock_Month.sort_values(by=['MonthA', 'Symbol'])

fig, ax = plt.subplots()
sns.boxplot(x='MonthA',y='Count',data=Ntrade_by_Stock_Month,ax=ax)
Ntrade_by_Stock_Month.describe()
Ntrade_by_Stock.describe()
# the number of trades varies across stock

# drop less traded stocks
# check symbol name 12 less traded stocks
Ntrade_by_Stock[0:15]
Ntrade_by_Stock[Ntrade_by_Stock['Count'] < 20]
Ntrade_by_Stock[Ntrade_by_Stock['Count'] < 40]
low_traded_stock = list(Ntrade_by_Stock.loc[Ntrade_by_Stock['Count'] < 40, 'Symbol'].iloc())
raw = raw[~raw['Symbol'].str.contains('|'.join(low_traded_stock))]
raw.groupby(["Symbol"]).count()
raw.groupby(["Symbol"]).count().describe()
raw['Month'] = raw['Time'].dt.month

# Save file.
#raw[['Symbol','Time', 'Ex', 'SaleType','Price']].sort_values(by=['Symbol', 'Time']).to_csv('../dataCleaned/trades2017_cleaned3.csv', sep=',')

# see BasicPlots.py.
