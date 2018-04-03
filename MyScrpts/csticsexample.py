import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.finance import candlestick2_ohlc
quotes = pd.read_csv(r'D:\USDRUB_160101_180323.txt')
fig, ax = plt.subplots()
candlestick2_ohlc(ax,quotes['open'],quotes['high'],quotes['low'],quotes['close'], width=0.5)
plt.show()