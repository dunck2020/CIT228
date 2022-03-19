import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'Chapter16/internationalfallstemp2021.csv'
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # get the high temps and low temps
    dates, hightemps, lowtemps = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%m/%d/%Y')
        dates.append(current_date)
        lowtemp = int(row[5])
        lowtemps.append(lowtemp)
        hightemp = int(row[4])
        hightemps.append(hightemp)

# plot the high and low temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, hightemps, c='red')
ax.plot(dates, lowtemps, c='blue')
ax.fill_between(dates, hightemps, lowtemps, facecolor='darkgray', alpha=0.5)
# format plot
ax.set_title("Daily High and Low Temps for International Falls,MN", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.set_xlabel('Date', fontsize=14)
fig.autofmt_xdate()
ax.tick_params(which='major', labelsize=8)

plt.show()