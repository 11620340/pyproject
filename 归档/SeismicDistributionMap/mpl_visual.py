import matplotlib.pyplot as plt
import main

# plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(main.dates, main.highs, c = 'red')
ax.plot(main.dates, main.lows, c = 'blue')
ax.fill_between(main.dates, main.highs, main.lows, facecolor='blue', alpha=0.1)

ax.axes.xaxis.set_ticks(range(0, 365, 60))
fig.autofmt_xdate()

plt.show()