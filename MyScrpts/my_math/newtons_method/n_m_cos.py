import math as m
import matplotlib.pyplot as plt
def my_derivat_fun(x):
    return -1 - m.sin(x)
def my_func(x):
    return m.cos(x) - x

def xn (x):
    return x - (my_func(x))/(my_derivat_fun(x))
print('1')
xinit = 1

for i in range(100):
    xinit = xn(xinit)
    print(xinit)
y = []
for x in range(1,1000):
    y.append(my_func(x))
plt.plot(list(range(1,1000)), y)
plt.show()


