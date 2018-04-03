#import correlation
import pandas as pd
import linreg
import matplotlib
import matplotlib.pyplot as plt



er = pd.read_csv(r'D:\EURRUB_160101_180323.txt')
ur = pd.read_csv(r'D:\USDRUB_160101_180323.txt')

erd=[]
urd = []
for e,u in zip (er['close'], ur['close']):
    erd.append(e)
    urd.append(u)

a,b = linreg.linreg(erd, urd)

ypredict = []
for e in erd:
    ypredict.append(e*b+a)
plt.scatter(erd,urd)
plt.plot(erd, ypredict)
plt.show()
linreg.stderror(erd,urd)