from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
plt.xkcd()

dev_x=[25,26,27,28,29,30,31,32,33,34]
dev_y=[38654,48569,46752,49320,53200,56000,99656,25356,69665,32654]
dev_y_age=[386541,485692,467521,49320,53200,56000,99656,25356,69665,32654]

plt.plot(dev_x, dev_y,color='k',linestyle='--',marker='.',label="All devs")
plt.plot(dev_x, dev_y_age,color='#444444',marker='o',linewidth=2,label="Python")

# config plot
plt.xlabel("Ages")
plt.ylabel("Salary")
plt.title("Median Salary by age")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('plot.png')

plt.show()