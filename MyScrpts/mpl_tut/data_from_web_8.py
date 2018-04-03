import urllib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime

myurl ='https://pythonprogramming.net/yahoo_finance_replacement'

s = urllib.request.urlopen(myurl).read().decode().split('\n')
y = []


for i in range(1,len(s)):
    e = s[i].split(',')
    t = []
    t.append( datetime.datetime.strptime(e[0], '%Y-%m-%d') )

    for j in range(1,len(e) ):
        t.append( float(e[j]) )
    y.append(t)
time = []
price = []

for e in y:
    time.append(e[0])
    price.append(e[4])


plt.plot_date(time, price,'-')




plt.xlabel('X')
plt.ylabel(('Y'))
plt.title('FUNCTION\n2nd Line')
plt.legend()

plt.show()