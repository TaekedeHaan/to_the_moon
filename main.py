# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt   # Import matplotlib
import pandas as pd
import quandl
import datetime
import pandas_candlestick as candlestick


# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2016,1,1)
end = datetime.date.today()
apiKey = '99CZfV56mrUsiPxRX1go'
# Let's get Apple stock data; Apple's ticker symbol is AAPL
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
s = "AAPL"
apple = quandl.get("WIKI/" + s, start_date=start, end_date=end, api_key = apiKey)
 
type(apple)

# pylab.rcParams['figure.figsize'] = (15, 9)   # Change the size of plots
 
# apple["Adj. Close"].plot(grid = True) # Plot the adjusted closing price of AAPL
candlestick.pandas_candlestick_ohlc(apple, adj=True, stick="month")