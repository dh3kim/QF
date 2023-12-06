import pandas as pd
import os
import time

os.chdir('C:/Users/HannK/OneDoc/StonyAMS520/code')

start = time.time()
raw=pd.read_csv('../dataIn/trades2017_202310232114.csv')
print(time.time() - start)

# Take a look at columns
#list(raw)
print(*raw, sep='\n')
raw = raw[['Time', 'Exchange', 'Sale_Condition', 'Symbol', 
           'Trade_Price', 'Sequence_Number', 'Date', 'YearMonth']]
raw = raw.rename(columns={'Exchange': 'Ex', 'Sale_Condition': 'SaleType',
                          'Trade_Price':'Price'})
print(*raw, sep='\n')

# Take a look at records
raw["Time"] = pd.to_datetime(raw["Time"])
raw.sort_values(by=['Symbol', 'Time', 'Sequence_Number'])
raw.drop_duplicates(['Symbol', 'Time', 'Sequence_Number'])

# SaleType
raw["SaleType"].value_counts()
raw = raw[~raw['SaleType'].str.contains('A|B|N|R|Z|4 B', na=False)]
raw["Ex"].value_counts()

# Save file
raw.sort_values(by=['Symbol', 'Time'])
raw.head(5)

raw['SaleType']

raw[raw['Symbol'] == 'AAPL']['Price'].describe()
raw[['Symbol','Time', 'Ex', 'SaleType','Price']].sort_values(by=['Symbol', 'Time']).to_csv('../dataCleaned/trades2017_cleaned.csv', sep=',')