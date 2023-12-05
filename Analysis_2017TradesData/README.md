# Analysis of the 2017 TAQ NYSE Trades Data: An initial analysis

### Data pre-processing

**pre.py**: It reads the downloaded data, checks columns and records, and then save it to a datafile with columns of Symbol, Time, Ex (Exchange), SaleType and Price. <br>
Input: trades2017_202310232114.csv <br>
Output: trades2017_cleaned.csv <br>
Columns: Symbol, Time, Ex, SaleType, Price. <br>

**Prep2.py**: It reads the panel dataset of trades, checks the total observations, the number of stocks, and so on.  <br>
Input: trades2017_cleaned.csv <br>
Output: trades2017_cleaned2.csv <br>
Columns: Symbol, Time, Ex, SaleType, Price. <br>

**Prep3.py**: It reads data, checks the number of trades (data points) by stock. <br>
Input: trades2017_cleaned2.csv <br>
Output: trades2017_cleaned3.csv <br>
Columns: Symbol, Time, Ex, SaleType, Price. <br>

**prep4.py**: It creates monthly price data. <br>
Input: trades2017_Cleaned3.csv <br>
Output: trades2017_1m_med.csv <br>

**basicPlots.py**: some plots <br>
Input: trades2017_Cleaned3.csv <br>
Output: some graphs <br>


