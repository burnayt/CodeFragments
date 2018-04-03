import matplotlib.pyplot as plt
import random as r

x = [2,4,6,8,10,1]
y =[6,7,8,4,3,1]

plt.bar(x,y,label = 'Bar1', color = 'grey')
plt.bar(y,x, label = 'Bar2', color = 'purple')

plt.xlabel('X')
plt.ylabel(('Y'))
plt.title('FUNCTION\n2nd Line')
plt.legend()

plt.show()