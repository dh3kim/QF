import pandas as pd
import os
import time
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

os.chdir('C:/Users/HannK/OneDoc/StonyAMS520/code')

# data from prep3.py.
start = time.time()
raw=pd.read_csv('../dataCleaned/trades2017_Cleaned3.csv')
print(time.time() - start)

# monthly price data
raw["Time"] = pd.to_datetime(raw["Time"])
raw['Month'] = raw['Time'].dt.month
raw_1m = raw.set_index("Time").groupby("Symbol").resample("1m")['Price'].median()
raw_1m_df = raw_1m.reset_index()
raw_1m_df.to_csv('../dataCleaned/trades2017_1m_med.csv', sep=',')
