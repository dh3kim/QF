import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

os.chdir('C:/Users/HannK/OneDoc/StonyAMS520/code')
df = pd.read_csv('../dataCleaned/trades2017_1m_med.csv')

# monthly return
df['logPrice'] = np.log(df.Price)
df['Return'] = df.groupby('Symbol')['logPrice'].diff()

# merge
factor_df = pd.read_csv('../dataIn/FF_Factors.csv')
factor_df = factor_df.rename(columns={'Unnamed: 0':'YearMonth', 'Mkt-RF':'Mkt-Return', 'RF':'rfReturn'})
factor_df['YearMonth'] = factor_df['YearMonth'].astype(str)

df["Time"] = pd.to_datetime(df["Time"])
df['Year'] = df['Time'].dt.year.astype(str)
df['Month'] = df['Time'].dt.month.astype(str)
df['YearMonth'] = df['Year'] + '0' + df['Month']

df.sort_values(by=['YearMonth'])
merged_df = pd.merge(df, factor_df, on='YearMonth', how="inner")
merged_df = merged_df.sort_values(by=['Symbol','Time'])

merged_df['excessReturn'] = merged_df['Return'] - merged_df['rfReturn']
merged_df['MktExcessReturn'] = merged_df['Mkt-Return']

# Save file
merged_df.to_csv('../dataCleaned/trades2017_return_factors.csv', sep=',')

# Regression analysis
import statsmodels.formula.api as sm
result = sm.ols(formula="excessReturn ~ MktExcessReturn", data=merged_df).fit()
print(result.params)
print(result.summary())

result = sm.ols(formula="excessReturn ~ MktExcessReturn + SMB + HML", data=merged_df).fit()
print(result.params)
print(result.summary())

# group-by regression
df = df.dropna()
Symbols = df['Symbol'].unique()
np.sort(Symbols)
Betas = []
for i, symbol in enumerate(Symbols):
    data = df[df['Symbol'] == symbol]
    if data.shape[0] > 5:
        result = sm.ols(formula="excessReturn ~ MktExcessReturn + SMB + HML", data=data).fit()
        Betas.append([symbol,result.params[1]]) 
# Save symbol and beta
beta_df = pd.DataFrame([[beta[0], beta[1]] for beta in Betas],
                  columns=['Symbol', 'Beta'])
beta_df.to_csv('../dataCleaned/trades2017_betas.csv', sep=',')