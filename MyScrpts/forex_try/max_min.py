import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import date2num
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime


ax = plt.subplot()
def graph_ycs(ax):
    date = []
    op = []
    hi = []
    lo = []
    cl = []

    with open(r'D:\Data\USDRUB_170101_180401.txt') as data:
        for e in list(data)[1:]:
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
    quotes = []
    for e in zip(date2num(date), op, hi, lo, cl):
        quotes.append(e)
    candlestick_ohlc(ax, quotes, colorup='blue', colordown='black', width=0.9)
    for label in ax.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))
    ax.grid(True, linewidth=0.3)

    return date, op, hi, lo, cl


date, op, hi, lo, cl = graph_ycs(ax)

#find max
max_interval = 5

for i in range(max_interval, len(hi) - max_interval):
    cur_max = hi[i]
    is_max = False
    for j in range(i-max_interval,i+max_interval):
        if(cur_max < hi[j]):
            is_max = False
            break
        else:
            is_max = True
    if is_max == True:
        ax.text(date[i], hi[i], 'Mx')

min_interval = 3
close_percent = 0.35

for i in range(min_interval, len(hi) - min_interval):
    cur_min = lo[i]
    is_min = False
    for j in range(i-min_interval,i+min_interval):
        if(cur_min > lo[j]):
            is_min = False
            break
        else:
            is_min = True

    if is_min == True:
        ax.text(date[i], lo[i], 'Mn')
plt.show()





