import numpy as np
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
plt.xkcd()

dev_x=[25,26,27,28,29,30,31,32,33,34]
x_indexes=np.arange(len(dev_x))
width=0.25

dev_y=[38654,48569,46752,49320,53200,56000,99656,25356,69665,32654]

dev_y_age=[386541,485692,467521,49320,53200,56000,99656,25356,69665,32654]

plt.bar(x_indexes-width, dev_y,color='k',linestyle='--',label="All devs")
plt.bar(x_indexes, dev_y_age,width=width,color='#444444',linewidth=2,label="Python")

plt.bar(x_indexes+width, dev_y,color='k',linestyle='--',label="All devs")

# config plot
plt.xlabel("Ages")
plt.ylabel("Salary")
plt.title("Median Salary by age")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('plot.png')

plt.show()