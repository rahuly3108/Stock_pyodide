#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Read the list of tickers
data = pd.read_csv('ind_nifty200list.csv')
symbols_list = data['Symbol'].tolist()

# Define date range
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

# Function to get all stock data (Close prices)
def get_stock_data(symbols, start_date, end_date):
    stock_df = pd.DataFrame()
    for symbol in symbols:
        try:
            data = yf.download(symbol + ".NS", start=start_date, end=end_date, progress=False)['Close']
            stock_df[symbol] = data
        except Exception as e:
            print(f"Failed to get data for {symbol}: {e}")
    
    pct_df = stock_df.pct_change() * 100  # Calculate percentage change
    return stock_df, pct_df


# Function to get Nifty50 data
def get_nifty_data(start_date, end_date):
    nifty = yf.download("^NSEI", start=start_date, end=end_date, progress=False)['Close']
    nifty_df = nifty.reset_index()
    nifty_df.columns = ['Date', 'Nifty']

    # Copy for percentage change
    nifty_pct_df = nifty_df.copy()
    nifty_pct_df['Nifty'] = nifty_pct_df['Nifty'].pct_change() * 100

    return nifty_df, nifty_pct_df

# Function to calculate betas


# In[ ]:


stock_returns,stock_prt_chng = get_stock_data(symbols_list, start_date, end_date)
nifty_returns_without,nifty_returns = get_nifty_data(start_date, end_date)


# In[ ]:


stock_returns.to_csv('stock_returns.csv',index=False)
stock_prt_chng.to_csv('stock_prt_chng.csv',index=False)
nifty_returns.to_csv('nifty_returns.csv',index=False)
nifty_returns_without.to_csv('nifty_returns_without.csv',index=False)

