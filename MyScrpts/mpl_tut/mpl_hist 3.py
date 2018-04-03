import matplotlib.pyplot as plt
import random as r

x = []
for e in range(100):
    x.append(round(6*r.random()))

plt.hist(x,bins=[0,2,4,6], histtype='bar', rwidth=0.95, color='black', alpha=0.1 )

plt.xlabel('Numbers')
plt.ylabel(('Frequence'))
plt.title('FUNCTION')


plt.show()