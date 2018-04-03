import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7]
y = [2,8,18,32,50,72, 98]
x2 = [1,2,3]
y2 = [100, 200 ,300]

plt.plot(x,y, label = 'First')
plt.plot (x2, y2, label = 'Second')
plt.xlabel('X')
plt.ylabel(('Y'))
plt.title('FUNCTION\n2nd Line')
plt.legend()

plt.show()