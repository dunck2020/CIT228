import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Northern Michigan', 'Upper Peninsula', 'SW Michigan', 'SE Michigan'
coolFactor = [75, 50, 30, 16]
explode = (.1, 0, 0, 0)  # only "explode" the 1st wedge
wedgeColors=('tomato','mediumseagreen','plum','darkslategray')
fig1, ax1 = plt.subplots()
ax1.pie(coolFactor, explode=explode, labels=labels, autopct='%3.1f%%', shadow=False, startangle=0)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle("Best Places in Michigan Factor")

plt.show()
