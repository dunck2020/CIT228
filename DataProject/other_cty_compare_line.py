import csv
import matplotlib.pyplot as plt

filename = 'DataProject/county_pop_data.csv'
NUM_COUNTIES = 82
NUM_DATES = 10
NUM_POP_RECORDS = 830

with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get name, population growth (domestic and international)
    names, pop_growth, counties_net_change = [], [], []
    
    for row in reader:
        sumlev = int(row[0])
        name = (row[6])
        # if name is for grand traverse county fill gt array
        if sumlev==50:
            net_change = 0
            for x in range(86, 97):
                pop_growth_for_year = int(row[x])
                pop_growth.append(pop_growth_for_year)
                net_change += pop_growth_for_year
            if net_change > 0:
                counties_net_change.append(net_change)
                names.append(name)

# set date array - data file has no hard dates
dates=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

name_counter = 0
while name_counter < NUM_COUNTIES:
    # print(names[name_counter])
    # print(county_totals[name_counter])
    date_counter = 0
    while date_counter < NUM_DATES:
        # print(dates[date_counter])
        date_counter += 1
        pop_index = NUM_DATES * name_counter + date_counter
        # print(pop_growth[pop_index])
    name_counter += 1

# print(len(counties_net_change))
# print(len(names))
# plot gt county and michigan population growth
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(counties_net_change, c='blue')
# for name in names:
#     print(name)
# for counties in counties_net_change:
#     print(counties)

# format plot
ax.set_title("Positive Net Migration", fontsize=16)
ax.set_ylabel("Net Migration (Int'l and Domestic)", fontsize=14)
ax.set_xlabel('41 Counties with Growth', fontsize=14)
plt.show()