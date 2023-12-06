import pandas as pd
import os
import time

os.chdir('C:/Users/HannK/OneDoc/StonyAMS520/code')

start = time.time()
raw=pd.read_csv('../dataCleaned/trades2017_Cleaned.csv')
print(time.time() - start)

# Panel data
# total observations, cross sectional units, and average per unit
raw.shape
raw['Symbol'].unique().shape
raw.shape[0]/raw['Symbol'].unique().shape[0]

# observations by unit
obs_by_unit = raw.groupby(["Symbol"])['Price'].count() 
obs_by_unit.describe()
raw.groupby(["Symbol"])['Price'].describe()
raw.groupby(["Symbol", "Date"]).count() 

#abnormal/unusual price
raw['Price'].describe()
raw = raw[raw.Price < 1200]
raw = raw[raw.Price > 1]
obs_by_unit.describe()
raw = raw[raw['Symbol'] != 'AAAA TEST'] 

# Save file
#raw[['Symbol','Time', 'Ex', 'SaleType','Price']].sort_values(by=['Symbol', 'Time']).to_csv('../dataCleaned/trades2017_cleaned2.csv', sep=',')
