from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
"""
print(header_row)


for index, column_header in enumerate(header_row):
    print(index, column_header)
"""

# Extract dates and high temperatures.
dates, highs = [], []
for row in reader:
    curent_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(curent_date)
    highs.append(high)

# print(highs)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Format plot.
ax.set_title("Daily High Tempratures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()