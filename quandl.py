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
import numpy as np
import pandas_datareader.data as web    # Going to get SPY from Yahoo!


# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2016,1,1)
end = datetime.date.today()
apiKey = '99CZfV56mrUsiPxRX1go'
stockCodes = ["AAPL", "MSFT", "GOOG"]

# Get stock data; Apple's ticker symbol is AAPL
apple, microsoft, google = (quandl.get("WIKI/" + stockCode, start_date=start, end_date=end, api_key = apiKey) for stockCode in stockCodes)
 
# Create a DataFrame consisting of the adjusted closing price of these stocks, first by making a list of these objects and using the join method
stocks = pd.DataFrame({"AAPL": apple["Adj. Close"],
                      "MSFT": microsoft["Adj. Close"],
                      "GOOG": google["Adj. Close"]})


stocks.head() # display result
stocks.plot(grid = True)

# pylab.rcParams['figure.figsize'] = (15, 9)   # Change the size of plots
 
# apple["Adj. Close"].plot(grid = True) # Plot the adjusted closing price of AAPL
candlestick.pandas_candlestick_ohlc(apple, adj=True, stick="month")

# df.apply(arg) will apply the function arg to each column in df, and return a DataFrame with the result
# Recall that lambda x is an anonymous function accepting parameter x; in this case, x will be a pandas Series object
stock_return = stocks.apply(lambda x: x / x[0])
# stock_return.head() - 1 # display result

stock_change = stocks.apply(lambda x: np.log(x) - np.log(x.shift(1))) # shift moves dates back by 1.
# stock_change.head() # display result


stock_return.plot(grid = True).axhline(y = 1, color = "black", lw = 2)
stock_change.plot(grid = True).axhline(y = 1, color = "black", lw = 2)


spyder = web.DataReader("SPY", "yahoo", start, end)    # Didn't work
# spyder = web.DataReader("SPY", "google", start, end)    # Didn't work either
# If all else fails, read from a file, obtained from here: http://www.nasdaq.com/symbol/spy/historical
# spyderdat = pd.read_csv("/home/curtis/Downloads/HistoricalQuotes.csv")    # Obviously specific to my system; set to
                                                                          # location on your machine
spyderdat = pd.DataFrame(spyderdat.loc[:, ["open", "high", "low", "close", "close"]].iloc[1:].as_matrix(),
                         index=pd.DatetimeIndex(spyderdat.iloc[1:, 0]),
                         columns=["Open", "High", "Low", "Close", "Adj Close"]).sort_index()
 
spyder = spyderdat.loc[start:end]
 
stocks = stocks.join(spyder.loc[:, "Adj Close"]).rename(columns={"Adj Close": "SPY"})
stocks.head()

