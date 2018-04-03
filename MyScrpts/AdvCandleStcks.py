import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, HourLocator, \
    DayLocator, MONDAY
import matplotlib.finance as f
import datetime
from matplotlib.dates import date2num

mondays = WeekdayLocator(MONDAY)  # major ticks on the mondays
alldays = DayLocator()  # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')  # e.g., 12

date = []
op = []
hi = []
lo =[]
cl = []

with open(r'D:\Gold.txt') as g:
    for e in list(g)[1:]:
        lstmp = e.split(',')
        #DATE
        strl = lstmp[0]
        date.append(datetime.datetime.strptime(strl, '%Y%m%d'))
        #OPEN
        strl = lstmp[2]
        op.append(float(strl))
        #HIGH
        strl = lstmp[3]
        hi.append(float(strl))
        #LOW
        strl = lstmp[4]
        lo.append(float(strl))
        #CLOSE
        strl = lstmp[5]
        cl.append(float(strl))

quotes = []
for e in zip(date2num(date), op, hi, lo, cl):
    quotes.append(e)

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
# ax.xaxis.set_minor_formatter(dayFormatter)

# plot_day_summary(ax, quotes, ticksize=3)
f.candlestick_ohlc(ax, quotes, width=0.6)

ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()




