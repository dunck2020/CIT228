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

fig = plt.figure()
ax1 = fig.add_subplot()
ax1.scatter(names,counties_net_change, cmap=plt.cm.Greens, label="people")
ax1.set_ylabel("Positive Net Migration")
ax1.set_xlabel("41 Counties with growth A-Z", fontsize=8)
ax1.set_xticklabels([])  #turns of category x labels
ax1.set_title("We need rollercoasters!!", fontsize=8)
plt.legend(loc='upper left', ncol=2, fontsize=8)
plt.suptitle("Northern Michigan Continues to Grow")
plt.show() 
