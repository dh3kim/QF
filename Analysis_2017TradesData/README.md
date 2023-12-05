# Analysis of the 2017 TAQ NYSE Trades Data: An initial analysis

pre.py: It reads the downloaded data, checks columns and records, and then save it to a datafile with columns of Symbol, Time, Ex (Exchange), SaleType and Price.
Input: trades2017_202310232114.csv
Output: trades2017_cleaned.csv
Columns: Symbol, Time, Ex, SaleType, Price.

Prep2.py: It reads the panel dataset of trades, checks the total observations, the number of stocks, and so on. 
Input: trades2017_cleaned.csv
Output: trades2017_cleaned2.csv
Columns: Symbol, Time, Ex, SaleType, Price.

Prep3.py: It reads data, checks the number of trades (data points) by stock.
Input: trades2017_cleaned2.csv 
Output: trades2017_cleaned3.csv
Columns: Symbol, Time, Ex, SaleType, Price.

prep4.py: It creates monthly price data
Input: trades2017_Cleaned3.csv
Output: trades2017_1m_med.csv

basicPlots.py: some plots
Input: trades2017_Cleaned3.csv
Output: some graphs


