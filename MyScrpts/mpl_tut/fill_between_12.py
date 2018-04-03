import matplotlib.pyplot as plt
import statistics as s

time = list (range(100))
y = [x**2 for x in time]
print(y)

#fig = plt.figure()
ax = plt.subplot()
ax.fill_between(time, y , s.mean(y))
plt.show()