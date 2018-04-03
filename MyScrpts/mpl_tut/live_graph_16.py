import matplotlib.pyplot as plt
import matplotlib.animation as animation
from  matplotlib import style
style.use('fivethirtyeight')

fig = plt.figure()

ax = fig.add_subplot(1,1,1)
def anim(i):
    with open(r'D:\anim.txt') as g:
        l1 = list(g)
        x = []
        y = []
        for e in l1:
            stre = e.split()
            x.append(float(stre[0]))
            y.append(float(stre[1]))

    ax.clear()
    ax.plot(x, y)
ani = animation.FuncAnimation(fig,anim, interval= 1000)

plt.show()


