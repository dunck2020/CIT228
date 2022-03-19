import matplotlib.pyplot as plt

imageFormats = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
numTimesImgUsed = [376, 348, 153, 104, 19]
explode = (.2, 0, 0, 0, 0)  # only "explode" the 1st wedge

fig1, ax1 = plt.subplots()
ax1.pie(numTimesImgUsed, explode=explode, labels=imageFormats, autopct='%3.1f%%', shadow=True, startangle=300)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle('Popular Image Formats')

plt.show()