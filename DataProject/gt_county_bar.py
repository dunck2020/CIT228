import csv
import matplotlib.pyplot as plt

filename = 'DataProject/gt_vs_michigan.csv'

with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get name, population growth (domestic and international)
    names, gt_pop_growth = [], []
    gt_county_total = 0
    for row in reader:
        name = (row[6])
        names.append(name)
        # if name is for grand traverse county fill gt array
        if name=="Grand Traverse County":
            for x in range(86, 97):
                gt_pop_growth_for_year = int(row[x])
                gt_pop_growth.append(gt_pop_growth_for_year)
                gt_county_total += gt_pop_growth_for_year

# set date array - data file has no hard dates
dates=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
range=[-500, 0, 0, 500]
plt.bar(dates, gt_pop_growth, color="mediumaquamarine",width=.50)
plt.tick_params(which='major',labelsize=10, color="navy", width=5, length=10, pad=10)
plt.ylabel("Number of Folks") 
plt.xlabel("Year") 
plt.title("GT County Net Migration - 10 Years over 6000") 
plt.show() 