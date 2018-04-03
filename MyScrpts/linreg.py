import statistics as s
import correlation as cor


def linreg(x,y):
    xmean = s.mean(x)
    ymean = s.mean(y)
    a = 0
    b = 0
    ssx = 0
    ssy = 0
    for i,j in zip(x,y):
        ssx += (i - xmean)**2
        ssy += (j - ymean)**2
    r = cor.corr(x,y)
    b = (ssy/ssx)**0.5
    b = b*r
    a = ymean - b*xmean
    return a,b


def stderror(x, y):
    a,b = linreg(x,y)
    sumy = 0
    for i,j in zip(x,y):
        ypredict = b*i+a
        sumy += (j - ypredict)**2
    return ( sumy / (len(x)-2) )**0.5