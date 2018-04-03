import matplotlib.pyplot as plt
import numpy as np
import random

y = random.sample( list(range(1000)), 50 )

fig = plt.figure()

ax = plt.subplot2grid((1,1), (0,0))

for label in ax.xaxis.get_ticklabels():
    label.set_rotation(45)

ax.grid(True, linewidth = 0.25)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Title")
ax.plot(range(len(y)),y, label = "Funce")
plt.legend()
plt.subplots_adjust(left=0.05, bottom = 0.16, right = 0.94, top = 1, wspace=0.2, hspace = 0.2)
plt.show()