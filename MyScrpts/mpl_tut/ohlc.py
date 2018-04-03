from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import date2num
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime

def ohlc(g):
    date = []
    op = []
    hi = []
    lo = []
    cl = []
    for e in list(g)[1:]:
        lstmp = e.split(',')
        # DATE
        strl = lstmp[0]
        date.append(datetime.datetime.strptime(strl, '%d/%m/%y'))
        # OPEN
        strl = lstmp[2]
        op.append(float(strl))
        # HIGH
        strl = lstmp[3]
        hi.append(float(strl))
        # LOW
        strl = lstmp[4]
        lo.append(float(strl))
        # CLOSE
        strl = lstmp[5]
        cl.append(float(strl))

    ax = plt.subplot()
    quotes = []
    for e in zip(date2num(date), op, hi, lo, cl):
        quotes.append(e)
    candlestick_ohlc(ax, quotes, colorup='blue', colordown='black', width=0.9)
    for label in ax.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))
    ax.grid(True, linewidth=0.3)
    plt.show()
