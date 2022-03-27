import csv
import matplotlib.pyplot as plt

filename = 'DataProject/gt_vs_michigan.csv'

with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get name, population growth (domestic and international)
    names, gt_pop_growth, mi_pop_growth = [], [], []
    gt_county_total = 0
    mi_total = 0
    for row in reader:
        name = (row[6])
        names.append(name)
        # if name is for grand traverse county fill gt array
        if name=="Grand Traverse County":
            for x in range(86, 97):
                gt_pop_growth_for_year = int(row[x])
                gt_pop_growth.append(gt_pop_growth_for_year)
                gt_county_total += gt_pop_growth_for_year

        # if name is for michigan fill michigan array
        if name=="Michigan":
            for x in range(86, 97):
                mi_pop_growth_for_year = int(row[x])
                mi_pop_growth.append(mi_pop_growth_for_year)
                mi_total += mi_pop_growth_for_year

# set date array - data file has no hard dates
dates=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

# plot gt county and michigan population growth
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, gt_pop_growth, c='red', marker='D')
ax.plot(dates, mi_pop_growth, c='blue', marker='p')

# format plot
ax.set_title("Migration to Michigan vs Grand Traverse County", fontsize=16)
ax.set_ylabel("Net Migration Growth", fontsize=14)
ax.set_xlabel('Date', fontsize=14)

plt.show()
